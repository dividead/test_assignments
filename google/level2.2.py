def answer(pegs):
  limit = pegs[1] - pegs[0] - 1
  for x in range(1, limit):
    gears = [x]
    for peg in range(1, len(pegs)):
      gears.append(pegs[peg] - (pegs[peg-1] + gears[-1]))
    if any(d <= 0 for d in gears):
      continue
    if x == 2 * gears[-1]:
      return [x, 1]
    if x+1 == 2 * gears[-1]:
      return [(x * 3) + 1, 3]
    if x+2 == 2 * gears[-1]:
      return [(x * 3) + 2, 3]
  return [-1, -1]