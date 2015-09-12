import time
import pdb

e = "y"

while e == "y":
  
  old = time.time()
  
  print(time.time()-old)
  e = input("Again? y/n --> ")