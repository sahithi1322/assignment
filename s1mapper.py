#!usr/bin/env python

import sys
for line in sys.stdin:
	line = line .strip()
	words = line.split(",")
	state = words[-2]
	category = words[-3]
	sales = words[-1]
	print '%s\t%s\t%s' % (state,category,sales)
