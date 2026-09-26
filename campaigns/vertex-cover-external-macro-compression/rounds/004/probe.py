"""A whole-edge phrase beats the repeated-vertex-gadget threshold."""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "work"))
from check import valid_target


block = "#a#b#"
repeats = 4
target = {"s": block * repeats, "h": 2, "B": 4 * repeats}
output = {"D": [{"lit": char} for char in block],
          "C": [{"ptr": [0, len(block)]} for _ in range(repeats)]}
assert valid_target(target, output)
assert len(output["D"]) + 2 * len(output["C"]) == 13 < target["B"]
data = {"source": {"n": 2, "edges": [[0, 1]], "k": 0},
        "target": target, "target_output": output}
(Path(__file__).parent / "counterexample.json").write_text(json.dumps(data, indent=2) + "\n")
print("whole-edge EPM cost 13 < intended no-cover threshold 16")
