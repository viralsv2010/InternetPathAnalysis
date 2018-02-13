#!/usr/bin/python
import subprocess as sp

array = []
index = 0
with open("1000NodesList.txt", "r") as f:
  for line in f:
    array.append(line)
    print("\n")
    ip = array[index]
    status,result = sp.getstatusoutput("ping " + ip)
    if status == 0:
    	print("reachable  :: " + array[index])
    	with open('newfile.txt', 'a+') as f:
    		f.write(array[index])
    		f.write("\n")
    index+=1;