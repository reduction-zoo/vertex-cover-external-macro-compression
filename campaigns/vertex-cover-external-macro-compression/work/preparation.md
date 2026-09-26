# Prepare, 2026-09-25

The fixed corpus has 120 distinct source instances: 12 hand-designed edge
cases and 108 cases from `random.Random(seed)` with recorded seeds in 0–114
(seven duplicate source encodings were skipped). Counts by `(kind, n)` are:
edge: `0:1, 1:2, 2:2, 3:4, 4:3`; random:
`3:15, 4:22, 5:17, 6:21, 7:20, 8:13`. Sizes span 0–8 vertices.
Enumeration fixes the expected answers before a
candidate; 70 admit a cover and 50 do not. The source oracle separately uses
Z3 5.1.0.0: one Boolean per vertex, one disjunction per edge and a
pseudo-Boolean cardinality bound. A satisfying assignment is checked against
the graph and `k`; `unsat` is interpreted as `NO-SOLUTION`; `unknown` fails.
Exhaustive subset enumeration checks every stored answer and Z3 decision.

The target finite oracle enumerates dictionary token arrays with cost within
budget, including recursive pointers and cycles, over the source string's
alphabet. For each acyclic dictionary, dynamic programming finds a minimum
cost compressed sequence of literals and dictionary pointers. The enumeration
is complete for the token-index model in `contract.md` when `B <= 5`, assuming
unused dictionary literals outside the output alphabet can be removed.
For `B >= len(s)`, the all-literal witness is immediate. A `NO-SOLUTION`
answer with `B > 5` raises an explicit unsupported-domain error. This is a
small-instance oracle, not a polynomial target solver. The corpus alone does
not establish that the target interpretation matches the fixed question.

Reproduce: `uv sync --locked`; then
`uv run python campaigns/vertex-cover-external-macro-compression/work/check.py --self-test`.
The self-test first runs `research/validate_preparation.py`, regenerates
random inputs from seeds, recomputes all labels by enumeration, checks Z3
witnesses, rejects false source witnesses and NO answers, and checks feasible,
infeasible, over-budget and cyclic target fixtures. On 2026-09-25 it passed:
120 source instances, 70 YES, 50 NO, and target fixtures. The initial run
found a Z3 empty-graph encoding error; the guard was fixed before this pass.

The candidate command is `uv run python .../work/check.py --candidate
.../work/algorithm.py`. It executes both subprocess modes and checks recovered
source answers. It will fail explicitly if a constructed target instance is
outside the finite oracle's negative-answer domain. It currently exercises
one target output per source input; alternate target witnesses remain a
verification obligation for a complete candidate.
