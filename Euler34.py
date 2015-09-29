import time
import pdb
import math

e = "y"

print("Euler problem 34 - Digit factorials")

while e == "y":
	
	numbers = []
	factorials = []
	for i in range(0,10):
		factorials.append(math.factorial(i))
	
	maxDig = 5
	target = input("Enter range or 0/empty for default (25401610) --> ")
	target = int(target) if target != "" else 0
	if target == 0:
		target = 25401610
	old = time.time()
	for i in range(10, target):
		hstr = str(i)
		if i<factorials[maxDig]:
			if str(maxDig) in hstr:
				continue
			msum = 0
			for k in hstr:
				msum += factorials[int(k)]
			if msum == i:
				numbers.append(i)
				print(i)
		else:
			if maxDig < 9:
				maxDig += 1
	
	msum = sum(numbers)
	print(msum, time.time()-old)
	e = input("Again? y/n --> ")