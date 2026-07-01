[← All guides](../README.md) · part of [ai-interview-guides](https://github.com/landedjobs/ai-interview-guides) by [Landed](https://landed.jobs)

<div align="center">

# <img src="https://unavatar.io/deepmind.google" width="30" align="top"> Google DeepMind AI Interview Guide (2026)

![Updated](https://img.shields.io/badge/updated-2026.07-00A86B?style=flat-square) ![Sources](https://img.shields.io/badge/sources-Glassdoor·Blind·Reddit·candidate_blogs-6C2BD9?style=flat-square)

**The most research-flavored loop of the six frontier labs: paper discussions, math and theory rounds, banned AI tools, and a hiring committee that can take 2-4 weeks after your final interview.**

</div>

---

## 1. Company AI Context (2026)

DeepMind is the AI research arm of Alphabet, combining the original DeepMind with Google Brain. Develops Gemini family, Veo (video), AlphaFold, robotics (RT-2 / RT-X), AI safety, and theoretical ML. ~7,000-person org across London, Mountain View, Zurich, Paris, Tokyo ([2]).

**Confirmed hiring teams** (DeepMind Careers page):

- **Research Scientist**: standalone research, publications expected.
- **Research Engineer**: bridges research and engineering (training infra, distributed systems).
- **Software Engineer**: standard SWE roles.
- **Applied AI**: deployment, product integration, protos.

Hiring bar reputation: DeepMind is widely considered the most prestigious AI lab ([2]). Exponent and JobsByCulture note it is heavy on theory, math, and paper discussion.

## 2. Interview Process, Stage by Stage

| Stage | Format | Duration | Who | Evaluated |
|---|---|---|---|---|
| Recruiter screen | Phone | 30 min | Recruiter | Background, publications, motivation |
| Hiring manager chat | Phone | 45 min | HM | Projects, alignment with team's research agenda |
| Technical phone screen (1-2) | Virtual | 60 min each | Engineer or scientist | Coding or ML coding depending on track |
| Virtual onsite loop | 4-5 rounds | 60 min each | Cross-team Eng / Sci | Coding, ML coding, paper, math/theory, behavioral |
| Hiring committee review | Internal | 2-4 weeks | Committee | Bar calibration |
| Offer | Written | 2-4 weeks total | -- | -- |

Sources: [3]; [2]; [4]; [1].

**Track-specific variation** (per techinterview, May 2026):

- **Research Scientist**: 60 min paper discussion + 60 min research problem framing + 60 min ML coding + 60 min math/theory + 45 min behavioral.
- **Research Engineer**: ML coding + distributed training (tensor parallelism, ZeRO) + eval infrastructure (test contamination awareness) + standard coding + behavioral.
- **Software Engineer**: 2 coding + 1 system design + 1 domain depth + 1 behavioral.
- **Applied AI**: similar to RE but tilted to deployment.

**Reported timelines**: 6-10 weeks per JobsByCulture; total committee + offer can reach 8-12 weeks.

## 3. Real Interview Questions (Reported 2024-2026)

**Math / theory**

> 1. "Derive the optimal Bayesian posterior for a Gaussian likelihood with Gaussian prior and compute the marginal likelihood analytically" (candidate anecdote on techinterview [3])
> 2. "Implement attention with masking and KV caching" (techinterview RE track)
> 3. "Prove the convergence rate of SGD on a strongly convex objective" (techinterview RS track)
> 4. "Compute the gradient of a custom loss where you have two coupled models" (techinterview)
> 5. "Implement a transformer from scratch with PyTorch" (traditional DeepMind historian question [31])

**Coding**

> 6. LeetCode-medium level (LinkedList/BST/graph) plus an ML twist (candidate anecdote, Reddit r/csMajors DeepMind, recent)
> 7. "Reverse a linked list in-place with custom memory constraints" (candidate anecdote, sundeep teki blog)

**Paper discussion**

> 8. "Discuss a paper you chose; bring a list of strengths, weaknesses, future directions" ([33])
> 9. "Be prepared to defend the choice of baseline in a paper you admire" ([33])
> 10. "Tell me about a limitation in the Flash Attention paper and how you'd address it in v3" (candidate report referenced in dataford guide)

**System design / ML (Gemini team)**

> 11. "Design a distributed training system for a 500B-parameter model" (candidate anecdote [38])
> 12. "Design a training data deduplication + decontamination pipeline" (candidate anecdote)
> 13. "Design a multimodal eval harness" (candidate report)
> 14. "How would you address test-set contamination at training?" (candidate report, dataford)
> 15. "Design an RLHF post-training pipeline" (Gemini) (candidate report)

**Behavioral**

> 16. "Tell me about a research disagreement you resolved" ([3])
> 17. "Why DeepMind over Google research / OpenAI?" ([4])
> 18. "Describe a tough feedback you gave someone more senior" (candidate anecdote)

## 4. Technical Topics to Master

- **PyTorch + DeepMind's JAX/Flax** idioms; transformer internals; attention variants; deep learning theory.
- **Math**: linear algebra, probability, Bayesian inference, gradient-flow analysis, optimization theory ([3]).
- **Distributed training**: tensor parallelism, ZeRO, FSDP, pipeline parallelism, gradient compression ([3]).
- **Eval infrastructure**: contamination, leakage, robustness ([3]).
- **Coding language**: Python; some teams expect C++ for systems-track RE.
- **AI-assisted coding policy**: "AI tools such as ChatGPT or Copilot are prohibited or heavily limited during technical rounds" ([3]).

**Recommendation:** Build a paper-reading habit; the paper-discussion round is unique to DeepMind.

## 5. System Design Themes

**(a) Distributed training for a 500B model.** Strong answer: data / tensor / pipeline parallelism combo (5D parallelism), activation/gradient checkpointing, FSDP + ZeRO-3, async checkpoint streams; fault tolerance (NVIDIA/Magnum); gradient compression; placement-aware scheduling; queued preemption on transient pod loss; observability.

**(b) Eval harness with contamination control.** Strong answer: deterministic split-by-source; near-duplicate + n-gram overlap with held-out benchmarks; sacred set policies; canonicalization; continual re-eval on each checkpoint; human-eval sampler with calibration; adversarial red-team piloting.

**(c) RLHF post-training pipeline.** Strong answer: SFT -> RM training with pairwise comparisons + Bradley-Terry -> PPO with KL penalty + value model + clipping -> DPO/IPO alternative; reward hacking detection; safety reward blend; multi-reward Pareto.

## 6. Behavioral / Values Fit

Behavioral round happens in most loops ([3]). DeepMind screens for:

- Research taste (novel problem framing).
- Cross-team collaboration (bridge between research and infra).
- Genuine interest in scientific discovery, not just shipping ([4]).

## 7. Compensation (2026)

| Level | Base | Equity | Total ~TC |
|---|---|---|---|
| L3 (Junior SWE) | ~$160K | ~$35K | $205K |
| L4 (SWE) | ~$190K | ~$90K | $280-360K |
| L5 (Senior SWE) | ~$220K | ~$255K | **$475-625K** |
| L6 (Staff SWE) | ~$280K | ~$445K | **$725-950K** |
| L7 (Principal) | ~$330K | ~$620K | **$950K-1.4M** |

Research Scientist: L3-L8 in the range $178K-$893K ([83]).

Sources: [84]; [82]; [86].

**Outlier offers**: deep AI talent occasionally receives large sign-on, explicit "front-loaded" Alphabet RSUs ([3]).

## 8. What Gets People Rejected

- Weak ML coding (can't implement attention).
- Theory gaps (can't recall bias/variance trade-off in a Bayesian frame).
- Inability to discuss a paper critically.
- Slow decision after the loop ends ([2]: committee review 2-4 weeks).
- "Self-sabotage" pattern (similar to OpenAI); candidate anecdotes ([64]).

## 9. Insider Tips

- Bring a paper you're willing to defend to extremes; expect 60-min discussion ([33]).
- Train unaided ML coding; AI tools are prohibited ([3]).
- Past student researcher FAQ thread on r/csMajors ([5]) shows DeepMind's "Team Matching" happens after an initial screen; candidates should ask about team preferences early.
- Know the AI-coding policy by heart: "if your interview involves any tooling that lets you paste from GPT, expect disqualification" ([3]).

## Sources

1. *Careers at Google DeepMind*. https://deepmind.google/careers/
2. *Google DeepMind Interview Prep 2026 - JobsByCulture*. https://jobsbyculture.com/blog/deepmind-interview-prep-2026
3. *Google DeepMind Interview Process 2026 - techinterview*. https://www.techinterview.org/post/3233474918/deepmind-interview-process-2026/
4. *Google DeepMind Research Scientist Interview Questions - Dataford*. https://dataford.io/interview-guides/google-deepmind/research-scientist
5. *Google DeepMind student researcher position 2026*. https://www.reddit.com/r/csMajors/comments/1qlvxs1/google_deepmind_student_researcher_position_2026/
31. *[D] Google DeepMind Research Engineer/Scientist*. https://www.reddit.com/r/MachineLearning/comments/1q2wiub/d_google_deepmind_research_engineerscientist/
33. *AI Research Engineer Interview Guide: OpenAI, Anthropic, Google DeepMind - Sundeep Teki*. https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs
38. *[D] Preparing for a DeepMind Gemini Team Interview*. https://www.reddit.com/r/MachineLearning/comments/1k8gy12/d_preparing_for_a_deepmind_gemini_team_interview/
64. *Self-sabotage at OpenAI interview : r/leetcode*. https://www.reddit.com/r/leetcode/comments/1j8x3og/selfsabotage_at_openai_interview/
82. *Google Software Engineer Salary | $205K-$1.79M+ | Levels.fyi*. https://www.levels.fyi/companies/google/salaries/software-engineer
83. *Google Research Scientist Salary | $178K-$893K+ | Levels.fyi*. https://www.levels.fyi/companies/google/salaries/software-engineer/title/research-scientist
84. *Google DeepMind Salary (2026): Research Scientist, RE - ctaio.dev*. https://ctaio.dev/en/salary/google-deepmind-salary/
86. *Google Research Scientist Salary | Levels.fyi*. https://www.levels.fyi/companies/google/salaries/research-scientist

---

<div align="center">

**Prepping for Google DeepMind? [Landed](https://landed.jobs) preps you with courses and voice mock interviews, matches you fresh AI roles daily, and drafts your application answers.**

[![Get Started](https://img.shields.io/badge/Get%20Started%20Free-→-6C2BD9?style=for-the-badge)](https://landed.jobs)

<sub>Compiled from public candidate reports — processes change; verify against the official careers page. Interviewed here recently? PRs welcome. · [All guides →](../README.md)</sub>

</div>
