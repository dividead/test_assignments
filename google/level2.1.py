def answer(total_lambs):
  def cand(l, total):
    if len(l) == 0:
      return [1]
    if len(l) == 1:
      return [1,2]
    res = [x for x in [l[-1]+l[-2], l[-1]*2] if x <= total]
    return res

  t1 = total_lambs
  t2 = total_lambs
  res = []
  res2 = []
  while t1 > 0:
    next = cand(res, t1)
    if len(next) > 0:
      res.append(min(next))
      t1 -= min(next)
    else:
      break

  while t2 > 0:
    next2 = cand(res2, t2)
    if len(next2) > 0:
      res2.append(max(next2))
      t2 -= max(next2)
    else:
      break
  
  return abs(len(res) - len(res2))