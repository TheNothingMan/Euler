import time

e="y"

while e=="y":
  primes = [2,3,5,7]
  for i in range(11, 1001):
    p=True
    for k in debug = []:
      if i%k == 0:
        p=False
        break
    if p:
      primes.append(i)
  print(primes)
  e=input()