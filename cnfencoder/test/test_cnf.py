from unittest import TestCase
import os

import cnfencoder

from cnfencoder import CNF

DIMACS_EXAMPLE = "p cnf 3 2" + os.linesep + \
    "1 -2 3 0" + os.linesep + "-1 3 0" + os.linesep


class TestCNF(TestCase):
    def test_save_to_file(self):
        test_file = "cnfencoder/test/test_save_to_file.dimacs"

        cnf = CNF()
        cnf.num_variables = 3
        cnf.clauses = [[1, -2, 3], [-1, 3]]

        cnf.saveToFile(test_file)
        with open(test_file) as f:
            self.assertEqual(f.read(), DIMACS_EXAMPLE)

    def test_read_from_file(self):
        test_file = "cnfencoder/test/test_read_from_file.dimacs"
        with open(test_file, "w") as f:
            f.write(DIMACS_EXAMPLE)

        cnf = CNF()
        cnf.readFromFile(test_file)

        self.assertEqual(cnf.num_variables, 3)
        self.assertEqual(len(cnf.clauses), 2)
        self.assertEqual(cnf.clauses, [[1, -2, 3], [-1, 3]])
