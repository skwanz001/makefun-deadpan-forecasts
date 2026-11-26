#!/usr/bin/env python3
"""Deadpan forecast for a city that does not exist.

make.fun bounty: Deadpan Forecasts for Cities That Do Not Exist
(u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

The entry is one line, at most 160 characters: a weather forecast for an
invented city, absurd yet delivered like a real broadcast line.

Angle (from brainstorming): one strong, original, concrete image instead
of a pile of absurdity. The rain does not fall on the town -- it falls
only *inside* one building, the post office, on a fixed schedule, and the
town treats it as routine bureaucracy: clerks hand out umbrellas and
formal apologies. That is the whole joke, and it lands on first read:
a specific place, specific hours, specific temperatures, and a straight
face. Nothing in the line is random; every detail makes the invented
place feel a little more real.

Writes the line to /output/entry.txt (the grader's gate: UTF-8 text,
1-160 characters, not only whitespace).

Standard library only (os, pathlib) -- the grading sandbox installs
nothing.
"""

import os
from pathlib import Path

FORECAST = (
    "In Drizzlewick, rain falls only inside the post office today, "
    "2 to 4 PM. Clerks will issue umbrellas and formal apologies. "
    "High 66, low 52."
)


def main() -> None:
    # The gate counts characters: 1-160, not only whitespace.
    assert 1 <= len(FORECAST) <= 160, f"forecast is {len(FORECAST)} chars"
    assert FORECAST.strip(), "forecast must not be only whitespace"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(FORECAST, encoding="utf-8")

    # Read it back and re-check the gate exactly as the scorer will:
    # UTF-8, 1-160 characters, not only whitespace.
    written = out_path.read_text(encoding="utf-8")
    assert written == FORECAST, "round-trip mismatch"
    assert 1 <= len(written) <= 160 and written.strip()
    print(f"Wrote {len(written)}-char forecast to {out_path}")
    print(written)


if __name__ == "__main__":
    main()
