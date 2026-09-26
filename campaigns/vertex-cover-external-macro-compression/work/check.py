"""Independent finite oracles and end-to-end injection for the fixed contract."""

import argparse
import itertools
import json
import subprocess
import sys
from pathlib import Path

import z3

from generate_cases import cover, random_source


HERE = Path(__file__).parent
ROOT = HERE.parents[2]


def source_oracle(source):
    n, edges, k = source["n"], source["edges"], source["k"]
    variables = [z3.Bool(f"v{i}") for i in range(n)]
    solver = z3.Solver()
    if variables:
        solver.add(z3.PbLe([(v, 1) for v in variables], k))
    solver.add(*(z3.Or(variables[u], variables[v]) for u, v in edges))
    answer = solver.check()
    if answer == z3.unsat:
        return "NO-SOLUTION"
    if answer != z3.sat:
        raise RuntimeError(f"Z3 returned {answer}")
    model = solver.model()
    return {"cover": [i for i, v in enumerate(variables) if z3.is_true(model.eval(v))]}


def valid_source(source, output):
    if output == "NO-SOLUTION":
        return cover(source) is None
    if not isinstance(output, dict) or set(output) != {"cover"}:
        return False
    vertices = output["cover"]
    if not isinstance(vertices, list) or any(type(v) is not int or v < 0 or v >= source["n"] for v in vertices):
        return False
    chosen = set(vertices)
    return len(chosen) == len(vertices) and len(chosen) <= source["k"] and all(
        u in chosen or v in chosen for u, v in source["edges"])


def expand(dictionary, tokens):
    """Pointers address inclusive-exclusive intervals of dictionary tokens."""
    active = set()
    memo = {}

    def token_at(i):
        if i in active:
            raise ValueError("recursive pointer cycle")
        if i in memo:
            return memo[i]
        active.add(i)
        value = render(dictionary[i])
        active.remove(i)
        memo[i] = value
        return value

    def render(token):
        if not isinstance(token, dict) or len(token) != 1:
            raise ValueError("bad token")
        if "lit" in token:
            value = token["lit"]
            if not isinstance(value, str) or len(value) != 1:
                raise ValueError("bad literal")
            return value
        if "ptr" not in token:
            raise ValueError("bad token")
        interval = token["ptr"]
        if (not isinstance(interval, list) or len(interval) != 2 or
                any(type(x) is not int for x in interval)):
            raise ValueError("bad pointer")
        lo, hi = interval
        if not 0 <= lo < hi <= len(dictionary):
            raise ValueError("bad interval")
        return "".join(token_at(j) for j in range(lo, hi))

    for i in range(len(dictionary)):
        token_at(i)
    return "".join(render(token) for token in tokens)


def valid_target(target, output):
    if output == "NO-SOLUTION":
        return solve_target(target) == "NO-SOLUTION"
    if not isinstance(output, dict) or set(output) != {"D", "C"}:
        return False
    dictionary, compressed = output["D"], output["C"]
    if not isinstance(dictionary, list) or not isinstance(compressed, list):
        return False
    tokens = dictionary + compressed
    cost = sum(1 if isinstance(t, dict) and "lit" in t else target["h"] for t in tokens)
    if cost > target["B"]:
        return False
    try:
        return expand(dictionary, compressed) == target["s"]
    except (ValueError, RecursionError):
        return False


