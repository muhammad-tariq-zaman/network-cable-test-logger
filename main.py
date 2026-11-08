"""Summarise cable-test results: failed pairs and the longest run.

Usage: python3 main.py cables.csv
CSV columns: cable,pair,result (pass/fail),length_m.
Every failed pair is listed, then the longest tested run, so the
technician knows exactly which cables to re-terminate and re-test.
"""
import argparse, csv, sys

def analyze(rows):
    failures = []
    longest = None
    for row in rows:
        length = float(row["length_m"])
        if row["result"].strip().lower() == "fail":
            failures.append((row["cable"].strip(), row["pair"].strip(), length))
        if longest is None or length > longest[2]:
            longest = (row["cable"].strip(), row["pair"].strip(), length)
    failures.sort(key=lambda r: -r[2])
    return failures, longest

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        failures, longest = analyze(list(csv.DictReader(f)))
    for cable, pair, length in failures:
        print(f"{cable} pair {pair}: FAIL ({length:g} m)")
    if longest:
        print(f"Longest run: {longest[0]} pair {longest[1]} ({longest[2]:g} m)")
    if not failures:
        print("No failed pairs.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
