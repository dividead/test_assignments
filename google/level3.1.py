_min = 0
def answer(n):
    def iter(m, s):
        if m == 1:
            global _min
            if _min == 0:
                _min = s
            else:
              _min = min(_min, s) 
            return
        s += 1
        x = []
        if m%2 == 0:
            iter(m/2,s)
        else:
            iter(m - 1,s)
            iter(m + 1,s)
    iter(long(n, 10), 0)
    print(_min)
    return _min

def answer(n):
  n = int(n,10)
  s = -1
  while n > 0:
    if n == 3:
      s += 3
      break
    x = n%4
    if x == 0 or x == 2:
      n /= 2
    if x == 1:
      n -= 1
    if x == 3:
      n += 1
    s += 1
  return s