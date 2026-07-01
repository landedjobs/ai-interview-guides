[← All guides](../README.md) · part of [ai-interview-guides](https://github.com/landedjobs/ai-interview-guides) by [Landed](https://landed.jobs)

<div align="center">

# <img src="https://unavatar.io/notion.so" width="30" align="top"> Notion AI Interview Guide (2026)

![Updated](https://img.shields.io/badge/updated-2026.07-00A86B?style=flat-square) ![Sources](https://img.shields.io/badge/sources-Glassdoor·Blind·Reddit·candidate_blogs-6C2BD9?style=flat-square)

**A 24-72 hour block-editor take-home that the pair-programming round then extends live, capped by OT-vs-CRDT system design and a ~23% pass rate.**

</div>

---

## Company AI Context (2026)

Notion is the collaborative documents/wiki + databases + AI surface; in 2026 the AI team rebuilds for agentic AI [87]. "Meet your AI team" page describes Custom Agents, AI that works where the team works, and the Notion Agent building, editing, and taking action [56]. AI Engineering Survey 2026 published by Notion discusses hiring, onboarding, knowledge transfer [18]. Most-hired roles per public Ashby: Software Engineer, New Grad (AI) [17]; Software Engineer, AI Workflows [20]; AI Applications Engineer [16]. HQ San Francisco; AI team distributed.

## Interview Process

Per [74], [70], [71]:

1. Recruiter screen.
2. Take-home: build a simplified block-based editor in ~24-72 hours - text/heading/list blocks, drag-and-drop, undo/redo [70].
3. Pair-programming: extend the take-home project to add nested blocks, toggle lists; 60 minutes [70].
4. Technical screen: CoderPad stubs, complete basic text-editor functionality [71].
5. System design: real-time collaboration (OT vs CRDT, websockets, conflict resolution) [70], database/index, schema, scaling, security [71].
6. Cross-functional: 45-minute session with a product member analyzing a user-reported perf issue (engineering + product lens) [70].
7. Behavioral + culture + top-management chats [71].

Total: 5 rounds over ~5 weeks for new grads [70]. Pass rate ~23% of engineers [74].

## Real Questions & Exercises

Take-home [70]:

> "Build a simplified block-based editor with text, heading, and list blocks, featuring drag-and-drop reordering and undo/redo functionality." [70]

Pair-programming [70]:

> "Extend the take-home project together to add nested blocks and toggle lists" in 60 minutes. [70]

Technical screen [71]:

> "Implement basic text editor functionality by completing pre-stubbed functions in CoderPad." [71]

Functional implementation round [71]:

> "Implement a specific functional requirement, emphasizing clean code and data structure selection." [71]

System design [70]; [71]:

> "Discussion on Operational Transformation vs Conflict-free Replicated Data Types, websockets, conflict resolution for concurrent edits." [70]

> "Deep dives into database schema, indexes, efficient SQL queries, scaling strategies, data security." [71]

Cross-functional [70]:

> "Users complain about slow performance on large pages - diagnose and propose solutions from both engineering and product angles." [70]

Behavioral [70]; [71]:

> "Why Notion?" [70][71]

> "Tell me about a project you are proud of." [70][71]

> "How do you handle changing requirements?" [70][71]

> "Tell me about a time..." (standard behavioral probing). [70][71]

Evaluation criteria reported: state management, component design, code organization [70]; problem-solving, communication, product understanding [71].

Glassdoor meta: stages described as Phone interview 35%, Skills test 23%, One-on-one 19%, Background check 12% [72].

## Technical Topics to Master

- Block-based editor architecture: data model, render pipeline, drag-and-drop, undo/redo [70].
- Real-time collaboration: OT vs CRDT vs hybrid (Yjs, Automerge), websocket fan-out, conflict resolution [70]; [87].
- Postgres / sharded block model at 200B blocks [89].
- AI features: agent orchestration, retrieval, prompt format design [56]; [58].
- Engineering hygiene: state management, component design, code organization [70].
- Database/index/SQL scaling [71].

## Product Sense & Practical Rounds

Two-pronged practical rounds. Worked examples:

1. **Take-home (24-72h)**: ship a block editor with text/heading/list, drag-and-drop reorder in O(n), command-stack undo/redo with a clean reducer pattern, and 80%+ test coverage on reducer + DnD. Document the data model (single tree with stable IDs) vs an alternative matrix-of-cells early in the README so the pair-programming debrief has a shared vocabulary [70].
2. **Cross-functional performance triage** [70]: split your answer into "what we measure now (TTI, INP, doc-size fan-out cost)," "where the cost is (render fan-out for big pages)," and "product surface to fix (lazy-load block chunks, virtualization, AI summarization shim before render)."
3. **OT-vs-CRDT system design** [70]: articulate, with concrete examples, why Notion's page-level CRUD hybrid avoided OT and chose CRDT-like semantics for shared cursors.

## Behavioral & Culture

- Founded by Ivan Zhao; strong craft values and an explicit "meet your AI team" framing [56].
- In-office requirements vary by team; interview coder report cites culture-fit interviews toward the final stages [71].
- Mission: "To scale agentic AI" via a wholly rebuilt stack [87].

## Compensation (2026)

Per [92]:

| Level | Base | Stock | Bonus | TC |
|---|---|---|---|---|
| L1 | $143K | $51.8K | $0.8K | $196K |
| L2 | $179K | $163K | $1.3K | $344K |
| L3 | $189K | $157K | $0.4K | $346K |
| L4 | $258K | $390K | $1.5K | $649K |
| L5 | - | - | - | up to $776K |

- Vesting: 25% year 1, then 2.08% monthly years 2-4 [92].
- 10-year post-termination exercise window - among the most generous in this group [92].
- Highest reported TC $777,500 [92].

## What Gets People Rejected

- Take-home that doesn't reach the 4-of-5 quality bar or skips the data-model README that anchors the pair-programming round [70].
- Inability to articulate the cross-functional diagnosis on the perf-on-large-pages scenario [70].
- Vague system design without OT/CRDT specifics, websocket fan-out numerics, or schema/ACL choices.
- Behavioral answers that don't surface personal craft (Notion is craft-driven; bring receipts on a project you polished yourself).

## Insider Tips

- Pre-build a block-editor prototype in your strongest stack (Typescript + React, or Rust + egui) so the take-home is incremental, not from zero [70].
- Read the VentureBeat "tore down its tech stack" piece before your system design round; it explicitly describes the agentic rebuild [87].
- For the cross-functional perf round, prepare one perf issue you shipped to all four quadrants: input cause, observation metric, shipping mitigation, customer impact in dollars.

## Sources

- [16] [Careers at Notion](https://www.notion.com/careers)
- [17] [Software Engineer, New Grad (AI) @ Notion - Ashby](https://jobs.ashbyhq.com/notion/7e6dc7fe-7ddd-42c1-8928-13f7bddb9ec9)
- [18] [2026 AI Engineering Survey - Notion](https://www.notion.com/lp/ai-engineering-survey)
- [20] [Software Engineer, AI Workflows - Notion (Built In NYC)](https://www.builtinnyc.com/job/software-engineer-ai-workflows/8985481)
- [56] [Meet your AI team - Notion](https://www.notion.com/product/ai)
- [58] [Lessons from Notion: How to build a great AI product - Statsig](https://www.statsig.com/blog/notion-how-to-build-an-ai-product)
- [70] [Interviewed at Notion for New Grad SWE, here's everything - Reddit](https://www.reddit.com/r/InterviewCoderHQ/comments/1r32gip/interviewed_at_notion_for_new_grad_swe_heres/)
- [71] [How I Passed My 2026 Notion Software Engineer Interview - LinkJob](https://www.linkjob.ai/interview-questions/notion-software-engineer-interview-questions/)
- [72] [Notion Labs Software Engineer interview questions - Glassdoor](https://www.glassdoor.com/Interview/Notion-Labs-Software-Engineer-Interview-Questions-EI_IE3304926.0,11_KO12,29.htm)
- [74] [Notion Interview Experiences (2026) - Taro](https://www.jointaro.com/interviews/companies/notion/?tab=experiences)
- [87] [To scale agentic AI, Notion tore down its tech stack - VentureBeat](https://venturebeat.com/technology/to-scale-agentic-ai-notion-tore-down-its-tech-stack-and-started-fresh)
- [89] [The Tech Stack Behind Notion: Building a Block-Based Editor - TechAhead](https://www.techaheadcorp.com/blog/tech-stack-powering-notion-block-based-editor/)
- [92] [Notion Software Engineer Salary - Levels.fyi](https://www.levels.fyi/companies/notion/salaries/software-engineer)

---

<div align="center">

**Prepping for Notion? [Landed](https://landed.jobs) preps you with courses and voice mock interviews, matches you fresh AI roles daily, and drafts your application answers.**

[![Get Started](https://img.shields.io/badge/Get%20Started%20Free-→-6C2BD9?style=for-the-badge)](https://landed.jobs)

<sub>Compiled from public candidate reports — processes change; verify against the official careers page. Interviewed here recently? PRs welcome. · [All guides →](../README.md)</sub>

</div>
