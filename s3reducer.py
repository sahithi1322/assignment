#!usr/bin/env python
import sys
total_sales = 0
current_state = None

for line in sys.stdin:
	line = line.strip()
	state,sales = line.split('\t',1)

	if current_state == state:
		total_sales += sales

	else:
		if current_state != None:
			print '%s\t%s' % (current_state,total_sales)
		current_state = state
		total_sales = sales
if current_state:
	print '%s\t%s' % (current_state,total_sales)
