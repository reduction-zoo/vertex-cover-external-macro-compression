# Arbitrary dictionary intervals collapse entry costs

## Claim and applicability

Tags: external macro compression, dictionary overlap, grammar transfer.
When a reduction charges separately for named dictionary rules, transferring
the same threshold to EPM with arbitrary substring pointers can fail:
concatenating phrases may expose all desired overlapping factors without
paying a separate entry cost. This observation applies to that transfer,
not to every EPM construction.

## Evidence and status

The [round 002 counterexample](../../campaigns/vertex-cover-external-macro-compression/rounds/002/round.md)
gives a `k=0` graph with a valid EPM cost 27 below the transferred grammar
threshold 33. It is a checked concrete counterexample, not a general
impossibility theorem. No independent review yet.

## Consequence for search

Count every substring made available by a proposed dictionary, including
cross-entry overlaps, before asserting a vertex selection cost. A new
construction needs a converse that allows arbitrary intervals.

## Use history

- 2026-09-25, originating round 002: excluded the direct grammar threshold.
