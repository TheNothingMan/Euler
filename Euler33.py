import time
import pdb

def check(a,b):
	astr = str(a)
	bstr = str(b)
	if astr[0] in bstr:
		hb = int(bstr.replace(astr[0], ""))
		ha = int(astr.replace(astr[0], ""))
		if a/b == ha/hb:
			return True
	if astr[1] in bstr:
		hb = int(bstr.replace(astr[1], ""))
		ha = int(astr.replace(astr[1], ""))
		if a/b == ha/hb:
			return True
	return False

e = "y"
print("Euler problem 33 - digit cancelling fractions")
while e == "y":
	co = 1
	deno = 1
	old = time.time()
	for i in range(12, 100):
		if i%10==0 or i%10==i//10:
			continue
	
		for k in range (12, i):
			if k%10 == k//10:
			  continue
			if check(k, i):
				print(k, i)
				co *= k
				deno *= i
	print(co, deno)
	i = co
	while i > 2:
	  if co%i == 0 and deno%i == 0:
	    print(co, deno, i)
	    co = co/i
	    deno = deno/i
	    break
	  i = i-1
	print(co, deno, time.time()-old)
	e = input("Again? y/n --> ")