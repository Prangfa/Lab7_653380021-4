#653380021-4 Prangnapha Wibunatthaphon
import unittest
import sys
import os

sys.path.append('/workspaces/Lab7_653380021-4/Lab7.3_BlockCoverage/assignment/clumpCount/source')

from CountClump import CountClump

class TestCountClump(unittest.TestCase):
    def test_empty_list(self):
        assert CountClump.count_clumps([]) == 0

    def test_no_clumps(self):
        assert CountClump.count_clumps([1, 2, 3, 4, 5]) == 0

    def test_one_clump(self):
        assert CountClump.count_clumps([1, 2, 2, 3, 4]) == 1

    def test_all_elements_same(self):
        assert CountClump.count_clumps([1, 1, 1, 1, 1]) == 1

if __name__ == '__main__':
    unittest.main() 