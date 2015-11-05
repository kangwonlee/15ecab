# -*- coding: cp949 -*-
# 참고문헌: Pedregosa, Fabian. (2015) "Sympy : Symbolic Mathematics in Python", Scipy lecture notes,
#   http://www.scipy-lectures.org/advanced/sympy.html (accessed November 05 2015).

from sympy import *

print '''2.10.1.1.'''
a = Rational(1, 2)
print "a =", a
print "a * 2 =", a * 2

print "pi ** 2 =", pi ** 2
print "pi.evalf() =", pi.evalf()
print "(pi+exp(1)).evalf() =", (pi+exp(1)).evalf()

print "oo > 99999 =", oo > 99999
print "oo + 1 =", oo + 1
