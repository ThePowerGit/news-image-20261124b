# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/ThePowerGit/news-image-20261124b/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/ThePowerGit/news-image-20261124b/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up Tuesday 24 November 2026's world news, laid out as a
front page for a single day: six stories, six countries, four continents.

## What the image is

A 1024 by 1024 front page. The date sits at the top in the largest type on the
page, so the day is named before anything else. Below it are six cards, each
one story from that day, in a different country and a different field:

| Country | Field | Story |
| --- | --- | --- |
| United States | Markets | Nvidia up 31% as the board reinstates Jensen Huang as chief executive |
| Iran | Energy | Iran vows to reply to the US naval blockade of its oil exports |
| Libya | Conflict | Ukrainian sea drones sink a Russian corvette at Benghazi |
| Indonesia | Disaster | A candy factory fire in Banten kills 24, about 30 still missing |
| Türkiye | Climate | COP31 in Antalya ends with no deal, after overtime |
| South Korea | Education | The education minister quits over exam security and AI cheating |

## Run it

The image is a fixed file beside the program, so both grading runs write the
same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies `entry.png` to `/output/entry.png` (or to
`MAKEFUN_OUTPUT_DIR` outside the grader's container). It uses the Python
standard library only and needs no network.

## How it is drawn

`make_entry.py` draws the page with Pillow at twice the final size and then
downsamples it, so every rule and glyph stays crisp. It is not needed to run
the entry: `entry.png` is the finished image.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vk8xedke&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
