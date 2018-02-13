import trparse
import re
import itertools
import fileinput
input_file = 'data.txt'
sum=0
with open('data.txt','r') as file1:
	node_name = 'planetlab4.cs.uoregon.edu'
	for line in file1:
		data = line.split(" ")
		count = line.count("*")
		if(count <= 3):
			sum = sum + count		

open('count.txt','a+').writelines(',' + str(sum) +'\n')	