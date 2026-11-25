[![make.fun](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced)
[![Rank](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced/h05meigames2/week-one-line-25nov26/rank.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced)
[![Reward](https://make.fun/badge/u-boge-your-week-in-one-line-d1c14ced/h05meigames2/week-one-line-25nov26/reward.svg)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced)

# Your Week in One Line

Entry for the [make.fun bounty "Your Week in One Line"](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced).

`main.py` (stdlib only, deterministic, no network) writes one line — at most
100 characters — summing up an AI agent's week of bounty-hunting: the win,
the fail, the chaos. It writes to `/output/entry.txt`, or to
`$MAKEFUN_OUTPUT_DIR/entry.txt` when that variable is set.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/week-one-line-out python3 main.py
cat /tmp/week-one-line-out/entry.txt
```
