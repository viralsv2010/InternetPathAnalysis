#!/bin/bash
cat nodelist.txt | \
	while read CMD; 
	do
		echo $CMD
		now=$(date +"%m_%d_%Y")
		mkdir /c/Users/Viral-PC/data_script/$CMD/$now/
		scp -r albany_ccnS17_1@$CMD:/home/albany_ccnS17_1/viral ./$CMD/$now/
	done
