import time

e="y"

while e=="y":
	old = time.time()
	primes = [2,3,5,7]
	for i in range(11, 1001):
		p=True
		for k in primes:
			if i%k == 0:
				p=False
				break
		if p:
			primes.append(i)
	
	count = 0;
	max = 0;
	max_a = 0;
	max_b = 0;
	for i in primes:
		for k in range(-1000, 1001):
			count = 0;
			for n in range(0, 1000):
				if abs(n**2+k*n+i) not in primes:
					break
			if n > max:
				max = n
				max_a = k
				max_b = i
	print(max_a, max_b, max_a*max_b, max, time.time()-old)
	e=input("Again? y/n --> ")