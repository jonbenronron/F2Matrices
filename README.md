# F2Matrices

## Description

Matrices for [polynomials](https://numpy.org/devdocs/reference/routines.polynomials.polynomial.html) over field [Z/2Z](https://en.wikipedia.org/wiki/GF(2)).

## Documentation

### Files

```
f2matrices.py   # Imports F2Polynomial class and functions from f2polynomial.py file
```

### Class F2Matrix
  
  #### Parameters:
  
  ```
  self
  rows=[]
  ```
  
  #### Methods:
  
  _Initialization_:
  ```
  __init__(self, coef):
  return F2Polynomial
  ```
  
  _String format_:
  ```
  __str__(self):
  return String
  ```
  
  _Addition operator_ `+`:
  ```
  __add__(self, other):
  return self + other
  ```
  
  #### Example:
  
  ```
  import f2polynomial as f2p
  
  a = f2p.F2Polynomial([1, 1, 1, 0])
  b = f2p.F2Polynomial([0, 1, 0, 0])
  c = f2p.F2Polynomial([1, 1, 1, 1])
  d = f2p.F2Polynomial([1, 0, 1, 1])

  print(str(F2Matrix([[a, b],
                      [c, d]])))
  ```
  
  will print out:
  
  ```
  |      1 + D + D^2,                 D|
  |1 + D + D^2 + D^3,     1 + D^2 + D^3|
  ```
  

## State
- [x] `F2Polynomial`
  - [x] `__init__`
  - [x] `__str__`
  - [x] `__add__`
  - [ ] `__sub__`
  - [ ] `__mul__`
  - [ ] `__pow__`
