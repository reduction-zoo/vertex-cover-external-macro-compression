# Fixed question

```json
{
  "source": "Vertex Cover",
  "target": "External macro data compression",
  "category": "Construction open",
  "summary": "This reconstructs a rule for selecting reusable dictionary phrases under an explicit storage-cost model.",
  "source_definition": "Given a finite simple graph and k, return a vertex cover of size at most k, or NO-SOLUTION. All finite combinatorial structures are explicit and numerical data use binary encoding.",
  "target_definition": "Given a finite string s, pointer cost h and budget B, return a dictionary D and compressed string C composed of literals and pointers to substrings of D. Recursive replacement must terminate and expand C to s. Count every literal as one unit and every pointer occurrence as h units across both D and C; require total cost at most B. Encode pointer destinations and substring endpoints explicitly.",
  "required_result": "Construct deterministic polynomial-time maps F and G. F must produce a legal target instance, and G(x,y) must return a valid source output for every valid target output y, including NO-SOLUTION. A complete rule may reconstruct a published construction or give a new one; it must specify every gadget, numerical parameter and decoding step.",
  "acceptance": "Deliver executable instance construction and output recovery, a general proof covering all legal inputs and target outputs, and worst-case polynomial time and encoding-size bounds. Cite the actual proof used, or identify a newly derived argument. Check small positive and negative instances with independent solvers; finite tests alone do not establish correctness.",
  "importance": "This reconstructs a rule for selecting reusable dictionary phrases under an explicit storage-cost model.",
  "difficulty": "Difficulty is not yet established by a construction attempt. All legal pointer sharing and dictionary overlaps must be covered by the converse. Pointer cost and recursive expansion semantics cannot remain implicit.",
  "openness": "The cited source points to Storer and Storer-Szymanski compression results. Recovering their precise construction and compatible pointer conventions is part of the task, rather than a new claim of compression hardness.",
  "literature_checked": "2026-09-18",
  "coverage": "Import inventory review of the cited sources. Primary proofs have not been independently re-audited; availability of a complete reconstruction elsewhere remains unassessed.",
  "references": [
    {
      "title": "Problem-Reductions: Vertex Cover \u2192 External macro data compression",
      "url": "https://github.com/CodingThrust/problem-reductions/issues/455",
      "note": "Upstream issue and review discussion checked on 2026-09-18. Its references are reconstruction leads, not independently audited proof sources."
    }
  ],
  "solutions": [],
  "equation": ""
}
```
