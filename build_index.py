#!/usr/bin/env python3
"""Render README.md (the index) from the guide files in guides/.
Run after adding or editing guides: python3 build_index.py
"""
import re
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = "https://landed.jobs"
ORG = "https://github.com/landedjobs"

GROUPS = [
	("🧪 Frontier labs", "The hardest loops in the industry — research taste, safety, and systems depth.", [
		("openai", "OpenAI", "openai.com"),
		("anthropic", "Anthropic", "anthropic.com"),
		("google-deepmind", "Google DeepMind", "deepmind.google"),
		("meta-ai", "Meta AI", "meta.com"),
		("xai", "xAI", "x.ai"),
		("mistral", "Mistral AI", "mistral.ai"),
	]),
	("🏢 Big tech AI orgs", "ML breadth/depth rounds, team matching, and the AI premium on comp.", [
		("google", "Google", "google.com"),
		("microsoft", "Microsoft", "microsoft.com"),
		("amazon", "Amazon", "amazon.com"),
		("apple", "Apple AIML", "apple.com"),
		("nvidia", "NVIDIA", "nvidia.com"),
		("tesla", "Tesla AI", "tesla.com"),
	]),
	("⚡ AI-native product companies", "Work trials, paid projects, and product-sense rounds — shipping beats puzzles.", [
		("perplexity", "Perplexity", "perplexity.ai"),
		("cursor", "Cursor", "cursor.com"),
		("scale-ai", "Scale AI", "scale.com"),
		("harvey", "Harvey", "harvey.ai"),
		("glean", "Glean", "glean.com"),
		("sierra", "Sierra", "sierra.ai"),
		("notion", "Notion", "notion.so"),
	]),
	("🔧 AI infra & tooling", "Distributed systems, inference economics, and open-source signal.", [
		("databricks", "Databricks", "databricks.com"),
		("hugging-face", "Hugging Face", "huggingface.co"),
		("together-ai", "Together AI", "together.ai"),
		("groq", "Groq", "groq.com"),
		("langchain", "LangChain", "langchain.com"),
		("weights-and-biases", "Weights & Biases", "wandb.ai"),
		("pinecone", "Pinecone", "pinecone.io"),
	]),
	("🚀 Applied AI & forward-deployed", "Decomposition cases, customer scenarios, and practical rounds.", [
		("palantir", "Palantir", "palantir.com"),
		("ramp", "Ramp", "ramp.com"),
		("stripe", "Stripe", "stripe.com"),
		("snowflake", "Snowflake", "snowflake.com"),
		("salesforce", "Salesforce", "salesforce.com"),
		("duolingo", "Duolingo", "duolingo.com"),
		("servicenow", "ServiceNow", "servicenow.com"),
	]),
]


def hook(slug: str) -> str | None:
	p = HERE / "guides" / f"{slug}.md"
	if not p.exists():
		return None
	for line in p.read_text(encoding="utf-8").splitlines():
		m = re.fullmatch(r"\*\*(.+)\*\*", line.strip())
		if m:
			return m.group(1)
	return ""


def cell(slug, name, domain):
	h = hook(slug)
	if h is None:
		return f'<td align="center" width="33%"><img src="https://unavatar.io/{domain}" width="40"><br><b>{name}</b><br><sub>🔜 guide in progress</sub></td>'
	short = h if len(h) <= 150 else h[:150].rsplit(" ", 1)[0] + " …"
	return (
		f'<td align="center" valign="top" width="33%"><a href="guides/{slug}.md"><img src="https://unavatar.io/{domain}" width="40"></a><br>'
		f'<b><a href="guides/{slug}.md">{name}</a></b><br><sub>{short}</sub></td>'
	)


def grid(companies):
	cells = [cell(*c) for c in companies]
	rows = ["<tr>" + "".join(cells[i : i + 3]) + "</tr>" for i in range(0, len(cells), 3)]
	return "<table>\n" + "\n".join(rows) + "\n</table>"


