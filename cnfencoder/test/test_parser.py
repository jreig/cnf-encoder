from unittest import TestCase

from cnfencoder import Parser


class TestCNF(TestCase):
    def test_valid_formula(self):
        formula = "(X1 ∧ X22 ∧ X4) → ((X3 ↔ ¬X1) ⊕ X2)"
        expected_variables = set(['X1', 'X22', 'X4', 'X3', 'X2'])

        parser = Parser(formula)
        parser.program()

        self.assertSetEqual(parser.variables, expected_variables)

    def test_invalid_formula(self):
        formula = '(X1 ∧ X22 ∨ X4) → ((X3 ↔ ¬X1) ⊕ X2)'

        parser = Parser(formula)

        try:
            parser.program()
            self.assertTrue(False)
        except:
            self.assertTrue(True)
