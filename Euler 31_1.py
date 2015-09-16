import time
import pdb

e = "y"

def count(coin_index, remainder, level):
	global counter
	#global level
	level +=1
	while coin_index > 0 :
		remainder1 = remainder
		print("c_i:", coin_index, ", r:", remainder, ", l:", level, ", c:", counter)
		while remainder1 >= coinsr[coin_index] :
			remainder1 = remainder - coinsr[coin_index]
			print("		c_i:", coin_index, ", r:", remainder, ", l:", level, ", c:", counter)
			if remainder1 == 0 :
				counter+=1
			count(coin_index, remainder1, level)
		coin_index-=1
	#level-=1
	return
	
while e == "y":
	counter = 0
	#level = 0
	#amount = int(input("Input amount in pence --> "))
	coinsf = [200,100,50,20,10,5,2,1]
	coinsr = [1,2,5,10,20,50,100,200]
	#remainder = amount
	old = time.time()
	#count(7, amount)
	count(7, 10, 0)
	
	print(counter, time.time()-old)
	e = input("Again? y/n --> ")
	
