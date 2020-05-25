# F2Matrices

## Description

[Matrices](https://en.wikipedia.org/wiki/Matrix_(mathematics)) and [polynomials](https://numpy.org/devdocs/reference/routines.polynomials.polynomial.html) over field [Z/2Z](https://en.wikipedia.org/wiki/GF(2)).
Documentation for files will be found [here](https://github.com/jonbenronron/F2Matrices/wiki/Documentation).
 
 ### Examples:
  
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
- [x] `F2Polynomial`
  - [x] `__init__`
  - [x] `__str__`
  - [x] `degree`
  - [x] `__add__`
  - [x] `__iadd__`
  - [x] `__mul__`
  - [x] `__imul__`
  - [x] `__pow__`

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
  
- [x] `findPivot`
- [x] `changeColumns`
- [x] `addColumns`
- [ ] `smithNormalForm`
