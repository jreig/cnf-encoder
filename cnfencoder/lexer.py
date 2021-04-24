from enum import Enum

# CONSTANT CHARACTERS
EOF = '\0'
VAR_INIT = 'X'
OP_NEG = '¬'    # (U+00AC)
OP_AND = '∧'    # (U+2227)
OP_OR = '∨'     # (U+2228)
OP_XOR = '⊕'    # (U+2295)
OP_IMP = '→'    # (U+2192)
OP_EQU = '↔'    # (U+2194)
P_OPEN = '('
P_CLOSE = ')'


class TokenType(Enum):
    EOF = -1
    VARIABLE = 1
    NEGATION = 2
    AND = 3
    OR = 4
    XOR = 5
    IMPLICATION = 6
    EQUIVALENCE = 7
    PARENTHESES_OPEN = 8
    PARENTHESES_CLOSE = 9


class Token:
    def __init__(self, tokenText, tokenType):
        self.text = tokenText
        self.type = tokenType


class Lexer:
    def __init__(self, input):
        self.source = input + EOF
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = EOF
        else:
            self.curChar = self.source[self.curPos]

    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return EOF
        return self.source[self.curPos+1]

    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    def getToken(self):
        token = None

        self.skipWhitespace()

        # Parenheses
        if self.curChar == P_OPEN:
            token = Token(self.curChar, TokenType.PARENTHESES_OPEN)
        elif self.curChar == P_CLOSE:
            token = Token(self.curChar, TokenType.PARENTHESES_CLOSE)

        # Operators
        elif self.curChar == OP_NEG:
            token = Token(self.curChar, TokenType.NEGATION)
        elif self.curChar == OP_AND:
            token = Token(self.curChar, TokenType.AND)
        elif self.curChar == OP_OR:
            token = Token(self.curChar, TokenType.OR)
        elif self.curChar == OP_XOR:
            token = Token(self.curChar, TokenType.XOR)
        elif self.curChar == OP_IMP:
            token = Token(self.curChar, TokenType.IMPLICATION)
        elif self.curChar == OP_EQU:
            token = Token(self.curChar, TokenType.EQUIVALENCE)

        # EOF
        elif self.curChar == EOF:
            token = Token('', TokenType.EOF)

        # Variables
        elif self.curChar == VAR_INIT:
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            tokText = self.source[startPos: self.curPos + 1]
            token = Token(tokText, TokenType.VARIABLE)

        # Unknown token!
        else:
            raise Exception('Lexing error. Invalid character: ' + self.curChar)

        self.nextChar()
        return token
