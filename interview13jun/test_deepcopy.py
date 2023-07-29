import unittest
from deepcopy import *

class TestDeepCopy(unittest.TestCase):
    def TestList(self):
        l1 = [1,[1,2,3],3]
        dc = DeepCopy(l1)
        l2 = dc.deep_copy(l1)
        self.assertEqual(id(l1) != id(l2))
        self.assertEqual(id(l1[1]) == id(l2[1]))



if __name__ == "__main__":
    unittest.main()


