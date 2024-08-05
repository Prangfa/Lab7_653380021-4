#653380021-4 Prangnapha Wibunatthaphon
import unittest
import sys
import os

sys.path.append('/workspaces/Lab7_653380021-4/Lab7.6_CDCCoverage/assignment/clumpCount/source')


from CountClump import CountClump

class TestCountClump(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(CountClump.count_clumps([]), 0)

    def test_no_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 3, 4, 5]), 0)

    def test_one_clump(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 3, 4]), 1)

    def test_multiple_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 3, 3, 4, 4, 4, 1]), 3)

    def test_all_identical_elements(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 1, 1, 1]), 1)

    def test_alternating_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 2, 2, 3, 3, 4, 4]), 4)

    def test_single_element(self):
        self.assertEqual(CountClump.count_clumps([1]), 0)

    def test_two_different_elements(self):
        self.assertEqual(CountClump.count_clumps([1, 2]), 0)

    def test_two_same_elements(self):
        self.assertEqual(CountClump.count_clumps([1, 1]), 1)

    def test_large_input(self):
        self.assertEqual(CountClump.count_clumps([1,1,1,1,2,2,2,2]), 2)

    def test_non_consecutive_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 1, 2, 3, 1, 1]), 2)

    def test_mixed_elements(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 3, 1, 1, 2, 2]), 3)

if __name__ == '__main__':
    unittest.main()