import numpy as np
from numpy.polynomial import Polynomial

"""
Function for adding two given polynomials
"""


def polyAdd(p1, p2):
    newCoef = [int(p1.coef[i]) + int(p2.coef[i])
               for i in range(max(len(p1.coef), len(p2.coef)))]

    return F2Polynomial(newCoef)


"""
Function for multiplication two given polynomials
"""


def polyMul(p1, p2):
    newCoef = [0 for i in range(len(p1.coef) + len(p2.coef))]

    for index1, coefficient1 in enumerate(p1.coef):
        for index2, coefficient2 in enumerate(p2.coef):
            newCoef[index1 + index2] += (int(coefficient1) * int(coefficient2))

    return F2Polynomial(newCoef)


"""
Function for division of two given polynomials
"""


def polyDiv(p1, p2):
    if sum(p2.coef) == 0:
        raise ZeroDivisionError("Denominator is a zero polynomial!")
    else:
        return F2Polynomial((0))


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
