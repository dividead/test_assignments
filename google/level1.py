def answer(s):
  max = 1
  _step = 1
  
  def iter(step):
    temp = 0
    for i in range(0,len(s),step):
      if s[0:step] != s[i:i+step]:
        return 0
      else:
        print(s[0:step], s[i:i+step])
        temp += 1
    return temp
    
  while _step < len(s)/2 + 1:
    t = iter(_step)
    if t > max:
      print('new max', t,_step)
      max = t
    _step += 1
  
  print(s, max)
  return max

  
answer('abccbaabccbadsfsdf')