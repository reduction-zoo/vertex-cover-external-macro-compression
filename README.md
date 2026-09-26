# Vertex Cover → External macro data compression

**Status:** `stopped_without_discovery` · **Research model:** `gpt-6-sol` (confirmed from the research session's turn context) · **Research ended:** 2026-09-25

Independent research campaign. Stopped without a reduction after seven
attempts (13 of 20 rounds remain). Three gadget families have checked
false-YES counterexamples under arbitrary dictionary pointers; no
executable F/G or general proof is claimed.

[State](campaigns/vertex-cover-external-macro-compression/state.md) · [Question](campaigns/vertex-cover-external-macro-compression/question.md)

The [prepared corpus](campaigns/vertex-cover-external-macro-compression/work/preparation.md)
contains 120 independently labeled Vertex Cover inputs and a bounded
finite target oracle. The [round records](campaigns/vertex-cover-external-macro-compression/rounds/)
preserve literature findings and counterexamples. Reproduce with
`uv sync --locked` and
`uv run python campaigns/vertex-cover-external-macro-compression/work/check.py --self-test`;
run `uv run python campaigns/vertex-cover-external-macro-compression/rounds/002/probe.py`,
and similarly for rounds 004 and 005, to reconstruct the counterexamples.

Board source commit: 6c7d3bd9c0a8f595279969a9c0a4d1853a3f5c17.
