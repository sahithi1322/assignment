#!usr/bin/env/ python

import sys
prev_state = None
prev_category = None
Agg_sales = 0

for line in sys.stdin:
	line = line.strip()
	state,category,sales = line.split('\t')
	sales = float(sales)
	if state == prev_state:
		if category == prev_category:
			Agg_sales += sales
		else: 
			print '%s\t%s\t%s' % (state,prev_category,Agg_sales)
			prev_category = category
			Agg_sales = sales
	else :
		prev_state = state
		prev_category = category
		Agg_sales = sales

		
		
