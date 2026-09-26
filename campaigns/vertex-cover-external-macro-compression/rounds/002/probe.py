"""Check whether EPM intervals collapse the grammar gadget's rule costs."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import valid_target


def word(edges):
    pieces = []
    fresh = iter(chr(i) for i in range(0xE000, 0xE100))
    for vertex in "ab":
        for _ in range(2):
            pieces.append(f"#{vertex}{next(fresh)}{vertex}#{next(fresh)}")
    for vertex in "ab":
        pieces.append(f"#{vertex}#{next(fresh)}")
    for u, v in edges:
        pieces.append(f"#{u}#{v}#{next(fresh)}")
    return "".join(pieces)


def compressed(s, dictionary):
    paths = {0: (0, [])}
    phrases = [(dictionary[a:b], a, b)
               for a in range(len(dictionary))
               for b in range(a + 2, len(dictionary) + 1)]
    for i in range(len(s)):
        if i not in paths:
            continue
        cost, path = paths[i]
        choices = [(s[i], {"lit": s[i]})] + [
            (phrase, {"ptr": [a, b]}) for phrase, a, b in phrases]
        for phrase, token in choices:
            end = i + len(phrase)
            if s.startswith(phrase, i) and (end not in paths or paths[end][0] > cost + 1):
                paths[end] = (cost + 1, path + [token])
    return paths[len(s)]


dictionary = "#a#b#"
factors = ["#a", "a#", "#a#", "#b", "b#", "#b#"]
assert all(phrase in dictionary for phrase in factors)
for edges in ([], [("a", "b")]):
    s = word(edges)
    cost, C = compressed(s, dictionary)
    output = {"D": [{"lit": c} for c in dictionary], "C": C}
    assert valid_target({"s": s, "h": 1, "B": len(dictionary) + cost}, output)
    if edges:
        (Path(__file__).parent / "counterexample.json").write_text(
            json.dumps({"source": {"n": 2, "edges": [[0, 1]], "k": 0},
                        "target": {"s": s, "h": 1, "B": 33},
                        "target_output": output}, indent=2) + "\n")
    print(json.dumps({"edges": edges, "length": len(s), "dictionary": dictionary,
                      "cost": len(dictionary) + cost,
                      "grammar_k0_threshold": 30 + 3 * len(edges)}))
