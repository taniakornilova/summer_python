import sys
import math as m

def read_args(argument):
	num = float(argument)
	if num <= 0:
		print("ln(%g) is illegal" % num)
	else:
		print("ln(%g) = %g" % (num, m.log(num)))

for r in sys.argv[1:]:
	read_args(r)
