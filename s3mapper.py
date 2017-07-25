#!usr/bin/env python
import sys
for line in sys.stdin:
	line  = line.strip()
	word = line.split(",")
	state = word[3]
	sales = word[-1]
	print '%s\t%s' % (state,sales)
