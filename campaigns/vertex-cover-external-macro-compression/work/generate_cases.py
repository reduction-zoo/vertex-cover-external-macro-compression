"""Rebuild the fixed Vertex Cover corpus; source expectations use enumeration."""

import itertools
import json
import random
from pathlib import Path


HERE = Path(__file__).parent


def cover(source):
    n, edges, k = source["n"], source["edges"], source["k"]
    for size in range(min(k, n) + 1):
        for subset in itertools.combinations(range(n), size):
            chosen = set(subset)
            if all(u in chosen or v in chosen for u, v in edges):
                return list(subset)
    return None


def random_source(seed):
    rng = random.Random(seed)
    n = rng.randrange(3, 9)
    probability = rng.choice((0.2, 0.4, 0.6, 0.8))
    edges = [[u, v] for u in range(n) for v in range(u + 1, n)
             if rng.random() < probability]
    return {"n": n, "edges": edges, "k": rng.randrange(n + 1)}


def main():
    edge = [
        (0, [], 0), (1, [], 0), (1, [], 1),
        (2, [[0, 1]], 0), (2, [[0, 1]], 1),
        (3, [[0, 1], [1, 2]], 0), (3, [[0, 1], [1, 2]], 1),
        (3, [[0, 1], [1, 2], [0, 2]], 1),
        (3, [[0, 1], [1, 2], [0, 2]], 2),
        (4, [[0, 1], [2, 3]], 1), (4, [[0, 1], [2, 3]], 2),
        (4, [[0, 1], [1, 2], [2, 3], [0, 3]], 1),
    ]
    cases = []
    seen = set()
    for n, edges, k in edge:
        source = {"n": n, "edges": edges, "k": k}
        cases.append({"kind": "edge", "source": source,
                      "expected": {"cover": cover(source)} if cover(source) is not None else "NO-SOLUTION"})
        seen.add(json.dumps(source, sort_keys=True))
    for seed in range(1000):
        source = random_source(seed)
        key = json.dumps(source, sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        witness = cover(source)
        cases.append({"kind": "random", "seed": seed, "source": source,
                      "expected": {"cover": witness} if witness is not None else "NO-SOLUTION"})
        if len(cases) == 120:
            break
    assert len(cases) == 120
    (HERE / "cases.json").write_text(json.dumps(cases, indent=2) + "\n")


if __name__ == "__main__":
    main()
