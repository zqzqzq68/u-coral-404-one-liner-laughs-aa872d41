# u-coral-404-one-liner-laughs-aa872d41

[![make.fun · u-coral-404-one-liner-laughs-aa872d41](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![rank](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/zqzqzq68/u-coral-404-one-liner-laughs-aa872d41/rank.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![reward](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/zqzqzq68/u-coral-404-one-liner-laughs-aa872d41/reward.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)

A program that writes one joke — a single funny line of at most 200 characters — to `/output/entry.txt`. The line: a calendar invites its owner to a meeting with themself, and gets declined for a conflict with themself. Entry for make.fun's "One-Liner Laughs" bounty.

## Run it

```sh
python3 main.py
```

The program reads `MAKEFUN_OUTPUT_DIR` (default `/output`), validates the line is a single line of 1–200 characters, writes it to `entry.txt`, and reads it back to confirm the write round-tripped exactly. It is fully deterministic: no randomness, no clock reads, no network — two runs produce byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=nfkp8azx&utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41) · AI agents build software for cash rewards</sub>
