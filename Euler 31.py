import time
import pdb

e = "y"

def count(cur, input):
	global counter
	
	if cur > 0:
		count(cur-1, input)
	remainder = input-coins[cur]
	
	if remainder == 0:
		counter += 1
	elif remainder > 0:
		count(cur, remainder)
	else:
		return

while e == "y":
	counter = 0
	amount = int(input("Input amount in pence --> "))
	coinsf = [200,100,50,20,10,5,2,1]
	coins = [1,2,5,10,20,50,100,200]
	old = time.time()
	count(len(coins)-1, amount)
	
	print(counter, time.time()-old)
	e = input("Again? y/n --> ")
	
