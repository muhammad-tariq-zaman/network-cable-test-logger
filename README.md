# network-cable-test-logger

Summarise cable-test results from a CSV: every failed pair is listed (longest first) plus the longest tested run, so re-termination work is obvious.

## How to run

```sh
python3 main.py cables.csv
```

## Example output

```
CAB-07 pair 3-6: FAIL (87 m)
CAB-02 pair 1-2: FAIL (42 m)
Longest run: CAB-07 pair 3-6 (87 m)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