def main():
	today = datetime.now(timezone.utc).strftime("%Y.%m")
	live = sum(1 for _, _, cs in GROUPS for c in cs if (HERE / "guides" / f"{c[0]}.md").exists())
	total = sum(len(cs) for _, _, cs in GROUPS)

	toc = " · ".join(f'[{title.split(" ", 1)[1]}](#{re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")})' for title, _, _ in GROUPS)
	sections = "\n\n".join(
		f'<a name="{re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")}"></a>\n## {title}\n\n_{sub}_\n\n{grid(cs)}'
		for title, sub, cs in GROUPS
	)

	readme = f"""<a name="top"></a>

<div align="center">

<a href="{SITE}"><img src="https://static.b100x.ai/email/landed-wordmark.png" alt="Landed" width="200"></a>

<img src="https://static.b100x.ai/github-repos/images/ai-interview-guides/banner.svg" alt="AI Interview Guides" width="100%">

![Guides](https://img.shields.io/badge/{live}%20company%20guides-ff5b29?style=flat-square) ![Updated](https://img.shields.io/badge/updated-{today.replace('.', '.')}-00A86B?style=flat-square) ![Sourced](https://img.shields.io/badge/every%20claim-cited-6C2BD9?style=flat-square) [![Stars](https://img.shields.io/github/stars/landedjobs/ai-interview-guides?style=social)]({ORG}/ai-interview-guides)

**Deep, sourced interview guides for the AI companies everyone wants to join.**
Real processes stage by stage · real questions candidates reported · comp ranges · what gets people rejected.

{toc}

</div>

---

> **How these are built** — each guide is compiled from hundreds of public candidate reports (Glassdoor, Blind, Reddit, interviewing.io, candidate blogs and X threads, 2024–2026), with every process claim and question cited to its source. Anecdote is labeled as anecdote. Processes change — if you interviewed recently, [a PR or issue]({ORG}/ai-interview-guides/issues) makes the guide better for the next person. ⭐ **Star this repo** — guides get refreshed and new companies added.

{sections}

---

## ➕ Add or improve a guide

Interviewed at one of these companies — or one we don't cover yet? [Open an issue →]({ORG}/ai-interview-guides/issues/new?template=add-guide-intel.yml) with what the loop looked like and any questions you were asked, or open a PR editing the company's file in `guides/`. Fresh first-hand reports are what keep these accurate. See [CONTRIBUTING.md](CONTRIBUTING.md).

## What's inside every guide

**1. Company AI context** — who's hiring and for what · **2. The loop, stage by stage** · **3. Real reported questions** (cited) · **4. Technical topics for this company** · **5. Design/practical round themes with worked outlines** · **6. Behavioral & culture** · **7. Compensation** · **8. What gets people rejected** · **9. Insider tips**

## Related

Part of the [Landed]({SITE}) AI-native job-search family:

- 🧭 [awesome-ai-native-jobs]({ORG}/awesome-ai-native-jobs) — the umbrella that maps the whole AI-native job landscape
- ❓ [ai-interview-questions]({ORG}/ai-interview-questions) — 331 real interview questions with answers
- 🔥 [whos-hiring-in-ai]({ORG}/whos-hiring-in-ai) — real hiring posts from founders on X
- 💸 [recently-funded-ai-startups-hiring]({ORG}/recently-funded-ai-startups-hiring) — fresh-capital startups staffing up now
- 🚀 [ai-engineer-jobs]({ORG}/ai-engineer-jobs) — 300 live AI engineer roles, auto-updated
- 🤝 [forward-deployed-engineer-jobs]({ORG}/forward-deployed-engineer-jobs) — FDE & customer-facing engineering
- 📈 [gtm-engineer-jobs]({ORG}/gtm-engineer-jobs) — GTM engineering roles
- 🎓 [ai-fellowships-and-residencies]({ORG}/ai-fellowships-and-residencies) — 75 fellowships, residencies & programs
- 🧪 [projects-to-land-an-ai-job]({ORG}/projects-to-land-an-ai-job) — portfolio projects that actually get you hired
- 📦 [ai-engineer-portfolio-projects]({ORG}/ai-engineer-portfolio-projects) — 80+ buildable portfolio projects
- 🗺️ [ai-product-engineer-roadmap]({ORG}/ai-product-engineer-roadmap) — the AI product engineer roadmap
- 🎯 [become-a-gtm-engineer]({ORG}/become-a-gtm-engineer) — the GTM engineer roadmap

---

<div align="center">

**Reading about interviews isn't practicing them. [Landed]({SITE}) runs voice mock interviews tuned to the company you're targeting — plus daily matched AI roles and agent-drafted application answers.**

[![Get Started](https://img.shields.io/badge/Get%20Started%20Free-→-6C2BD9?style=for-the-badge)]({SITE})

<sub>Compiled from public candidate reports — not affiliated with any company listed. · maintained by <a href="{SITE}">Landed</a></sub>

</div>
"""
	(HERE / "README.md").write_text(readme, encoding="utf-8")
	print(f"index: {live}/{total} guides live")


if __name__ == "__main__":
	main()
