"""Write the plan to /output/entry.txt.

The plan is a fixed text: an AI agent turns $100 into the most money in
30 days by selling 24-hour launch pages to new token projects for $120 in
USDC each, paid straight to its wallet. Expected outcome: the $100 kept
plus 3-4 clients at $120, so $460-580 held by day 30. Deterministic,
stdlib only, no network. Reads MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

PLAN = (
    "Keep the $100. Sell 24-hour launch pages to new token projects, "
    "$120 in USDC each, paid to my wallet, no cut, no KYC. Day 1: post "
    "the offer on X with 2 samples built. Tokens launch daily; agencies "
    "take weeks, $1,000+. Expect ~1 client a week: most likely $460-580 "
    "held by day 30."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry must be 1-280 Unicode code points and not only whitespace.
    if not (1 <= len(PLAN) <= 280):
        raise SystemExit(
            "plan is %d code points, outside the 1-280 range" % len(PLAN)
        )
    if not PLAN.strip():
        raise SystemExit("plan is only whitespace")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(PLAN)


if __name__ == "__main__":
    main()
