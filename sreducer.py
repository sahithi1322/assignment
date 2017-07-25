#/!/usr/bin/python

import sys

total_sales = 0
current_category = None

for line in sys.stdin:
	line = line.strip()
	category,sales = line.split('\t',1)
	sales = float(sales)
	if current_category == category:
		total_sales += sales
	else:
		if current_category != None:
			print '%s\t%s' % (current_category,total_sales)
		current_category = category
		total_sales = sales
if current_category:
	print '%s\t%s' % (current_category,total_sales)

