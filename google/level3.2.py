from fractions import Fraction, gcd
def answer(m):
  terminal = lambda a: sum(a) == 0
  paths = []
  def expand(a, add):
    return [(m[ind],Fraction(i,sum(a))*add,ind) for (ind,i) in enumerate(a) if i!=0]

  def iter(a):
    if terminal(a[0]):
      paths.append(a[1:])
    else:
      for i in expand(a[0], a[1].limit_denominator()):
        print(i)
        iter(i)
        
  for i in expand(m[0], 1):
    print(i)
    iter(i)
      
  res = []
  dnm = []
  for i in sorted(paths, key=lambda p: p[1]):
    res.append(i[0])
    dnm.append(i[0].denominator)
  
  greatest = max(dnm)
  x = [i.numerator * greatest / i.denominator for i in res]
  x.append(greatest)
  print(x)


  from itertools import product
from fractions import Fraction, gcd
def answer(m):
  terms = [ind for (ind, i) in enumerate(m) if sum(i) == 0]
  N = sorted(m, key=lambda i: sum(i) > 0)
  T = len(terms)
  O = len(m) - T
  Q = [map(lambda i: Fraction(i, sum(x)), (x[O:] + x[:O])[T:]) for x in N[T:]]
  R = [map(lambda i: Fraction(i, sum(x)), (x[O:] + x[:O])[:T]) for x in N[T:]]
  # F = (I-Q)^-1
  F = inverse(sub(id(len(Q)), Q))
  FR = multiply(F, R)
  dnm = lcm([f.denominator for f in FR[0]])
  res = [f.numerator * dnm / f.denominator for f in FR[0]]
  res.append(dnm)
  print(res)
  return res

def lcm(l):
  low = l[0]
  for i in l[1:]:
    low = low*i/gcd(low, i)
  return low

  
def id(s):
  res = []
  for x in range(s):
    res.append([])
    for y in range(s):
      res[x].append(1) if x == y else res[x].append(0)
  return res
  
def sub(m1, m2):
  m3 = []
  for x in range(len(m1)):
    m3.append([])
    for y in range(len(m1[0])):
      m3[x].append(m1[x][y] - m2[x][y])
  return m3
  
def multiply(matr_a, matr_b):
    cols, rows = len(matr_b[0]), len(matr_b)
    resRows = xrange(len(matr_a))
    rMatrix = [[0] * cols for _ in resRows]
    for idx in resRows:
        for j, k in product(xrange(cols), xrange(rows)):
            rMatrix[idx][j] += matr_a[idx][k] * matr_b[k][j]
    return rMatrix

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def inverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors
  

answer([[1, 1, 1, 0, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
