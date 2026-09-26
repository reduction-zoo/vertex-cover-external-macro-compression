# Campaign state

Budget: 20 rounds. Used: 7. Remaining: 13.
Board source: 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17.
Research model: `gpt-6-sol`, confirmed from this campaign session's `turn_context`.

Capability probe, 2026-09-25: Python 3.12.14 at
`/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at
`/Users/xiweipan/.local/bin/uv`; Z3 executable 5.1.0 at
`/opt/homebrew/bin/z3`, Python binding z3-solver 5.1.0.0 locked in uv;
Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; Typst 0.15.1 at
`/opt/homebrew/bin/typst`; Lean 4.34.1 and Lake 5.0.0 at
`/opt/homebrew/bin`; no campaign Mathlib checkout; writing skill available.
Prepare: 120 fixed cases, self-test passed; see [preparation](work/preparation.md).
Status: `stopped_without_discovery` (evidence-backed early stop, 2026-09-25).
No F/G rule or general converse proof is claimed. Correctness: none for a
reduction; the Prepare corpus and three negative gadget witnesses pass
their stated checks. Novelty: no construction claimed. Significance:
one reusable warning about arbitrary dictionary intervals, not a hardness
result. Prospects within the remaining budget: low (uncalibrated), based
on three failed mechanisms, inaccessible deferred proof, and incompatible
adjacent normal forms. No independent review or paper is warranted without
a complete candidate.
Next action for a resumed campaign: obtain the full Storer 1977 proof or
derive an EPM charging lemma that survives arbitrary dictionary intervals.
Experience: one distinct entry created, updated once, pending promotion zero.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Primary-source EPM model audit | Locate compatible full VC construction | Token-index semantics supported; full proof unavailable; upstream sketch fails cost check | [round](rounds/001/round.md) |
| 002 | Direct repeated-factor grammar gadget | Can one dictionary expose all vertex factors? | Yes; concrete false YES for transferred threshold | [round](rounds/002/round.md) |
| 003 | Adjacent EPM literature and normal forms | Locate unrestricted theorem with converse | Matching theorem found, but proof deferred to inaccessible 1977 report | [round](rounds/003/round.md) |
| 004 | Repeated identical edge blocks | Does a whole-edge dictionary beat the cover threshold? | Yes; cost 13 versus threshold 16 for a NO instance | [round](rounds/004/round.md) |
| 005 | Long-delimiter one-copy edge gadget | Check cost gap and repeated factors | Dictionary adjacency gives false YES: cost 145 versus 149 | [round](rounds/005/round.md) |
| 006 | Archival retrieval of Storer 1977 | Find full unrestricted EPM proof | Report URL failed; no accessible archive found in finite scope | [round](rounds/006/round.md) |
| 007 | Later dictionary-compression proofs | Find transferable VC gadget with EPM converse | Related proof uses infinite phrase weights; no compatible normal form found | [round](rounds/007/round.md) |
