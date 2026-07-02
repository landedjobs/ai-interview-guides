[← All guides](../README.md) · part of [ai-interview-guides](https://github.com/landedjobs/ai-interview-guides) by [Landed](https://landed.jobs)

<div align="center">

# <img src="https://static.b100x.ai/github-repos/images/logos/amazon.com.png" width="30" align="top"> Amazon AI Interview Guide (2026)

![Updated](https://img.shields.io/badge/updated-2026.07-00A86B?style=flat-square) ![Sources](https://img.shields.io/badge/sources-Glassdoor·Blind·Reddit·candidate_blogs-6C2BD9?style=flat-square)

**Leadership Principles are a binary gate here: every technical round doubles as a behavioral exam, and failing a single critical LP can sink an otherwise perfect performance.**

</div>

---

## 1. Company AI Context (2026)

Amazon's AI landscape is split between the **AGI Lab** (frontier research on next-gen foundation models) and **AWS AI/Bedrock** (platform and B2B AI). The AGI Lab has a bar similar to OpenAI/DeepMind, focusing on scaling laws and agentic behavior. AWS AI focuses on the "democratization" of AI, hiring for Bedrock's orchestration and model-as-a-service layers [AIOfferly, Nov 2025].

## 2. Interview Process, Stage by Stage

- **Recruiter Screen**: 30 min. Basic fit and experience check.
- **Technical Phone Screen**: 60 min. Coding (LeetCode Medium) + 1-2 ML fundamental questions [AIOfferly, Nov 2025].
- **The Loop (Onsite)**: 4-5 rounds.
    - **Coding (1-2 rounds)**: Data structures and algorithms; often includes an ML-specific coding task (e.g., implement a specific optimizer) [Reddit, 2025].
    - **ML System Design (1 round)**: Heavy focus on scalability and Bedrock-style orchestration.
    - **Behavioral (All rounds)**: Every single technical round includes 15-20 minutes of Leadership Principle (LP) questions [Amazon.jobs, 2026].
- **Timeline**: 4-8 weeks from application to offer [Jobright, Dec 2025].

## 3. Real Interview Questions Reported by Candidates

**Coding & ML Fundamentals**

> 1. "Implement an optimization algorithm (e.g., Adam) from scratch in Python" [Reddit, 2025]

> 2. "Given a list of documents, implement a basic TF-IDF search" [AIOfferly, Nov 2025]

> 3. "Explain the difference between L1 and L2 regularization and when to use each" [AIOfferly, Nov 2025]

> 4. "How do you implement a sliding window for a time-series forecasting model?" [AIOfferly, Nov 2025]

> 5. "Describe the architecture of a transformer and how self-attention works" [AIOfferly, Nov 2025]

**LLM/GenAI Knowledge**

> 6. "How would you design a system to handle multi-turn conversations in Bedrock?" [AIOfferly, Nov 2025]

> 7. "Explain the concept of 'Chain of Thought' prompting and how to optimize it" [AIOfferly, Nov 2025]

> 8. "What are the trade-offs between using a vector database vs. a keyword search in RAG?" [AIOfferly, Nov 2025]

> 9. "How do you optimize an LLM for low-latency inference in a production environment?" [AIOfferly, Nov 2025]

**ML System Design**

> 10. "Design a large-scale model training cluster for a trillion-parameter model" [AIOfferly, Nov 2025]

> 11. "Design a system for automatic data labeling using a smaller 'teacher' model" [AIOfferly, Nov 2025]

> 12. "How would you build a personalized recommendation system for Amazon's homepage?" [AIOfferly, Nov 2025]

**Behavioral (LP-focused)**

> 13. "Tell me about a time you had to deliver a result under a very tight deadline (Deliver Results)" [AIOfferly, Nov 2025]

> 14. "Describe a time you disagreed with your manager but decided to commit to the path (Have Backbone, Disagree and Commit)" [AIOfferly, Nov 2025]

> 15. "Tell me about a time you went above and beyond for a customer (Customer Obsession)" [AIOfferly, Nov 2025]

## 4. Technical Topics to Master for THIS Company

- **Generic Bar**: LeetCode Medium, Python, ML fundamentals.
- **Amazon-Specific**: AWS SageMaker, Bedrock APIs, distributed training at scale, and the 16 Leadership Principles.

## 5. ML System Design Themes

**Theme: Model Orchestration for Enterprise (Bedrock)**

- **Question**: Design a system that allows a company to swap foundation models (e.g., Claude to Titan) without changing their application logic.
- **Outline**:
    1. **Abstraction Layer**: Create a standardized API gateway that maps generic requests to model-specific prompts.
    2. **Prompt Management**: Implement a versioned prompt library that adapts prompts based on the target model's idiosyncrasies.
    3. **Evaluation Suite**: Build an automated A/B testing framework to compare model output quality using a gold dataset.
    4. **Routing**: Implement a router that sends simple queries to smaller, cheaper models and complex queries to larger models.

## 6. Behavioral & Values

**Format**: The 16 Leadership Principles (LPs). These are not just "culture fit"; they are the primary evaluation metric.

- **Key Strategy**: Use the STAR method (Situation, Task, Action, Result). Every "Action" must be a specific step you took, not "we did".
- **Common Pitfall**: Being too vague. Amazon interviewers will drill down into the details (e.g., "What exact number was the latency drop?").

## 7. Compensation (2026)

| Level | Total Compensation (TC) Range | AI Premium | Source |
| :--- | :--- | :--- | :--- |
| L4 (Entry) | $245K - $310K | Moderate | Levels.fyi 2026 |
| L5 (Mid) | $300K - $450K | High | Levels.fyi 2026 |
| L6 (Senior) | $400K - $653K+ | Very High | Levels.fyi 2026 |

## 8. What Gets People Rejected

- **LP Failure**: Failing even one critical Leadership Principle can result in a "No Hire" regardless of technical brilliance.
- **Lack of Ownership**: Answers that sound like "I was just told to do it" are rejected immediately.

## 9. Insider Tips

- **Quantify Everything**: In behavioral rounds, use numbers (e.g., "reduced latency by 15%", "increased accuracy by 2%") to prove impact.
- **Deep Dive**: Be prepared for the interviewer to ask "Why?" five times in a row to test the depth of your knowledge.

## Sources

Inline tags map to the original research references (numbering preserved): [AIOfferly, Nov 2025] → 21 · [Reddit, 2025] → 35, 37 · [Amazon.jobs, 2026] → 88, 89 · [Jobright, Dec 2025] → 24 · [Levels.fyi 2026] → 80, 81.

21. *Amazon ML Interview Questions — 2025/2026 Guide*. https://www.aiofferly.com/career-guide/amazon-ml-interview-questions
22. *Amazon AGI Interview Experience*. https://medium.com/@harimarampally190/my-experience-interviewing-for-amazon-agi-bfb18403a848
23. *Amazon AI Engineer Guide (2026): Job, Salary & Interviews*. https://www.datainterview.com/blog/amazon-ai-engineer-interview
24. *The Ultimate Guide to Acing the Amazon Technical ...*. https://jobright.ai/blog/the-ultimate-guide-to-acing-the-amazon-technical-interview/
25. *Amazon AGI Lab*. https://labs.amazon.science/
34. *ML Engineer GenAI @ Amazon : r/datascience*. https://www.reddit.com/r/datascience/comments/1jrdrpx/ml_engineer_genai_amazon/
35. *Amazon Applied Scientist interview experience*. https://www.reddit.com/r/leetcode/comments/1jwond7/amazon_applied_scientist_interview_experience/
36. *Meta, OpenAI, Google, Amazon top system design ...*. https://www.reddit.com/r/leetcode/comments/1lvnd0t/meta_openai_google_amazon_top_system_design/
37. *My Amazon SDE ML 2025 New Grad Interview Experience*. https://www.reddit.com/r/leetcode/comments/1iw0vsx/my_amazon_sde_ml_2025_new_grad_interview/
38. *Amazon AGI labs Interview : r/leetcode*. https://www.reddit.com/r/leetcode/comments/1ue11x5/amazon_agi_labs_interview/
80. *Amazon Applied Scientist Salary | $245K-$653K+*. https://www.levels.fyi/companies/amazon/salaries/applied-scientist
81. *Amazon Salaries*. https://www.levels.fyi/companies/amazon/salaries
83. *Amazon Applied Scientist Salaries 2026 | $294k-$825k*. https://6figr.com/us/salary/amazon--applied-scientist
84. *What's the compensation band for an L6 SDM?*. https://www.reddit.com/r/amazonemployees/comments/1hvhvan/whats_the_compensation_band_for_an_l6_sdm/
88. *Leadership Principles*. https://www.amazon.jobs/content/en/our-workplace/leadership-principles
89. *Applied Scientist Interview Prep*. https://amazon.jobs/content/en/how-we-hire/applied-scientist-interview-prep
90. *Amazon Behavioral Interview Questions and Answers ...*. https://www.tryexponent.com/blog/how-to-nail-amazons-behavioral-interview-questions
91. *Amazon Applied Scientist Interview (process, questions ...*. https://igotanoffer.com/en/advice/amazon-applied-scientist-interview

---

<div align="center">

**Prepping for Amazon? [Landed](https://landed.jobs) preps you with courses and voice mock interviews, matches you fresh AI roles daily, and drafts your application answers.**

[![Get Started](https://img.shields.io/badge/Get%20Started%20Free-→-6C2BD9?style=for-the-badge)](https://landed.jobs)

<sub>Compiled from public candidate reports — processes change; verify against the official careers page. Interviewed here recently? PRs welcome. · [All guides →](../README.md)</sub>

</div>
