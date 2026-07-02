# Contributing

These guides are compiled from public candidate reports. First-hand accounts from people who just interviewed are the most valuable thing you can add.

## 1. Share interview intel (easiest)

[Open an "Add guide intel" issue →](https://github.com/landedjobs/ai-interview-guides/issues/new?template=add-guide-intel.yml) — the company, what the loop looked like, questions you were asked, comp if you're comfortable. Even "the process changed, here's how" is gold.

## 2. Open a PR

- **Improve a guide:** edit the company's file in `guides/`. Keep the 9-section structure, put reported questions in blockquotes with a source, and use tables for comp.
- **Add a new company:** create `guides/<company>.md` from the same template as an existing one, then register it in `build_index.py` (add it to the right group with its logo domain) and run `python3 build_index.py` to refresh the index.

## Ground rules

- **Cite it.** Every process claim and question should trace to a source (a link, or "first-hand — my <month/year> loop").
- **Separate fact from anecdote.** "Confirmed on the careers page" and "one candidate reported" are different — say which.
- **Keep it current.** Loops change; a PR that updates a stale stage or comp number is a real contribution.

Thanks for helping the next candidate. 🙏
