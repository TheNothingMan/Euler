import time
import pdb

print("Euler p 30 - Digit fifth powers")

e = "y"

while e == "y":
	p = int(input("Enter power --> "))
	max = int(input("Enter max --> "))
	
	numbers = []
	sum = 0
	old = time.time()
	for i in range(10**(p-2), max+1):
		helper=0
		h=i
		while h>0:
			helper += (h%10)**p
			h = h//10
		if helper==i:
			numbers.append(i)
			sum += helper
	
	print("Sum is", sum, time.time()-old, "ms", numbers)
	
	e = input("Again? y/n --> ")
	if e!="y" and e!="n":
		e = input("Wrong input! y/n --> ")
