import time

print("Euler 34 - circular primes")

e="y"

while e == "y":
  primes = [2,3,5,7,11,13,17]
  end = int(input("Enter range --> "))
  for i in range (23, end):
    k = 0
    check = True
    while primes[k] < i//2 and check:
      if i%primes[k]==0:
        check = False
      k += 1
    if check:
      primes.append(i)
  
  print(primes)
  e = input("Again? y/n --> ")
