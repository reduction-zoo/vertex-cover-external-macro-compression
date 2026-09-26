# Round 001 — primary-source model audit

## Plan

Gap: the fixed target description leaves dictionary pointer endpoint and
recursive expansion conventions implicit. Mechanism: a standalone literature
investigation of the cited Storer and Storer-Szymanski primary sources and the
upstream issue. Prior evidence is only the question brief; the board's local
experience collection has no entries. First discriminating check: locate an
actual theorem and construction from Vertex Cover to external macro
compression, with a definition matching the fixed cost and pointer semantics.
If one matches, transcribe its exact parameters and test a small instance;
otherwise document the mismatch and decide whether a fresh construction is
needed. Scope ends at the cited primary papers and directly cited references.

## Evidence and diagnosis

Sources checked on 2026-09-25:

- [Garey–Johnson SR22](https://perso.limos.fr/~palafour/PAPERS/PDF/Garey-Johnson79.pdf),
  entry SR22: pointers identify substrings of `D`; cost is one per literal
  and `h` per pointer. The entry asserts a Vertex Cover transformation but
  gives no gadget or converse proof. It explicitly permits pointers in `D`
  and says several restricted variants are hard.
- [Storer–Szymanski 1982](https://doi.org/10.1145/322344.322346),
  bibliographic/abstract access only; the full PDF request returned HTTP 403.
  The cited 1977 Princeton report and 1978 STOC abstract were located by
  citation but no accessible primary full proof was found in this scope.
- [Casel et al. 2021, §2.4](https://link.springer.com/article/10.1007/s00224-020-10013-w)
  is a primary paper for its own grammar result and explicitly restates EPM:
  a pointer `(i,j)` references positions of the *encoded dictionary word*
  `s0`, and replacement is repeated until the output is literal. This
  agrees with the token-index convention in Prepare. It distinguishes EPM
  with overlapping pointers from smallest grammars. Its sketched Vertex
  Cover grammar reduction uses unique separator symbols and repeated
  `#v`, `v#`, `#v#` factors; the detailed proof is for grammars, not the
  unrestricted EPM target here.
- [Upstream issue #455](https://github.com/CodingThrust/problem-reductions/issues/455)
  supplies only a schematic construction. Its example represents each
  vertex by one symbol and takes `h=2`, then proposes replacing vertex
  symbols by pointers. Such a replacement costs two units instead of one,
  before dictionary storage, so it cannot give the claimed saving.

First check outcome: no compatible complete construction was found. One
precise semantics question is resolved for the classical EPM: endpoints
index dictionary tokens. The upstream sketch is not executable evidence.
No target instances or recovery outputs were checked this round (literature
scope only). The core converse under arbitrary dictionary overlaps remains
open. Experience extraction: none; these are question-specific source and
model findings, not a reusable construction lemma.

## Next action

Try a direct construction using longer repeated vertex factors, with the
classical token-index EPM semantics and a first small-instance check of
the proposed cost gap.
