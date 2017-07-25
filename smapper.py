#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(",")
	category = data[2]
	sales = data[4]
	print '%s\t%s' %(category,sales)
	
	
	
		

