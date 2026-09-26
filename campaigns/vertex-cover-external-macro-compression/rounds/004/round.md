# Round 004 — repeated edge blocks with vertex dictionary phrases

## Plan

Gap: a dictionary phrase `#v#` of length three costs three at `h=2`
and saves one symbol in an edge block `#u#v#`; the secondary account of
Storer's proof suggests a node-name/delimiter mechanism. Mechanism:
repeat each edge block to amplify the benefit of storing an endpoint.
Prior evidence: round 002 ruled out directly importing grammar rule costs.
First discriminating check: for the one-edge graph with `k=0`, compare
the intended no-cover threshold against a dictionary that stores the
entire repeated edge block. A witness below threshold invalidates this
amplification. Scope: repeated identical edge blocks with one-symbol
vertex names and `h=2`, not arbitrary node-name encodings.

## Evidence and diagnosis

For an edge `{a,b}`, four copies of `#a#b#`, `h=2`, and the natural
threshold `4R+3k=16` for `R=4`, the graph with `k=0` has no vertex
cover. Yet `D=#a#b#` (five literals) and four pointers to all of `D`
in `C` cost `5+4·2=13`. `uv run python
campaigns/vertex-cover-external-macro-compression/rounds/004/probe.py`
constructed and independently validated this exact witness in
[counterexample.json](counterexample.json). One target witness and one
source NO instance were checked; no optimum or recovery output was
claimed.

Diagnosis: repeating the same edge block creates a longer reusable
phrase with a larger per-copy saving than either endpoint phrase. This
excludes the repeated-identical-edge amplification, not a one-copy edge
gadget or repetition with truly unique interior content. Experience
extraction: none; the general overlap warning from round 002 already
covers this shortcut, so a second entry would duplicate it.

## Next action

Try one copy per edge, a longer shared delimiter, and calibration blocks
that pay most of each selected vertex's dictionary cost.
