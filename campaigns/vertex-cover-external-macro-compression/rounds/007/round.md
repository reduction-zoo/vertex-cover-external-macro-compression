# Round 007 — later dictionary-compression gadget audit

## Plan

Gap: the original unrestricted EPM proof is inaccessible, and local
gadgets fail through dictionary adjacency. Mechanism: inspect recent
primary hardness papers for dictionary-based compression or phrase
selection, looking for an explicit Vertex Cover gadget with a converse
that accounts for arbitrary substrings of a shared dictionary. First
discriminating check: identify a full proof, read its output model and
normalization lemma, then test whether those hypotheses match EPM.
Prior evidence: rounds 002 and 005 give concrete overlap failures.
Scope: papers that provide their own proof, not surveys or issue sketches.

## Evidence and diagnosis

[Rawitz et al., *The Minimum Substring Cover Problem*, Lemma 1](https://www.eng.biu.ac.il/~rawitzd/Papers/substring.pdf)
has an explicit Vertex Cover/Hypergraph Cover reduction: a vertex is a
two-character substring, and each edge string requires at least one
chosen vertex substring. Its converse relies on assigning infinite cost
to every non-vertex substring. EPM has no such phrase-price restriction;
rounds 004/005 exhibit precisely the cheaper non-vertex substring that
invalidates a direct transfer.

[Banbara et al., KR 2026](https://proceedings.kr.org/2026/66/)
provides exact Answer Set Programming encodings for smallest
bidirectional macro schemes and straight-line programs. Its published
abstract describes solver encodings, not an EPM reduction or a Vertex
Cover extraction. [Kempa et al., ESA 2018](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2018.52)
proves a reduction between string attractors and set cover under a
different output model. Neither supplies a normal-form lemma for EPM
dictionary intervals.

First check outcome: a full proof exists for a related phrase-selection
problem, but its infinite phrase weights are incompatible with this
target. No target instances or recovery outputs were checked this round
(literature scope only). Experience extraction: none; the incompatibility
is already represented by the round 002/005 arbitrary-interval entry.

## Next action

Stop discovery with 13 rounds unspent. Three distinct construction
mechanisms have concrete false-YES counterexamples; the unrestricted
primary proof remains inaccessible, and the checked adjacent proofs
require extra restrictions. A future attempt should start from an
accessible full Storer report or an independently proved EPM
normalization/charging lemma, not adjust these thresholds.
