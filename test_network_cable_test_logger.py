import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import analyze

def row(c, p, result, length):
    return {"cable": c, "pair": p, "result": result, "length_m": str(length)}

class TestCableLog(unittest.TestCase):
    def test_failed_pair_found(self):
        failures, _ = analyze([row("C1", "1-2", "fail", 42)])
        self.assertEqual(failures, [("C1", "1-2", 42.0)])
    def test_pass_not_listed(self):
        failures, _ = analyze([row("C1", "1-2", "pass", 42)])
        self.assertEqual(failures, [])
    def test_longest_run(self):
        _, longest = analyze([row("C1", "1-2", "pass", 42), row("C2", "3-6", "pass", 87)])
        self.assertEqual(longest, ("C2", "3-6", 87.0))
    def test_failures_longest_first(self):
        failures, _ = analyze([row("C1", "1-2", "fail", 10), row("C2", "3-6", "fail", 90)])
        self.assertEqual(failures[0][0], "C2")
    def test_empty_input(self):
        failures, longest = analyze([])
        self.assertEqual((failures, longest), ([], None))
