# Campaign state

Budget: 20 rounds. Used: 5.
Board source: 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17.

Capability probe, 2026-09-25: Python 3.12.14 at
`/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at
`/Users/xiweipan/.local/bin/uv`; Z3 executable 5.1.0 at
`/opt/homebrew/bin/z3`, Python binding z3-solver 5.1.0.0 locked in uv;
Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; Typst 0.15.1 at
`/opt/homebrew/bin/typst`; Lean 4.34.1 and Lake 5.0.0 at
`/opt/homebrew/bin`; no campaign Mathlib checkout; writing skill available.
Prepare: 120 fixed cases, self-test passed; see [preparation](work/preparation.md).
Next action: round 006, recover the 1977 proof from an archive or mirror;
if unavailable, assess remaining testable mechanisms.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Primary-source EPM model audit | Locate compatible full VC construction | Token-index semantics supported; full proof unavailable; upstream sketch fails cost check | [round](rounds/001/round.md) |
| 002 | Direct repeated-factor grammar gadget | Can one dictionary expose all vertex factors? | Yes; concrete false YES for transferred threshold | [round](rounds/002/round.md) |
| 003 | Adjacent EPM literature and normal forms | Locate unrestricted theorem with converse | Matching theorem found, but proof deferred to inaccessible 1977 report | [round](rounds/003/round.md) |
| 004 | Repeated identical edge blocks | Does a whole-edge dictionary beat the cover threshold? | Yes; cost 13 versus threshold 16 for a NO instance | [round](rounds/004/round.md) |
| 005 | Long-delimiter one-copy edge gadget | Check cost gap and repeated factors | Dictionary adjacency gives false YES: cost 145 versus 149 | [round](rounds/005/round.md) |
