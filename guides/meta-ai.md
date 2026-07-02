[← All guides](../README.md) · part of [ai-interview-guides](https://github.com/landedjobs/ai-interview-guides) by [Landed](https://landed.jobs)

<div align="center">

# <img src="https://static.b100x.ai/github-repos/images/logos/meta.com.png" width="30" align="top"> Meta AI Interview Guide (2026)

![Updated](https://img.shields.io/badge/updated-2026.07-00A86B?style=flat-square) ![Sources](https://img.shields.io/badge/sources-Glassdoor·Blind·Reddit·candidate_blogs-6C2BD9?style=flat-square)

**The only frontier lab that runs two dedicated ML system design rounds in one loop, and the 2026 bar is tighter than the 2025 hiring-spree era after the October FAIR cuts.**

</div>

---

## 1. Company AI Context (2026)

Meta is rebuilding its AI org: Llama line (Llama 3, 4, Behemoth-scale), GenAI product org (Meta AI in WhatsApp/Instagram/in-the-app), and AI infra (training clusters + Helix-style platform). After the 2025 hiring spree ($100M+ offers reported), Meta **cut ~600 AI roles in FAIR in Oct 2025** and reorganized; some teams were absorbed into the GenAI product org ([15]).

Hires heavily across:

- **GenAI Product Group** (consumer Meta AI).
- **FAIR** (research; reduced but still active).
- **AI Infra** (training infra, inference, eval).

Role types (Meta Research Career page):

- **Research Engineer** ([11]).
- **Research Scientist** (PhD path).
- **AI Engineer** (E4-E6 ladder).
- **Applied AI Engineer**.
- **Forward-deployed** (newer): mostly inside Reality Labs and GenAI.

Hiring bar reputation: very high coding + deep ML system design (the "two ML system design rounds" in a 6-round RE loop ([13])).

## 2. Interview Process, Stage by Stage

| Stage | Format | Duration | Who | Evaluated |
|---|---|---|---|---|
| Recruiter screen | Phone | 30 min | Recruiter | Background, motivation |
| Phone screen #1 | Coderpad | 45-60 min | Engineer | Coding (medium/hard) |
| ML system design #1 | Virtual | 60 min | Senior RE or manager | Practical ML infra design |
| ML system design #2 | Virtual | 60 min | Senior RE or manager | Training/inference design |
| AI coding | Virtual | 60 min | Engineer | Frontier ML coding problem |
| Standard coding | Virtual | 60 min | Engineer | LeetCode-hard |
| Hiring manager | Virtual | 45-60 min | HM | Team-fit, motivation |
| Decision | Committee + offer | 1-2 weeks | -- | -- |

Sources: [12]; [13].

**Track differences:**

- **Research Engineer**: 6 rounds (per candidate report); 2 ML system design + 1 AI coding + 1 coding + 1 phone + HM.
- **Research Scientist**: paper discussion + ML coding + ML systems.
- **AI Engineer**: standard coding + system design + AI coding.
- **Forward-deployed**: more product/business-case mix.

**Reported timeline**: 2-3 months total per IGotAnOffer; Meta is known for ~5 rounds + HM across many tracks.

## 3. Real Interview Questions (Reported 2024-2026)

**ML system design**

> 1. "Design a system that does continual pre-training on new corpora without catastrophic forgetting" (candidate report [12])
> 2. "Design a recommendation system for video content" (candidate anecdote on [13])
> 3. "Design a scalable RLHF infra for a chat model with continuous improvement from real traffic" (candidate report)
> 4. "Design a distributed inference serving for a 100M-user chat traffic" (candidate report)
> 5. "Design an eval framework for multi-turn dialogue that captures safety regressions" (candidate report)
> 6. "Design an LLM agent loop with safety guardrails" (candidate report, Meta RE)

**Coding**

> 7. "Implement FSDP-style sharded training in PyTorch" (candidate report)
> 8. "Standard LeetCode-hard LRUs, merge intervals, but more applied to feature ingestion" (candidate report)
> 9. "Reverse a transformer block - identify what's wrong" (candidate anecdote)
> 10. "Implement a top-k logits in batched form" (candidate report)

**Behavioral**

> 11. "Tell me about a time you shipped ML infra under deadline" (candidate report)
> 12. "Why Meta over OpenAI?" (common, [13])
> 13. "How do you handle model failure modes in production?" (candidate report)
> 14. "Walk me through a recent AI product launch you disagreed with" (candidate anecdote)
> 15. "Describe your role in a recent research paper" (paper discussion variant)

## 4. Technical Topics to Master

- **PyTorch**; C++ for low-level inference; systems-level knowledge (KV cache, batching).
- **ML systems**: distributed training (FSDP, ZeRO, Megatron-LM-style tensor parallel), inference optimization.
- **Recommendation systems**: candidate report mentions "ranking/relevance" for Ads+Search paths; good extra credit ([13]).
- **Coding language**: Python + PyTorch for ML rounds; standard-language mixed for coding rounds.
- **AI-assisted coding policy**: not explicitly stated (candidate anecdotes vary).

**Recommendation:** The ML system design round is the single most important to rehearse; Meta RE candidates consistently report "two ML SD rounds in one loop" and this is unique among the 6 labs.

## 5. System Design Themes

**(a) RLHF continual learning.** Strong answer: periodic freeze + replay buffer + KL-anchored regularization; on-policy vs off-policy tradeoffs; reward model versioning; eval shift detection; under-spec: lifetime safety preservation.

**(b) Distributed inference for 100M-DAU.** Strong answer: prefill/decode split, prefix-cache sharing, paged KV, COP (continuous online prediction) for personalization; tiered rate limit; observability + log-likelihood tracing.

**(c) Multi-turn eval framework.** Strong answer: offline + online + human pairwise + adversarial red-team eval; sampling rates by traffic tier; AB-test gating; canary rollout; reward model watching for subtle regressions.

## 6. Behavioral / Values Fit

Meta values:

- "Move fast": shipping velocity over perfect ([11]).
- Open-source orientation (Llama, fairseq, FAISS).
- Direct, low-ego feedback culture.

**Prepare 2-3 "rapid shipping under uncertainty" stories.**

## 7. Compensation (2026)

| Level | Base | Stock | Bonus | Total ~TC |
|---|---|---|---|---|
| E3 (Junior AI Eng) | ~$165K | ~$120K | low | $300K |
| E4 (AI Eng) | ~$185K | ~$165K | low | **$359K** |
| E5 (Senior AI Eng) | ~$220K | ~$260K | some | $480-550K |
| E6 (Staff AI Eng) | ~$270K | ~$370K | some | **$645K** |
| E7 (Principal) | $300K-$400K+ | very heavy | some | $1M-$1.5M+ |

Sources: [59]; [57]; [58].

**Outlier offers**: widely reported $100M+ AI talent offers; one reported $250M for a single researcher ([15]; [60]). The validity of the $250M figure is not independently corroborated; treat as candidate anecdote.

**Important context**: despite the headline offers, Meta cut ~600 AI roles in Oct 2025 ([15]). The 2026 process is more selective than the 2025 cycle.

## 8. What Gets People Rejected

- Inability to articulate a system-design end-to-end with a clear testable boundary ([12]).
- Weak standard-coding under pressure (Meta's coding bar is "FAANG hard").
- Over-indexing on research novelty; under-indexing on shipping.
- Reactive only vs proactive problem framing.

## 9. Insider Tips

- Treat every ML SD question as a *trade-off* exercise; show your workbench of constraints ([13]).
- Re-read a Meta AI paper (Llama 4, Segment Anything, ROBLE) and speak about its trade-offs specifically.
- The Oct 2025 FAIR restructuring changed team-matching timing; expect it earlier in 2026 ([15]).
- Practice "specific moment in time" stories for behavioral rounds.

## Sources

11. *Research Career & Job Openings - Meta*. https://www.metacareers.com/careerprograms/research/
12. *Meta Research Engineer Interview (6 Rounds) - ML*. https://www.reddit.com/r/OfferEngineering/comments/1sx5hja/meta_research_engineer_interview_6_rounds_ml/
13. *Meta Research Engineer Interview (questions, process, prep) - IGotAnOffer*. https://igotanoffer.com/en/advice/meta-research-engineer-interview-guide
15. *Meta slashes FAIR Research Lab after AI hiring spree*. https://www.rdworldonline.com/meta-cuts-600-ai-roles-months-after-reports-of-100m-offers-to-top-recruits/
57. *Meta Salaries | Levels.fyi*. https://www.levels.fyi/companies/meta/salaries
58. *AI Compensation Benchmarks 2026: The AI Hiring Bubble - Pin*. https://www.pin.com/blog/ai-compensation-salary-guide/
59. *Meta AI Engineer Salary | $359K-$645K+ | Levels.fyi*. https://www.levels.fyi/companies/meta/salaries/software-engineer/title/ai-engineer
60. *Meta offers $250m to young AI researcher*. https://www.facebook.com/groups/698593531630485/posts/1352611646228667/

---

<div align="center">

**Prepping for Meta AI? [Landed](https://landed.jobs) preps you with courses and voice mock interviews, matches you fresh AI roles daily, and drafts your application answers.**

[![Get Started](https://img.shields.io/badge/Get%20Started%20Free-→-6C2BD9?style=for-the-badge)](https://landed.jobs)

<sub>Compiled from public candidate reports — processes change; verify against the official careers page. Interviewed here recently? PRs welcome. · [All guides →](../README.md)</sub>

</div>
