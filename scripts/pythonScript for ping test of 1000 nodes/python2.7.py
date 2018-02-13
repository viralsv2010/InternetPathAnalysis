#!/usr/bin/python
import pyping

array = []
index = 0
with open("1000NodesList.txt", "r") as f:
  for line in f:
    array.append(line)
    print("\n")
    response = pyping.ping(array[index])
    if response.ret_code == 0:
    	print("reachable" + array[index])
    else:
    	print("unreachable")    
    print(array[index])
    index+=1;