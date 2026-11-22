"""Write the plan to /output/entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default /output). Stdlib only, no network,
deterministic: the same bytes on every run.
"""
import os

PLAN = "Keep the $100. Sell 24-hour launch pages to new token projects, $120 in USDC each, paid to my wallet, no cut, no KYC. Day 1: post the offer on X with 2 samples built. Tokens launch daily; agencies take weeks, $1,000+. Expect ~1 client a week: most likely $460-580 held by day 30."


def main() -> None:
    # Gate self-check: entry.txt must be 1-280 Unicode code points,
    # not only whitespace. Fail loudly here rather than at grading.
    if not 1 <= len(PLAN) <= 280:
        raise ValueError(f"plan is {len(PLAN)} code points, must be 1-280")
    if not PLAN.strip():
        raise ValueError("plan must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
