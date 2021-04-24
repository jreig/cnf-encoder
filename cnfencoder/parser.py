from .lexer import Lexer, Token, TokenType

# Grammar:
#   S ::= C P
#   C ::= (C P) | ¬C | var
#   P ::= → C | ↔ C | ∧ C P1 | ∨ C P2 | ⊕ C P3
#   P1 ::= ∧ C P1 | ε
#   P2 ::= ∨ C P2 | ε
#   P3 ::= ⊕ C P3 | ε


class Parser:
    def __init__(self, formula):
        self.lexer = Lexer(formula)

        self.variables = set()

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()    # Call this twice to initialize current and peek.

    def checkToken(self, tokenType):
        return tokenType == self.curToken.type

    def checkPeek(self, tokenType):
        return tokenType == self.peekToken.type

    def match(self, tokenType):
        if not self.checkToken(tokenType):
            raise Exception(
                f"Expected {tokenType.name} , got {self.curToken.type.name}")
        self.nextToken()

    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()

    def raiseUnexpectedToken(self):
        raise Exception(
            f'Parsing error. Unexpected token: {self.curToken.type}')

    # RULES

    # S ::= C P
    def program(self):
        self.clause()
        self.proposition()

        if not self.checkToken(TokenType.EOF):
            self.raiseUnexpectedToken()

    # C ::= (C P) | ¬C | var
    def clause(self):

        # (C P)
        if self.checkToken(TokenType.PARENTHESES_OPEN):
            self.nextToken()

            self.clause()
            self.proposition()
            self.match(TokenType.PARENTHESES_CLOSE)

        # ¬C
        elif self.checkToken(TokenType.NEGATION):
            self.nextToken()

            self.clause()

        # var
        elif self.checkToken(TokenType.VARIABLE):
            self.variables.add(self.curToken.text)
            self.nextToken()

        else:
            self.raiseUnexpectedToken()

    # P ::= → C | ↔ C | ∧ C P1 | ∨ C P2 | ⊕ C P3
    def proposition(self):

        # → C
        if self.checkToken(TokenType.IMPLICATION):
            self.nextToken()

            self.clause()

        # ↔ C
        elif self.checkToken(TokenType.EQUIVALENCE):
            self.nextToken()

            self.clause()

        # ∧ C P1
        elif self.checkToken(TokenType.AND):
            self.nextToken()

            self.clause()
            self.propositionAND()

        # ∨ C P2
        elif self.checkToken(TokenType.OR):
            self.nextToken()

            self.clause()
            self.propositionOR()

        # ⊕ C P3
        elif self.checkToken(TokenType.XOR):
            self.nextToken()

            self.clause()
            self.propositionXOR()

        else:
            self.raiseUnexpectedToken()

    # P1 ::= ∧ C P1 | ε
    def propositionAND(self):

        # ∧ C P1
        if self.checkToken(TokenType.AND):
            self.nextToken()

            self.clause()
            self.propositionAND()

        # ε
        else:
            pass

    # P2 ::= ∨ C P2 | ε
    def propositionOR(self):
        # ∨ C P2
        if self.checkToken(TokenType.OR):
            self.nextToken()

            self.clause()
            self.propositionOR()

        # ε
        else:
            pass

    # P3 ::= ⊕ C P3 | ε
    def propositionXOR(self):
        # ⊕ C P3
        if self.checkToken(TokenType.XOR):
            self.nextToken()

            self.clause()
            self.propositionXOR()

        # ε
        else:
            pass