def solve_target(target):
    s, h, budget = target["s"], target["h"], target["B"]
    if budget >= len(s):
        return {"D": [], "C": [{"lit": char} for char in s]}
    if budget > 5:
        raise RuntimeError("target exhaustive oracle restricted to budgets at most 5")
    alphabet = sorted(set(s))
    for length in range(budget + 1):
        literals = [({"lit": char}, 1) for char in alphabet]
        pointers = [({"ptr": [lo, hi]}, h)
                    for lo in range(length) for hi in range(lo + 1, length + 1)]
        options = literals + pointers
        for entries in itertools.product(options, repeat=length):
            dictionary = [token for token, _ in entries]
            dcost = sum(cost for _, cost in entries)
            if dcost + h > budget:
                continue
            try:
                expanded = expand(dictionary, [])
                del expanded
                phrases = [("".join(expand(dictionary, [{"ptr": [lo, hi]}])), lo, hi)
                           for lo in range(length) for hi in range(lo + 1, length + 1)]
            except (ValueError, RecursionError):
                continue
            paths = {0: (0, [])}
            for i in range(len(s)):
                if i not in paths:
                    continue
                used, path = paths[i]
                choices = [(s[i], {"lit": s[i]}, 1)] + [
                    (phrase, {"ptr": [lo, hi]}, h) for phrase, lo, hi in phrases]
                for phrase, token, cost in choices:
                    end = i + len(phrase)
                    if s.startswith(phrase, i) and used + cost <= budget - dcost:
                        if end not in paths or paths[end][0] > used + cost:
                            paths[end] = (used + cost, path + [token])
            if len(s) in paths:
                return {"D": dictionary, "C": paths[len(s)][1]}
    return "NO-SOLUTION"


def self_test():
    subprocess.run([sys.executable, ROOT / "research/validate_preparation.py", HERE / "cases.json"], check=True)
    cases = json.loads((HERE / "cases.json").read_text())
    yes = no = 0
    for case in cases:
        source = case["source"]
        if case["kind"] == "random" and random_source(case["seed"]) != source:
            raise AssertionError("seed regeneration mismatch")
        brute = cover(source)
        expected = case["expected"]
        assert expected == ({"cover": brute} if brute is not None else "NO-SOLUTION")
        z3_output = source_oracle(source)
        assert valid_source(source, z3_output)
        assert (z3_output == "NO-SOLUTION") == (brute is None)
        if source["k"] < source["n"]:
            assert not valid_source(source, {"cover": list(range(source["n"]))})
        yes += brute is not None
        no += brute is None
    assert valid_source({"n": 2, "edges": [[0, 1]], "k": 1}, {"cover": [0]})
    assert not valid_source({"n": 2, "edges": [[0, 1]], "k": 1}, {"cover": []})
    assert not valid_source({"n": 2, "edges": [[0, 1]], "k": 1}, {"cover": [0, 0]})
    assert not valid_source({"n": 2, "edges": [[0, 1]], "k": 1}, "NO-SOLUTION")
    assert solve_target({"s": "aaaaaa", "h": 1, "B": 5}) != "NO-SOLUTION"
    assert solve_target({"s": "aaaaaa", "h": 1, "B": 4}) == "NO-SOLUTION"
    assert solve_target({"s": "abc", "h": 1, "B": 2}) == "NO-SOLUTION"
    assert valid_target({"s": "aaaaaa", "h": 1, "B": 5},
                        {"D": [{"lit": "a"}, {"lit": "a"}],
                         "C": [{"ptr": [0, 2]}] * 3})
    assert not valid_target({"s": "aaaaaa", "h": 1, "B": 4},
                            {"D": [{"lit": "a"}, {"lit": "a"}],
                             "C": [{"ptr": [0, 2]}] * 3})
    assert not valid_target({"s": "a", "h": 1, "B": 1},
                            {"D": [{"ptr": [0, 1]}], "C": [{"ptr": [0, 1]}]})
    print(f"source cases: {len(cases)}; YES {yes}; NO {no}; target fixtures passed")


def candidate_test(path):
    cases = json.loads((HERE / "cases.json").read_text())
    checked = 0
    for case in cases:
        source = case["source"]
        target = json.loads(subprocess.check_output([sys.executable, path], input=json.dumps(source).encode()))
        target_output = solve_target(target)
        assert valid_target(target, target_output)
        recovered = json.loads(subprocess.check_output(
            [sys.executable, path, "--extract"],
            input=json.dumps({"source": source, "target_solution": target_output}).encode()))
        assert valid_source(source, recovered), (source, target, target_output, recovered)
        checked += 1
    print(f"candidate injection passed: {checked} instances")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--candidate", type=Path)
    args = parser.parse_args()
    if args.self_test:
        self_test()
    elif args.candidate:
        candidate_test(args.candidate)
    else:
        parser.error("choose --self-test or --candidate")
