# F2Matrices

## Description

Matrices for [polynomials](https://github.com/jonbenronron/F2Polynomials) over field [Z/2Z](https://en.wikipedia.org/wiki/GF(2)).

## Documentation

### Files

```
f2matrices.py   # Imports F2Polynomial class and functions from f2polynomial.py file
f2polynomial.py
```

### Class F2Matrix
  
  #### Parameters:
  
  ```
  self
  rows=[[F2Polynomial([0])]]
  ```
  
  _Attributes_:
  
  ```
  rowDimension
  columnDimension
  ```
  
  #### Methods:
  
  _Initialization_:
  ```
  __init__(self, rows):
  return F2Matrix
  ```
  
  _String format_:
  ```
  __str__(self):
  return String
  ```
  
  _Transpose matrix_:
  ```
  transpose(self):
  return F2Matrix   # This will be a transpose version of 'self'
  ```
  
  _Addition operator_ `+`:
  ```
  __add__(self, other):
  return self + other
  ```
  
  _Addition operator_ `+=`:
  ```
  __iadd__(self, other):
  return self + other
  ```
  
  _Multiplication operator_ `*`:
  ```
  __mul__(self, other):
  return self * other
  ```
  
  _Multiplication operator_ `*=`:
  ```
  __imul__(self, other):
  return self * other
  ```
  
  _Power operator_ `**`:
  ```
  __pow__(self, power):
  return self ** power
  ```
 
 ### Functions:
 
 _Dot product of given vectors_:
 ```
 dotProduct(v, u):
 return F2Polynomial
 ```
 
 ### Example:
  
 _Example 1_
  
 ```
 a = F2Polynomial([1, 1, 1, 0])
 b = F2Polynomial([0, 1, 0, 0])
 c = F2Polynomial([1, 1, 1, 1])
 d = F2Polynomial([1, 0, 1, 1])

 f = F2Matrix([[a, b],
               [c, d]])
 g = F2Matrix([[d, c],
               [b, a]])

 h = f + g

 print(str(f), " + \n")
 print(str(g), " = \n")
 print(str(h), "\n")
 ```
  
 will print out:
  
 ```
 |      1 + D + D^2,                 D|
 |1 + D + D^2 + D^3,     1 + D^2 + D^3|  +

 |    1 + D^2 + D^3, 1 + D + D^2 + D^3|
 |                D,       1 + D + D^2|  =

 |      D + D^3, 1 + D^2 + D^3|
 |1 + D^2 + D^3,       D + D^3|
 ```
 _Example 2_
  
 ```
 a = F2Polynomial([1, 0, 0, 0])
 b = F2Polynomial([1, 1, 0, 0])
 c = F2Polynomial([1, 1, 1, 0])
 d = F2Polynomial([1, 1, 1, 1])

 f = F2Matrix([[a, b],
               [c, d]])

 g = F2Matrix([[d, c],
               [b, a]])

 h = f * g

 print(str(f), " * \n")
 print(str(g), " = \n")
 print(str(h), "\n")
 ```
 will print out:
  
 ```
 |                1,             1 + D|
 |      1 + D + D^2, 1 + D + D^2 + D^3|  *

 |1 + D + D^2 + D^3,       1 + D + D^2|
 |            1 + D,                 1|  =

 |              D + D^3,                   D^2|
 |D^2 + D^3 + D^4 + D^5,         D + D^3 + D^4|
 ``` 
  
  _Example 3_
  
 ```
 a = F2Polynomial([1, 0, 0, 0])
 b = F2Polynomial([1, 1, 0, 0])
 c = F2Polynomial([1, 1, 1, 0])
 d = F2Polynomial([1, 1, 1, 1])

 f = F2Matrix([[a, b],
               [c, d]])

 h = f ** 2

 print(str(f), " ** 2 = \n")
 print(str(h), "\n")
 ```
 
 will print out:
 
 ```
 |                1,             1 + D|
 |      1 + D + D^2, 1 + D + D^2 + D^3|  ** 2 =

 |                  D^3,               D + D^4|
 |        D + D^3 + D^5, D^2 + D^3 + D^4 + D^6|
 ```
## State
- [x] `dotProduct`
- [x] `F2Matrix`
  - [x] `__init__`
  - [x] `__str__`
  - [x] `__add__`
  - [x] `__iadd__`
  - [x] `transpose`
  - [x] `__mul__`
  - [x] `__imul__`
  - [x] `__pow__`
