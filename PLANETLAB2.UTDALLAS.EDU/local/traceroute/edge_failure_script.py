import trparse
from sys import getsizeof
import re
import itertools
import fileinput
input_file = 'data.txt'
sum = 0
with open('traceroute.txt','r') as file1:
	for line in file1:
		data = line.split(" ")
		if('traceroute to ' in line):
			node_name = data[2]
		count = data.count("*")
		if(count>= 1 and count <= 3):
			line = ' '.join(filter(None,line.split(' ')))
			list1 = line.split(' ')
			print(list1)
			print(list1[0])
			if(list1[0] == '1'):
				sum = sum + 1

open('edgeFailure.txt','a+').writelines(',' + str(sum) +'\n')	

