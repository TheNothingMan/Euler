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
	
	old = time.time()
	for i in range(11, 100):
		if i%10==0:
			break
		for k in range (11, i):
			if check(k, i):
				print(k, i)
	
	print(time.time()-old)
	e = input("Again? y/n --> ")