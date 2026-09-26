# Campaign state

Budget: 20 rounds. Used: 2.
Board source: 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17.

Capability probe, 2026-09-25: Python 3.12.14 at
`/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at
`/Users/xiweipan/.local/bin/uv`; Z3 executable 5.1.0 at
`/opt/homebrew/bin/z3`, Python binding z3-solver 5.1.0.0 locked in uv;
Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; Typst 0.15.1 at
`/opt/homebrew/bin/typst`; Lean 4.34.1 and Lake 5.0.0 at
`/opt/homebrew/bin`; no campaign Mathlib checkout; writing skill available.
Prepare: 120 fixed cases, self-test passed; see [preparation](work/preparation.md).
Next action: round 003, find a mechanism robust to arbitrary dictionary
intervals or a valid normal-form theorem.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Primary-source EPM model audit | Locate compatible full VC construction | Token-index semantics supported; full proof unavailable; upstream sketch fails cost check | [round](rounds/001/round.md) |
| 002 | Direct repeated-factor grammar gadget | Can one dictionary expose all vertex factors? | Yes; concrete false YES for transferred threshold | [round](rounds/002/round.md) |
