# Round 005 — long-delimiter, one-copy edge gadget

## Plan

Gap: repeated edge blocks create whole-edge shortcuts. Mechanism: use one
edge block per edge, `Q=##`, a three-symbol private vertex name `vvv`,
`h=5`, and two calibration copies of `QvvvQ` per vertex. An edge block
is `Q uuu Q vvv Q`; either endpoint phrase saves two units, whereas
the complementary short fragment costs as much as its literal expansion,
so double coverage appears to give no extra saving. Add a highly
repeated anchor `Q zzz Q` to pay the initial dictionary `Q` overhead.
Prior evidence: rounds 002/004 require arbitrary-interval and whole-edge
checks. First discriminating check: compute explicit costs for a selected
set on an edge and a triangle, then inspect all repeated factors longer
than `h` for an unintended pointer phrase. If a longer factor repeats,
the proposed converse needs revision. Scope: this new gadget family,
not a final theorem until every dictionary is covered.

## Evidence and diagnosis

`uv run python campaigns/vertex-cover-external-macro-compression/rounds/005/probe.py`
checked one edge and a triangle with `T=10` anchor copies. All factors
of length at least six occurring twice in the *source string* were
substrings of an intended `##vvv##` phrase. The intended canonical
cost is `|s|-2T+7+|S|-2|covered edges|`. For one edge, the checked
costs were 112 with no selected vertex and 111 with one selected vertex.

The first check exposed a different failure: the *dictionary* can create
a useful factor not repeated in `s`. Place selected phrases for `a`
and `b` adjacently: `##zzz##aaa##bbb##`. Their combined interval is the
whole edge block `##aaa##bbb##`, so one pointer costs five instead of
the canonical ten. For the triangle and `k=1`, selecting `{a,b}` yields
the concrete valid EPM of cost **145** in [counterexample.json](counterexample.json),
below the proposed bound **149**, although the triangle has no
one-vertex cover. The independent validator checked expansion, recursion
termination and exact cost. Three target witnesses across the probe's
graphs were checked; no global optima or recovered outputs were claimed.

Diagnosis: a source repeated-factor inventory does not constrain
substrings created at dictionary concatenation boundaries. The proposed
converse is false. This excludes this exact long-delimiter calibration
gadget, not all one-copy edge gadgets. Experience extraction: updated the
round 002 entry with this distinct manifestation of the same arbitrary
interval hazard; no new entry.

## Next action

Seek the 1977 primary proof through archives or institutional mirrors;
it may reveal a delimiter/parameter technique that controls dictionary
adjacency.
