import sys
import f2polynomial as f2p

"""
Function for dot product of two given vectors
"""


def dotProduct(v, u):
    if len(v) == len(u):
        try:
            newVector = []
            for index, polynom in enumerate(v):
                newVector.append(f2p.polyMul(polynom, u[index]))
        except:
            print("Unexpected error:", sys.exc_info()[0])
        length = 0
        for p in newVector:
            length = len(p.coef) if length < len(p.coef) else length
        sumOfProductValues = f2p.F2Polynomial([0] * (length))
        for productPolynom in newVector:
            sumOfProductValues = f2p.polyAdd(
                sumOfProductValues, productPolynom)
        return sumOfProductValues
    else:
        raise TypeError("Vectors have different dimensions!")
        return f2p.F2Polynomial([0])


"""
Class for matrices with elements from polynomial ring over field Z/2Z
"""


class F2Matrix:

    """
    Initialization
    """

    def __init__(self, rows=[]):
        self.rows = rows

    """
    String format of matrix:

    |      1 + D + D^2,                 D|
    |1 + D + D^2 + D^3,     1 + D^2 + D^3|
     
    """

    def __str__(self):

        # Find and measure the longest polynomial in string format.
        # This is used to determine the size of columns in string format of the matrix.
        str_len = 0
        for row in self.rows:
            for polynomial in row:
                str_len = len(str(polynomial)) if str_len < len(
                    str(polynomial)) else str_len

        # Build the string from the matrix
        s = ""
        for index, row in enumerate(self.rows):
            s += "|"
            for index_p, polynomial in enumerate(row):
                if index_p == len(row) - 1:
                    s += (" " * (str_len - len(str(polynomial)))) + \
                        str(polynomial)
                else:
                    s += (" " * (str_len - len(str(polynomial)))) + \
                        str(polynomial) + ", "
            if index == len(self.rows) - 1:
                s += "|"
            else:
                s += "| \n"
        return s

    """
    Methods for addition operation
    """

    def __add__(self, other):
        if len(self.rows) == len(other.rows) and len(self.rows[0]) == len(self.rows[0]):
            newRows = []
            for rowIndex, row in enumerate(self.rows):
                newRow = []
                for polynomIndex, polynom in enumerate(row):
                    newRow.append(f2p.polyAdd(
                        polynom, other.rows[rowIndex][polynomIndex]))
                newRows.append(newRow)
            return F2Matrix(newRows)
        else:
            raise TypeError("Matrices have different size!")
            return F2Matrix([[f2p.F2Polynomial([0])]])

    def __iadd__(self, other):
        return self + other

    """
    Method for matrix transpose
    """

    def transpose(self):
        newMatrix = [[self.rows[j][i]
                      for j in range(len(self.rows))] for i in range(len(self.rows[0]))]
        return F2Matrix(newMatrix)

    """
    Methods for multiplication operation
    """

    def __mul__(self, other):

        if len(self.rows[0]) == len(other.rows):
            newMatrix = F2Matrix(
                [[dotProduct(row, column) for column in other.transpose().rows] for row in self.rows])
            return F2Matrix([[dotProduct(row, column) for column in other.transpose().rows] for row in self.rows])
        else:
            raise TypeError(
                "Row and column dimensions of matrices don't match!")
            return F2Matrix([[f2p.F2Polynomial([0])]])

    def __imul__(self, other):
        return self * other

    """
    Method for power operation
    """

    def __pow__(self, power):
        result = self
        for i in range(power - 1):
            result *= self
        return result
