## Reference From http://stackoverflow.com/questions/13680769/counting-jumpno-of-lines-between-first-two-string-occurrences-in-a-file

from itertools import groupby

def block_start(line, start=[None]):
    if 'traceroute to' in line:
       start[0] = not start[0]
    return start[0]

with open('traceroute.txt') as file:
     block_sizes = [sum(1 for line in block) # find number of lines in a block
                    for _, block in groupby(file, key=block_start)] # group
open('hopCount.txt','a+').writelines(str(block_sizes))	
#print(block_sizes)