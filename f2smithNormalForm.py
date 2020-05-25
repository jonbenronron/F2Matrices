from f2polynomial import F2Polynomial
from f2matrices import F2Matrix

"""
Function for finding a pivot element from the matrix
"""


def findPivot(row):

    # Choose left most element to be a pivot
    pivotPolynomial = row[0]

    # Compare other elements with current pivot
    for element in row:

        # If there exists a better candidate for pivot element,
        # change pivot element into it
        pivotPolynomial = element if (element.degree(
        ) < pivotPolynomial.degree()) else pivotPolynomial

    return row.index(pivotPolynomial)


"""
Function for Smith Normal Form
"""


def smithNormalForm(matrix):

    # Iterate over the rows of matrix
    for row in matrix.rows:

        # Choose a pivot element
        pivotIndex = findPivot(row)

        # If column with pivot element is not first from left
        # change it's place with most left column
        if pivotIndex:
            matrix.changeColumns(pivotIndex, 0)
            pivotIndex = 0

        # Try to reduce other elements in the row that differ from zero
        # with adding the column with the pivot element to others
        for index, polynomial in enumerate(row):

            # f(0) = 1 + 0 + 0^2 + 0^3 + ... + 0^n
            valueAtZero, firstTerm = polynomial.evaluate(0), polynomial.coef[0]

            # f(0) = 1     and f(x) = 1 + D + ... + D^n
            if valueAtZero and firstTerm:
                pass

            # f(0) = 1       and f(x) = 0 + D + ... + D^n
            elif valueAtZero and not firstTerm:
                pass

            else:
                pass


a = F2Polynomial([1, 0, 0, 0])
b = F2Polynomial([1, 1, 0, 0])
c = F2Polynomial([1, 1, 1, 0])
d = F2Polynomial([1, 1, 1, 1])

f = F2Matrix([[d, b],
              [c, d]])

print(str(f), "\n")
smithNormalForm(f)
