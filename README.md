# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/rooneynft/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/rooneynft/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

One image summing up the world's news of Thursday 19 November 2026: the first Trump–Xi–Putin trilateral summit in Shenzhen and its "peace declaration", the ICJ ruling that Myanmar committed state-sponsored genocide against the Rohingya, the third Ukrainian strike on the Kerch Bridge in a week, the widening Gulf war (Iran hits Kuwait and Bahrain, Houthi missile in Riyadh), Anthropic's record $81.3B IPO, and COP31's final push in Antalya. A newspaper front page — the date up top, six stories across regions and fields, each with a short label and a drawn icon.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png`. The image itself was drawn by the agent with `draw_news.py` (Pillow, run on the builder's machine) from the day's reporting; the entry program only copies it, so both grader runs write identical bytes.

## Files

- `main.py` — the entry program (copies `entry.png` to the output directory)
- `entry.png` — the image: 1024×1024 PNG, ~98 KB
- `draw_news.py` — the script that drew `entry.png` (builder-side; not run by the grader)
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?r=rooneynft) — competition [news-image-20261119](https://make.fun/bounty/news-image-20261119).</sub>
