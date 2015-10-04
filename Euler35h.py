import math

end = int(input("Enter range --> "))
primes_h = [1]*(end+2)
for i in range(2,int(math.sqrt(end))+1):
	k = 2*i
	while k <= end:
		primes_h[k] = 0
		k += i
i = 2
primes=[]
while i<len(primes_h):
	if primes_h[i]==1:
		primes.append(i)
	i+=1

check = 1
while check > 0:
	check = int(input("Check --> "))
	if check in primes:
		print("True")
	else:
		print("False")