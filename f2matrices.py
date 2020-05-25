import sys
import f2polynomial as f2p
from f2polynomial import F2Polynomial

"""
Function for dot product of two given vectors
"""


def dotProduct(vector, wector):
    if len(vector) == len(wector):
        try:
            # Multiply corresponding elements of given vectors
            productVector = list(map(lambda polynomial,
                                     qolynomial: polynomial * qolynomial, vector, wector))
            # Find and measure the length of the polynomial with longest list of coefficients
            length = 0
            for polynomial in productVector:
                length = len(polynomial.coef) if length < len(
                    polynomial.coef) else length
            # Initialize a zero polynomial with given length
            sumOfProductValues = F2Polynomial([0] * length)
            # Iterate and sum up the elements of vector we got from multiplication
            for productPolynomial in productVector:
                sumOfProductValues += productPolynomial
            return sumOfProductValues
        except:
            print("Unexpected error:", sys.exc_info()[0])
    else:
        raise TypeError("Vectors have different dimensions!")
        return F2Polynomial([0])


"""
Class for matrices with elements from polynomial ring over field Z/2Z
"""


class F2Matrix:

    """
    Initialization
    """

    def __init__(self, rows=[[F2Polynomial([0])]]):
        self.rows = rows

    """
    String format of matrix:

        example:

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

        # Build a string from the matrix
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

        # Make sure the dimensions of matrices are equal
        # If not, raise an type error and return an empty matrix
        if len(self.rows) == len(other.rows) and len(self.rows[0]) == len(self.rows[0]):

            # Iterate over rows of both matrices and sum up the corresponding polynomial elements:
            #
            #   p_(i,j) + q_(i,j) = r_(i,j)
            #
            newRows = []
            for rowIndex, row in enumerate(self.rows):
                newRow = []
                for polynomialIndex, polynomial in enumerate(row):
                    newRow.append(
                        polynomial + other.rows[rowIndex][polynomialIndex])
                newRows.append(newRow)
            return F2Matrix(newRows)
        else:
            raise TypeError("Matrices have different size!")
            return F2Matrix([[F2Polynomial([0])]])

    def __iadd__(self, other):
        return self + other

    """
    Method for matrix transpose
    """

    def transpose(self):
        # Transposed matrix will have columns as rows and rows as columns from original matrix
        #
        #   Original:           Transposed:
        #
        #   |a, b|      =       |a, c|^T
        #   |c, d|              |b, d|
        #
        transposedMatrix = [[self.rows[j][i]
                             for j in range(len(self.rows))] for i in range(len(self.rows[0]))]
        return F2Matrix(transposedMatrix)

    """
    Methods for multiplication operation
    """

    def __mul__(self, other):
        # Make sure that the row dimension of right matrix A
        # and the column dimension of left matrix B
        # are equal when the product is
        #
        #   A * B = C
        #
        # If not, raise an type error and return an empty matrix
        if len(self.rows[0]) == len(other.rows):
            # Return a matrix C where elements of C are dot products of
            # rows of matrix A with columns of matrix B
            return F2Matrix([[dotProduct(row, column) for column in other.transpose().rows] for row in self.rows])
        else:
            raise TypeError(
                "Row and column dimensions of matrices don't match!")
            return F2Matrix([[F2Polynomial([0])]])

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
