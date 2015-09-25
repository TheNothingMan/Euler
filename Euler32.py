import time

def check(prod, div):
  
  quot = prod//div
  dig = str(prod)+str(div)+str(quot)
  #print(prod, dig)
  if len(dig)!=9:
    return False
  for i in range(1,10):
    if str(i) not in dig:
      return False
  print(prod, "=", div, "*", quot)
  return True

e = "y"
print("Euler Problem 32 - Pandigital products")

while e == "y":
  pn = []
  old = time.time()
  for i in range(1000, 10000):
    for k in range(2, 100):
      if (i%k == 0):
        if check(i, k):
          pn.append(i)
          break
  sum = 0
  for i in pn:
    sum += i
  print(sum, pn, time.time()-old)
  e = input("Again? y/n -->")