# Round 002 — transfer repeated-factor grammar gadget to EPM

## Plan

Gap: Casel et al.'s grammar gadget relates `#v#` selection to covering an
edge, but EPM pointers may reference arbitrary overlapping dictionary
intervals. Mechanism: use its unique-symbol repeated-factor word with
`h=1` and test whether the purported optional `#v#` phrase still has a
per-vertex storage cost. Prior evidence: round 001 identified the exact
factor family and the overlap distinction. First discriminating check:
build one dictionary containing all `#v#` phrases for a two-vertex graph,
then verify that both `#v` and `v#` are addressable without separate
entries and compute a compressed edge block. If yes, the grammar cost
accounting does not transfer directly. This round tests this mechanism,
not all possible EPM gadgets.

## Evidence and diagnosis

`uv run python campaigns/vertex-cover-external-macro-compression/rounds/002/probe.py`
constructed the Casel et al. unbounded-alphabet word for two vertices,
with one unique diamond per specified position. The dictionary `#a#b#`
stores five literals yet exposes all six factors `#a`, `a#`, `#a#`,
`#b`, `b#`, `#b#` as addressable intervals. For the graph with edge
`{a,b}` and `k=0`, its 38-symbol word has a valid EPM of cost **27**;
the direct grammar threshold `15n+3m+k` is **33**. The exact target
instance and EPM witness are in [counterexample.json](counterexample.json).
The independent validator accepted its expansion and cost. This is one
actual target witness and one source NO instance; no target optimum or
recovered source output was claimed.

Diagnosis: the grammar proof charges separately for named rules. EPM
pointers can refer to any interval of a single dictionary, so composing
all full vertex factors makes every optional `#v#` available at no
separate rule cost. The direct threshold therefore produces a false YES
on this input. This excludes only this unmodified grammar-to-EPM transfer,
not all reductions based on repeated factors. Experience extraction:
[arbitrary intervals collapse entry costs](../../../../research/experience/arbitrary-intervals-collapse-entry-costs.md).

## Next action

Investigate a new encoding that charges vertex choices despite arbitrary
dictionary intervals, or establish from primary sources why a restricted
variant can be reduced to unrestricted EPM.
