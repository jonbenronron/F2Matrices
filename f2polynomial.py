import numpy as np
from numpy.polynomial import Polynomial


"""
Class for polynomials over field Z/2Z
"""


class F2Polynomial(Polynomial):

    """
    Initialization of base 2 polynomial:
    - Coefficients will be in mod 2 | np.fmod(coef, 2)

    """

    def __init__(self, coef):
        super().__init__(np.fmod(coef, 2))

    """
    Polynomials will be represented in the string
    format similiarly as in the example given here:
    
       1 + D + D^2 + ... + D^n
       
    """

    def __str__(self):
        s = ""
        nonZeroList = []
        for index, coefficient in enumerate(self.coef):
            if coefficient:
                if index == 0:
                    nonZeroList.append(str(int(coefficient)))
                elif index == 1:
                    nonZeroList.append("D")
                else:
                    nonZeroList.append("D^" + str(index))

        s = " + ".join(nonZeroList)
        if len(s) == 0:
            s = "0"
        return s

    """
    Method for returning the degree of the polynomial
    """

    def degree(self):
        maxDeg = 0
        for degree, coefficient in enumerate(self.coef):
            if coefficient != 0:
                maxDeg = degree

        return maxDeg + 1

    """
    Methods for addition operation
    """

    def __add__(self, other):
        newCoef = [int(self.coef[i]) + int(other.coef[i])
                   for i in range(max(len(self.coef), len(other.coef)))]

        return F2Polynomial(newCoef)

    def __iadd__(self, other):
        return self + other

    """
    Methods for multiplication operation
    """

    def __mul__(self, other):
        newCoef = [0 for i in range(len(self.coef) + len(other.coef))]

        for index1, coefficient1 in enumerate(self.coef):
            for index2, coefficient2 in enumerate(other.coef):
                newCoef[index1 +
                        index2] += (int(coefficient1) * int(coefficient2))

        return F2Polynomial(newCoef)

    def __imul__(self, other):
        return self * other

    """
    Methods for power operation
    """

    def __pow__(self, power):
        result = self
        for i in range(power - 1):
            result *= self
        return result
