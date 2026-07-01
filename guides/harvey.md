[← All guides](../README.md) · part of [ai-interview-guides](https://github.com/landedjobs/ai-interview-guides) by [Landed](https://landed.jobs)

<div align="center">

# <img src="https://unavatar.io/harvey.ai" width="30" align="top"> Harvey AI Interview Guide (2026)

![Updated](https://img.shields.io/badge/updated-2026.07-00A86B?style=flat-square) ![Sources](https://img.shields.io/badge/sources-Glassdoor·Blind·Reddit·candidate_blogs-6C2BD9?style=flat-square)

**Heavy data-structure coding (R-trees, red-black rebalancing, min-cost flow) with running code expected, a reported ~20% pass rate, and a signature probe on whether you're interesting outside of work.**

</div>

---

## Company AI Context (2026)

Harvey builds vertical AI for legal and professional services - domain LLMs for contract analysis, due diligence, "Words to Workflow," Deep Research. Three-year anniversary post (Aug 4 2025) reports $100M+ ARR, 500+ customers in 54 countries, 42% of AmLaw 100 firms adopting, Weekly Active Users growing 4x year-over-year [2]. TrueUp profile gives more recent headcount 900 employees, $11B valuation, 317 open job postings [4]. Hiring hubs in San Francisco, New York, London, Sydney, Frankfurt, Bengaluru [2]. Most-hired roles: legal-domain LLM engineers, applied AI engineers, product engineers for "Workflows," forward-deployed customer engineers.

## Interview Process

Per [1]:

1. Recruiter outreach.
2. Coding technical screen.
3. Onsite (virtual) - coding, system design, behavioral; some candidates add a lunch with the team.

Reported candidate population: only ~20% of engineers who go through pass [1].

## Real Questions & Exercises

Coding [1]:

> "Implementing a rudimentary geospatial partitioning scheme using R-trees" [1] - tag: advanced data structure.

> "Variation on the minimum cost flow problem" [1] - tag: graph algorithms.

> "Code a file storage system to get/put via paths" [1] - tag: file systems / trees.

> A tree problem to "rebalance a red-black tree" where "running code is expected" [1] - tag: low-level implementation.

System design:

> "Design a car dealership management system" [1]

Behavioral:

> Interviewers probe whether candidates "excel at a hobby or are interesting outside of work" [1] - signature cultural probe.

(Compiled verbatim from candidate reports dated 2024-2026.)

## Technical Topics to Master

- Legal RAG accuracy: high-recall retrieval over long contracts, citation faithfulness, hallucination detection.
- Advanced data structures: R-trees, red-black trees, minimum cost flow [1].
- Graph algorithms (min-cost flow, bipartition) [1].
- File-system / path-resolution systems [1].
- Domain modeling for legal workflows: contracts, MDD, jurisdiction-aware LLMs.
- Python, LLM APIs, React, SQL, AWS [4].

## Product Sense & Practical Rounds

In the system-design round, strong answers treat legal-AI as a domain-critical accuracy product, not general chat:

1. "Design a car dealership management system" - add modules for provenance, audit log, jurisdiction-specific contract templates, retrieval with citation quality metrics, rollback for AI hallucinations in signed documents.
2. Offer a "legal-RAG accuracy" deep dive: corpus segmentation by jurisdiction, citation faithfulness metrics, hallucination triage workflow with senior-attorney feedback loop.
3. End with metric ownership: p50/p95 retrieval latency, citation accuracy held at >X% over a 10K-doc test set.

## Behavioral & Culture

- TrueUp shows 81% employees recommend; 90% CEO (Winston Weinberg) approval; Trajectory Score 99/100 [4].
- The "interesting outside of work" probe is a signature filter [1].
- Founders Gabe Pereyra + Winston Weinberg emphasize "transform how lawyers work" [2].

## Compensation (2026)

Per [90]:

| Level | Base | Stock | Bonus | TC |
|---|---|---|---|---|
| L3 | $197K | $186K | $7.7K | $390K |
| L4 | $216K | $106K | $5.8K | $328K |
| L5 | $250K | $133K | $7.4K | $390K |

- Median TC $375K, reported high $595K [90].
- Vesting: 25% year 1, 2.08% monthly thereafter [90].
- Valuation $11B, ~$1.2B total funding, $11.3B secondary mark [4].
- Equity illiquidity is the principal risk: prefer secondaries, model liquidity scenarios.

## What Gets People Rejected

- Inability to write code end-to-end in the coding round (R-trees, red-black rebalance, min-cost flow are heavy) [1].
- Generic system design without domain-AI accuracy metrics.
- No signal of "an interesting outside-of-work hobby" [1].
- Quiet pushback against intense hours baked into the founder-led workload.

## Insider Tips

- Prepare one legal-domain anecdote: "How I would source-verify a 100-page M&A contract" or "How I'd QA a multi-state discovery corpus."
- Practice four hard data-structure problems (R-tree, red-black tree, min-cost flow, path-based file system) under CoderPad timing.
- Cultivate a public "interesting outside of work" signal: open-source, writing side project, sport, art - the interviewer will literally probe it.

## Sources

- [1] [Harvey AI Interview Experiences (2026) - Taro](https://www.jointaro.com/interviews/companies/harvey-ai/?tab=experiences)
- [2] [Harvey's Three Year Anniversary](https://www.harvey.ai/blog/harveys-three-year-anniversary)
- [4] [Harvey - Company Profile - TrueUp](https://www.trueup.io/co/harvey-ai)
- [90] [Harvey Software Engineer Salary - Levels.fyi](https://www.levels.fyi/companies/harvey/salaries/software-engineer)

---

<div align="center">

**Prepping for Harvey? [Landed](https://landed.jobs) preps you with courses and voice mock interviews, matches you fresh AI roles daily, and drafts your application answers.**

[![Get Started](https://img.shields.io/badge/Get%20Started%20Free-→-6C2BD9?style=for-the-badge)](https://landed.jobs)

<sub>Compiled from public candidate reports — processes change; verify against the official careers page. Interviewed here recently? PRs welcome. · [All guides →](../README.md)</sub>

</div>
