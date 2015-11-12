import math
import sys
try:
    r = int(raw_input("Please enter radius of a circle "))
except ValueError as e:
    print "Invalid radius value"
    print e
    sys.exit(-1)
except IOError as e:
    print "IOError"
    print e
    sys.exit(-1)

area = math.pi * r * r
print area
