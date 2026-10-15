# vertex-cover-external-macro-compression

Standalone formal definition of Q055. `record.json` preserves the exact
board source, target, requested result and equation used for this definition.
`Challenge.lean` imports only Mathlib. `Solution.lean` is its identical starting
copy, with the open theorem deliberately unproved.

## Modelling choices

Pointers use zero-based half-open token intervals in the encoded dictionary, following the classical EPM model described in Section 2.4 of https://link.springer.com/article/10.1007/s00224-020-10013-w . Overlaps and recursive pointers are allowed. An existential finite expansion depth expresses termination from the compressed code; unused dictionary cycles are not rejected, because only replacement of C must terminate in the board definition. Every pointer endpoint, including unused ones, must be in range. Literals are finite alphabet symbols represented by natural-number labels; their objective cost remains one even though their encoding takes binary bits. Both dictionary and code storage are charged. Empty words and empty substrings are admitted. SEMANTIC REVIEW: confirm the endpoint and empty-substring convention. The prepared validator additionally expands all dictionary tokens, and therefore rejects unused cycles accepted here; that extra restriction is not imposed by the board or the cited C-expansion semantics.

Finite indices are zero based. Numerical data use Q001's self-delimiting binary
encoding unless the source explicitly requires unary. `none` means no valid
witness exists; it never means a program error. Construction and recovery must
be deterministic polynomial-time TM2 computations with polynomial output bounds,
as in Q001. Recovery is universal over valid target outputs and receives the
original source instance as well. Legal-instance predicates are specifications,
not algorithms the proposed reduction must execute.

## Build and verification

Lean 4.35.0 and matching Mathlib are pinned by `lean-toolchain`, `lakefile.toml`
and `lake-manifest.json`. In this directory run:

```sh
lake exe cache get Mathlib.Computability.TuringMachine.Computable
LEAN_NUM_THREADS=2 lake build
lake env lean Audit.lean
./scripts/verify-comparator.sh
```

The comparator script and repository-root Linux CI follow the pinned Q001
reference. They run the bundled `lake comparator` with the strict axiom policy,
then, for an unfilled solution, require full statement agreement and rejection
only for `sorryAx`. Green CI verifies an open template, not a completed proof.
The script needs Linux and bubblewrap; macOS compilation is not comparator
verification. `Tests.lean` checks finite boundary examples, not general semantic
equivalence. Human review of the problem statement remains necessary.

## Provenance and license

Infrastructure follows Q001 at `6e5d9d7aa425db5f01ee44f4c4e1710cf2993fda`.
The files in this formal project are licensed under Apache-2.0; see `LICENSE`.
This does not change licensing of other files in the research repository.

Local verification results are recorded in `evidence/statement/verification.json`.
The comparator prerequisite test passes on macOS; its real Linux verdict cases
are skipped, and the comparator script itself exits at the missing `bwrap` prerequisite.
