import time
import math
import itertools

print("Euler 35 - circular primes")

e="y"

while e == "y":
	primes = [2,3,5,7,11,13,17,19]
	end = int(input("Enter range --> "))
	# old = time.time()
	# for i in range (23, end, 2):
		# k = 0
		# check = True
		# while primes[k] <= math.sqrt(i) and check:
			# if i%primes[k]==0:
				# check = False
			# k += 1
		# if check:
			# primes.append(i)
	
	# print(primes, time.time()-old)
	
	old = time.time()
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
	print(primes, time.time()-old)
	count = 0

	test = []
	for i in primes:
		check = True
		permuts = itertools.permutations(list(str(i)))
		permutints = [int(''.join(x)) for x in permuts]
		print(permutints)
		for k in permutints:
			if k not in primes:
				check = False
				break
		if check:
			test.append(i)
			count += 1
	
	print(count, test, time.time()-old)
	e = input("Again? y/n --> ")
