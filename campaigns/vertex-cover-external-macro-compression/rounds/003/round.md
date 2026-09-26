# Round 003 — adjacent literature for unrestricted EPM normal forms

## Plan

Gap: round 002 shows that grammar rule costs do not survive arbitrary EPM
dictionary intervals. Mechanism: standalone literature investigation of
later primary papers that state EPM hardness or normalize arbitrary
overlapping dictionaries, beyond the original sources scoped in round 001.
First discriminating check: locate an explicit theorem whose converse
handles arbitrary overlapping pointers under the one-literal/`h`-pointer
cost model, and inspect its actual construction and proof. If found,
attempt to adapt its extraction to this campaign; otherwise record the
coverage gap. Scope: directly relevant EPM hardness papers and their
primary references, not grammar hardness alone.

## Evidence and diagnosis

The indexed text of [Storer and Szymanski, JACM 1982, Theorem 2](https://doi.org/10.1145/322344.322346)
states NP-completeness of minimum EPM compression with both recursion and
overlapping permitted (case (a)), with fixed integer pointer size greater
than one. It also covers three restricted combinations. The paper explicitly
defers *all* theorem proofs to Storer's 1977 report. Thus the theorem is
compatible with the target's freedom, but it supplies no executable
construction or solution recovery in the accessible text.

[Casel et al. §2.4, footnote 8](https://link.springer.com/article/10.1007/s00224-020-10013-w)
points to `http://www.informatik.uni-trier.de/~fernau/Sto77.pdf` as a full
copy of the report. Both HTTPS and HTTP downloads failed in this session
(SSL error and HTTP 502, respectively); browser access also failed.
Searches for the report by title and filename found citations, not another
accessible full copy. A secondary thesis [Nevill-Manning, chapter 6](https://paperzz.com/doc/9247425/inferring-sequential-structure)
sketches a different node-name/delimiter construction but explicitly sends
readers to Storer 1977 for the full proof. It is a lead, not proof evidence.

First check outcome: a matching theorem exists; its converse and parameters
remain unavailable. No target instances or recovery outputs were checked
this round (literature scope only). Experience extraction: none; the source
location and access problem are campaign-specific.

## Next action

Reconstruct and test the node-name/delimiter mechanism indicated by the
secondary account, keeping all unsupported cost equalities explicit.
