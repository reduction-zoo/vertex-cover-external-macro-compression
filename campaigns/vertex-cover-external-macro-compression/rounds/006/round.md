# Round 006 — archival retrieval of Storer 1977 report

## Plan

Gap: the compatible 1982 theorem defers every proof to Storer's 1977
Technical Report 234. Mechanism: a finite archival search for the exact
report, focused on the URL cited by Casel et al., Internet Archive,
Princeton repositories and institutional mirrors. First discriminating
check: obtain and inspect a full PDF containing an unrestricted EPM
Vertex Cover reduction; otherwise document which locations were checked
and what remained inaccessible. Prior evidence: round 003 found the
report's cited URL but downloads failed. Scope ends after these archive
and institutional sources, without re-searching generic EPM literature.

## Evidence and diagnosis

The precise link printed in [Casel et al., footnote 8](https://link.springer.com/article/10.1007/s00224-020-10013-w)
still failed via HTTPS (TLS connection error) and HTTP (502). An
[Internet Archive CDX query](https://web.archive.org/cdx/search/cdx?url=www.informatik.uni-trier.de/~fernau/Sto77.pdf&output=json&filter=statuscode:200&collapse=urlkey)
returned no successful archived copy for that URL. Broader archive
query timed out and is not negative evidence. Searches of Princeton's
catalog/repository, the title, exact filename, and the 1978 STOC title
found bibliographic records and citations, not a full report or proof.
Storer's 1979 thesis is cataloged as a 199-page physical/reprint item,
but no accessible full text was found in this scope.

First check outcome: no full PDF was obtained. The unavailable report is
an evidence-access limitation, not proof that the construction cannot be
recovered. No target instances or recovery outputs were checked this
round. Experience extraction: none; this is a source-access fact tied
to this campaign.

## Next action

Inspect a broader recent dictionary-compression proof for an explicit
gadget that can withstand the dictionary-adjacency counterexample.
