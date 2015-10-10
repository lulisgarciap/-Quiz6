def superpower(a, b) :
  if(b == 0) :
      return 1
  else :
      return a * superpower(a, b-1)

print(superpower(3, 4))
