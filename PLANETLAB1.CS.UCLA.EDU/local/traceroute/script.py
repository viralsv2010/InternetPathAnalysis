import trparse
from sys import getsizeof
import re
import itertools
import fileinput
input_file = 'data.txt'
with open('traceroute.txt','r') as file1:
	for line in file1:
#		s = line
#		traceroute = trparse.loads(s)
#		hop = traceroute.hops[0]
#		probe= hop.probes[0]
#		print("Probe IP :: " + probe.ip + " Hops :: " + hop + " Probe :: " + probe)
		data = line.split(" ")
		if('traceroute to ' in line):
			node_name = data[2]
		count = data.count("*")
		if(count>= 1 and count <= 3):
			#pattern = re.compile("^\s+|\s*,\s*|\s+$")
			#line1 = [x for x in pattern.split(line) if x]
			#re.sub(r'\s', '', line).split(',')
			#list1 = line.split(',')
			#mylist = line.replace(' ','').split(',')
			#result=[x for x in re.split(',| ',line) if x!='']
			#re.split(', ',line)
			#filter(None, re.split('[, ]',line))
			#map(lambda s:s.strip(), line.split(','))
			#re.sub('\s{2,}', ' ', line)
			line = ' '.join(filter(None,line.split(' ')))
			list1 = line.split(' ')
			#line1 = line.replace(' ',',')
			#my_list = line.split(',')
			print(list1)
			len = list1.__len__()
			print(len)
			if(len > 4):
				if any([list1[3]=='*' and list1[4]=='*',list1[5]=='*' and list1[6]=='*',list1[3]=='*' and list1[6]=='*']):
					if(list1[3]=='*' and list1[4]=='*'):
						open('data.txt','a+').writelines(node_name + ',' + list1[0] + ',' + list1[3] + ',' + list1[4] + ',' +  list1[5] +'\n')
					elif(list1[5]=='*' and list1[6]=='*'):
						open('data.txt','a+').writelines(node_name + ',' + list1[0] + ',' + list1[3] + ',' + list1[5] + ',' +  list1[6] +'\n')
					elif(list1[3]=='*' and list1[6]=='*'):
						open('data.txt','a+').writelines(node_name + ',' + list1[0] + ',' + list1[3] + ',' + list1[4] + ',' +  list1[6] +'\n')
				elif any([list1[3]=='*',list1[5]=='*',list1[len-1]=='*']):
					if(list1[3] == '*'):
						open('data.txt','a+').writelines(node_name + ',' + list1[0] + ',' + list1[3] + ',' + list1[4] + ',' +  list1[6] +'\n')
					elif(list1[5] == '*'):
						open('data.txt','a+').writelines(node_name + ',' + list1[0] + ',' + list1[3] + ',' + list1[5] + ',' + list1[6]+'\n')
					elif(list1[7] == '*'):
						open('data.txt','a+').writelines(node_name + ',' + list1[0] + ',' + list1[3] + ',' + list1[5] + ',' + list1[7]+'\n')
			else:
				open('data.txt','a+').writelines(node_name + ',' + list1[0] + ',' + list1[1] + ',' + list1[2] + ',' + list1[3])
			#for each_line in fileinput.input(input_file):
			#	open('data.txt','a+').write("\n".join(x.strip() for x in each_line.split(',')))




#count = 0
#for line in open("traceroute.txt"):
#    if "TraceRoute   Command     Output" in line: 
#        count += 1
#print(count)









#with open('traceroute.txt','r') as f:
    # skip until we reach `Rank`:
#    itertools.takewhile(lambda l: 'TraceRoute   Command     Output' not in l, f)
    # takewhile will have read a line with `Rank` now
    # count the lines *without* `Rank` between them
 #  count = sum(1 for l in itertools.takewhile(lambda l: 'TraceRoute   Command     Output' not in l, f))
 #   count += 1
  #  open('data.txt','a+').writelines("@@" + count + "@@" + '\n')

#with open('ping.txt','r') as file1:
#	for line in file1:
#		if 'bytes of data.' in line:
#			list2 = line.split(" ")
#		if 'rtt' in line:
#			list1 = line.split(" ")
#			head = (list1)[1].replace("/",",")
#			val = (list1)[3].replace("/",",")
#			open('C:/Users/Viral-PC/area1/data.txt','a+').writelines(list2[1] + ',' + val+ '\n')

