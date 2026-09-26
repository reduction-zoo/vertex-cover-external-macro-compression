"""Check long-delimiter gadget costs and repeated substrings."""

import collections
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import valid_target


Q = "##"
H = 5
T = 10


def phrase(v):
    return Q + v * 3 + Q


def make(vertices, edges, selected):
    fresh = iter(chr(x) for x in range(0xE000, 0xF000))
    blocks = [(phrase("z"), "z") for _ in range(T)]
    blocks += [(phrase(v), v) for v in vertices for _ in range(2)]
    blocks += [(Q + u * 3 + Q + v * 3 + Q, (u, v)) for u, v in edges]
    blocks = [(block, owner, next(fresh)) for block, owner in blocks]
    s = "".join(block + marker for block, _, marker in blocks)
    d = phrase("z") + "".join(v * 3 + Q for v in sorted(selected))
    D = [{"lit": char} for char in d]
    C = []
    for block, owner, marker in blocks:
        if owner == "z" or isinstance(owner, str) and owner in selected:
            lo = d.index(phrase(owner))
            C.append({"ptr": [lo, lo + 7]})
        elif isinstance(owner, tuple) and block in d:
            lo = d.index(block)
            C.append({"ptr": [lo, lo + len(block)]})
        elif isinstance(owner, tuple) and any(v in selected for v in owner):
            u, v = owner
            chosen = u if u in selected else v
            lo = d.index(phrase(chosen))
            if chosen == u:
                C += [{"ptr": [lo, lo + 7]}] + [{"lit": c} for c in v * 3 + Q]
            else:
                C += [{"lit": c} for c in Q + u * 3] + [{"ptr": [lo, lo + 7]}]
        else:
            C += [{"lit": c} for c in block]
        C.append({"lit": marker})
    output = {"D": D, "C": C}
    cost = len(D) + sum(1 if "lit" in t else H for t in C)
    assert valid_target({"s": s, "h": H, "B": cost}, output)
    return s, output, cost


def repeats(s):
    found = collections.Counter(s[i:j] for i in range(len(s))
                                for j in range(i + 6, min(i + 13, len(s) + 1)))
    return {p: count for p, count in found.items() if count >= 2}


for vertices, edges, chosen in [
    ("ab", [("a", "b")], set()),
    ("ab", [("a", "b")], {"a"}),
    ("abc", [("a", "b"), ("a", "c"), ("b", "c")], {"a", "b"}),
]:
    s, output, cost = make(vertices, edges, chosen)
    expected = len(s) - 2 * T + 7 + len(chosen) - 2 * sum(
        u in chosen or v in chosen for u, v in edges)
    assert cost <= expected
    long_repeats = repeats(s)
    allowed = [phrase(v) for v in "z" + vertices]
    bad = [p for p in long_repeats if not any(p in a for a in allowed)]
    assert not bad, bad
    if vertices == "abc":
        target = {"s": s, "h": H, "B": len(s) - 2 * T + 7 + 1 - 2 * len(edges)}
        assert cost < target["B"]
        assert valid_target(target, output)
        (Path(__file__).parent / "counterexample.json").write_text(
            json.dumps({"source": {"n": 3, "edges": [[0, 1], [0, 2], [1, 2]], "k": 1},
                        "target": target, "target_output": output}, indent=2) + "\n")
    print(json.dumps({"vertices": vertices, "edges": edges, "selected": sorted(chosen),
                      "length": len(s), "cost": cost,
                      "repeated_factors_at_least_six": len(long_repeats)}))
