import unittest
from kstring import KUniqueCharacters

class SimpleTest(unittest.TestCase):
    def test1(self):
        Input1 = "3aabacbebebe"
        Output1 = "cbebebe"
        Input2 = "2aabbcbbbadef"
        Output2 = "bbcbbb"
        self.assertEqual(KUniqueCharacters(Input1), Output1)
        self.assertEqual(KUniqueCharacters(Input2), Output2)

if __name__ == '__main__':
   unittest.main()
