# Executable contract used by Prepare

Source JSON is `{ "n": N, "edges": [[u,v], ...], "k": K }`: integers
`N,K >= 0`, vertices `0..N-1`, and sorted distinct pairs `0 <= u < v < N`.
An output is `{"cover": [vertices...]}` with distinct in-range vertices,
at most `K` of them, covering every edge, or the string `"NO-SOLUTION"`
exactly when no such cover exists.

Target JSON is `{ "s": "...", "h": H, "B": B }`, with a finite string,
positive integer pointer cost `H`, and nonnegative integer budget `B`.
For the finite oracle, target output is `"NO-SOLUTION"` or
`{"D": [tokens...], "C": [tokens...]}`. A token is `{"lit":"c"}`
or `{"ptr":[lo,hi]}`. Endpoints are zero-based, half-open **token**
indices in `D`. Every dictionary token is recursively expanded; a cycle is
invalid. Expanding `C` must equal `s`; all literals cost one and all pointer
occurrences cost `H` in both arrays. The corpus uses ASCII; the interface
permits Unicode code points as literals.

The fixed question does not specify whether pointer endpoints index raw
dictionary tokens or positions in its expanded string. This finite oracle
chooses token indices. A full reduction must resolve the semantics before
claiming correctness for the question as written.

`algorithm.py` reads one source JSON from stdin and prints one target JSON.
`algorithm.py --extract` reads `{"source": source,
"target_solution": output}` and prints one source output. Both are fresh
processes; diagnostics go to stderr and errors exit nonzero.
