# -*- coding: cp949 -*-
# ������: Pedregosa, Fabian. (2015) "Sympy : Symbolic Mathematics in Python", Scipy lecture notes,
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

print '''2.10.1.3'''
x = Symbol('x')
y = Symbol('y')

print "x+y+x-y =", x+y+x-y
print "(x+y)**2 =", (x+y)**2

print '''2.10.2.1'''
print "expand((x+y)**3) =", expand((x+y)**3)

print "expand(x+y, complex=True) =", expand(x+y, complex=True)
print "expand(cos(x+y), trig=True) =", expand(cos(x+y), trig=True)

print '''2.10.2.2'''
print "simplify((x+x*y)/x) =", simplify((x+x*y)/x)

print '''2.10.3.1'''
print "limit(sin(x)/x, x, 0) =", limit(sin(x)/x, x, 0)

print "limit(x, x, oo) =", limit(x, x, oo)
print "limit(1/x, x, oo) =", limit(1/x, x, oo)
print "limit(x**x, x, 0) =", limit(x**x, x, 0)

print '''2.10.3.2'''
print "diff(sin(x), x) =", diff(sin(x), x)
print "diff(sin(2*x), x) =", diff(sin(2*x), x)
print "diff(tan(x), x) =", diff(tan(x), x)

print "limit((tan(x+y) - tan(x))/y, y, 0) =", limit((tan(x+y) - tan(x))/y, y, 0)

print "diff(sin(2*x), x, 1) =", diff(sin(2*x), x, 1)
print "diff(sin(2*x), x, 2) =", diff(sin(2*x), x, 2)
print "diff(sin(2*x), x, 3) =", diff(sin(2*x), x, 3)

print '''2.10.3.3'''
print "series(cos(x), x) =", series(cos(x), x)
print "series(1/cos(x), x) =", series(1/cos(x), x)

# Series ������ ���Ͽ� �׷����� �׸�
import pylab
x_deg = pylab.arange(-90, 90 + 1)
x_rad = pylab.deg2rad(x_deg)
y_cos = pylab.cos(x_rad)
y_series_1 = 1 * pylab.ones_like(x_rad)
y_series_2 = 1 - x_rad**2/2
y_series_3 = 1 - x_rad**2/2 + x_rad**4/24

pylab.plot(x_deg, y_cos, label='cos')
pylab.plot(x_deg, y_series_1, label='series 1')
pylab.plot(x_deg, y_series_2, label='series 2')
pylab.plot(x_deg, y_series_3, label='series 3')
pylab.grid()
pylab.legend(loc=0)
pylab.show()
