import unittest
from convert import *

class TutotiralTest(unittest.TestCase):
    def test(self):
        file = "examples/data/tcga.rnaseq_fpkm_uq.example.txt.gz" # First column is "project", the labels.
        convert(file, "/tmp/DeepInsight")

if __name__ == "__main__":
    unittest.main()