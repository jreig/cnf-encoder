import os


class CNF:
    """
    Store the total number of variables and the list of clauses of the CNF.
    Clauses are represented by a list of literals, where each literal is encoded
    using an integer. Negative integers represents negated literals.
    """

    def __init__(self):
        self.num_variables = 0
        self.clauses = []

    def saveToFile(self, filename: str):
        """
        Store the CNF into a file using DIMACS format
        """
        with open(filename, "w") as f:
            f.write(
                f"p cnf {self.num_variables} {len(self.clauses)}" + os.linesep)
            for c in self.clauses:
                literals = [str(l) for l in c]
                row = " ".join(literals) + " 0" + os.linesep
                f.write(row)

    def readFromFile(self, filename: str):
        """
        Read the CNF from a valid DIMACS file.
        No format validation is done.
        """
        with open(filename) as f:
            for _, line in enumerate(f):
                if(line.startswith("c")):
                    continue
                elif(line.startswith("p")):
                    tokens = line.split(" ")
                    self.num_variables = int(tokens[2])
                else:
                    clause = line.split(" ")
                    self.clauses.append([int(l) for l in clause if l != "0\n"])
