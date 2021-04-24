from unittest import TestCase

from cnfencoder import Lexer, Token, TokenType


class TestCNF(TestCase):
    def test_valid_formula(self):
        formula = "(X1 ∧ X22 ∧ X4) → ((X3 ↔ ¬X5) ⊕ X2)"
        expected_types = [
            TokenType.PARENTHESES_OPEN,
            TokenType.VARIABLE,
            TokenType.AND,
            TokenType.VARIABLE,
            TokenType.AND,
            TokenType.VARIABLE,
            TokenType.PARENTHESES_CLOSE,
            TokenType.IMPLICATION,
            TokenType.PARENTHESES_OPEN,
            TokenType.PARENTHESES_OPEN,
            TokenType.VARIABLE,
            TokenType.EQUIVALENCE,
            TokenType.NEGATION,
            TokenType.VARIABLE,
            TokenType.PARENTHESES_CLOSE,
            TokenType.XOR,
            TokenType.VARIABLE,
            TokenType.PARENTHESES_CLOSE
        ]

        lexer = Lexer(formula)

        tokens = []
        token = lexer.getToken()
        while token.type != TokenType.EOF:
            tokens.append(token)
            token = lexer.getToken()

        self.assertListEqual(expected_types, [t.type for t in tokens])

        self.assertEqual(tokens[1].text, 'X1')
        self.assertEqual(tokens[3].text, 'X22')

    def test_invalid_character(self):
        formula = '(X1 + X2)'

        lexer = Lexer(formula)

        try:
            tokens = []
            token = lexer.getToken()
            while token.type != TokenType.EOF:
                tokens.append(token)
                token = lexer.getToken()
            self.assertTrue(False)
        except:
            self.assertTrue(True)
