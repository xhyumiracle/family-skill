#!/usr/bin/env python3
"""Seat metrics for a family run, computed from claims.md and verification.md.

Usage: python3 metrics.py <run dir>

Reads the first markdown table in <run dir>/claims.md (columns: ID | Claim | Cited URL |
Quoted evidence | Seats | Why it matters) and in <run dir>/verification.md (columns: ID |
Claim (short) | Cited URL | Verdict | Flags | Direct? | Source risk | Evidence date |
Eligible | Note). Joins on ID. Prints, per seat code, the claims it contributed, the
CONFIRMED claims only it contributed, PARTIAL, MISQUOTED and NOT-VERIFIED counts, and a
one-line summary for runs.log. Counting by hand produced inconsistent numbers in earlier
runs; this is the only place these numbers should come from.
"""
import re
import sys
from collections import defaultdict
from pathlib import Path


def rows(path):
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or set(cells[0]) <= set("-: ") or cells[0].lower() in ("id", "#"):
            continue
        if re.fullmatch(r"C\d{2,3}", cells[0]):
            out.append(cells)
    return out


def main(run_dir):
    run = Path(run_dir)
    claims = {r[0]: r for r in rows(run / "claims.md")}
    verdicts = {r[0]: r for r in rows(run / "verification.md")}
    if not claims or not verdicts:
        sys.exit("no parsable rows; check the table formats described in the protocols")

    seats_of = {}
    for cid, r in claims.items():
        seats_of[cid] = [s for s in re.split(r"[,\s]+", r[4]) if re.fullmatch(r"S\d+", s)]

    per = defaultdict(lambda: {"contributed": 0, "confirmed_only_this_seat": 0,
                               "partial": 0, "misquoted": 0, "not_verified": 0})
    for cid, seats in seats_of.items():
        v = verdicts.get(cid)
        verdict = v[3].upper() if v else "NOT-VERIFIED (unchecked)"
        for s in seats:
            per[s]["contributed"] += 1
            if verdict.startswith("CONFIRMED") and len(seats) == 1:
                per[s]["confirmed_only_this_seat"] += 1
            if verdict.startswith("PARTIAL"):
                per[s]["partial"] += 1
            if verdict.startswith("MISQUOTED"):
                per[s]["misquoted"] += 1
            if verdict.startswith("NOT-VERIFIED"):
                per[s]["not_verified"] += 1

    checked = sum(1 for v in verdicts.values() if not v[3].upper().startswith("NOT-VERIFIED"))
    downgraded = sum(1 for v in verdicts.values() if v[3].upper().startswith(("PARTIAL", "MISQUOTED")))
    print(f"claims listed: {len(claims)} · checked: {checked} · downgraded: {downgraded}")
    print("seat | contributed | CONFIRMED only this seat | PARTIAL | MISQUOTED | NOT-VERIFIED")
    for s in sorted(per, key=lambda x: int(x[1:])):
        m = per[s]
        print(f"{s} | {m['contributed']} | {m['confirmed_only_this_seat']} | {m['partial']} | {m['misquoted']} | {m['not_verified']}")
    summary = " ".join(f"{s}:{per[s]['confirmed_only_this_seat']}/{per[s]['contributed']}" for s in sorted(per, key=lambda x: int(x[1:])))
    print(f"runs.log fragment: claims {checked}/{len(claims)} checked, {downgraded} downgraded | unique-confirmed/contributed per seat: {summary}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
