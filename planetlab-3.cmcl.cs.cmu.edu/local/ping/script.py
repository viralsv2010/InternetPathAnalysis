

#while True:
	#open('C:/Users/Viral-PC/area1/data.txt','a+').writelines([ line for line in open('ping.txt') if 'bytes of data.' in line])
	#open('C:/Users/Viral-PC/area1/data.txt','a+').writelines([ line for line in open('ping.txt') if 'rtt' in line])
	#line for line in open('ping.txt','r')
		#if 'bytes of data.' in line && 'rtt' in line
		#open('data.txt','a+').writelines[line]
	#open('C:/Users/Viral-PC/area1/data.txt','a+').writelines([ line for line in open('ping.txt') if 'rtt' or 'bytes of data.' in line])

with open('ping.txt','r') as file1:
	for line in file1:
		if 'bytes of data.' in line:
			list2 = line.split(" ")
			#open('C:/Users/Viral-PC/area1/data.txt','a+').writelines(line)
			#open('C:/Users/Viral-PC/area1/data.txt','a+').writelines((list1)[1] + '\n')
		if 'rtt' in line:
			#open('C:/Users/Viral-PC/area1/data.txt','a+').writelines(line)
			list1 = line.split(" ")
			#open('C:/Users/Viral-PC/area1/data.txt','a+').writelines((list1)[1]+ '\n')
			#head = (list1)[1].split("/")
			head = (list1)[1].replace("/",",")
			#open('C:/Users/Viral-PC/area1/data.txt','a+').writelines((list1)[3]+ '\n')
			#val = (list1)[3].split("/")
			val = (list1)[3].replace("/",",")
			open('data.txt','a+').writelines(list2[1] + ',' + val+ '\n')

