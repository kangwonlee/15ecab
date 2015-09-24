#from math module, import exp() function
from math import exp

def rect0(f, x0, x1, n=100):
    """
    Numerical integration

    Assume f(x) is a constant between x[k] and x[k+1]

    Parameters
    ----------
    f:function to be integrated
    x0:lower bound of integration
    x1:upper bound of integration
    n:number of intervals

    Return:
    ------
    Numerical integration of function f(x) in interval [x0, x1]
    """
    # calculate x interval
    delta_x = (float(x1) - float(x0)) / n

    # generate list x
    # k = 0, 1, 2, ..., (n-1)
    # list of mid point of each rectangle
    x = [x0 + delta_x * (0.5 + k ) for k in xrange(n)]

    # integration result
    result = 0.0

    # k loop
    # k = 0, 1, 2, ..., (n-1)
    for k in xrange(n):
        # k-th x
        xk = x[k]
        # k-th area
        F_k = f(xk) * delta_x
        # accumulate to integration result
        result += F_k
    # end k loop

    # return integration result
    return result
# end of function rect0()


def trapezoid1(f, x0, x1, n=100):
    """
    Numerical integration

    Assume f(x) is a straight line between x[k] and x[k+1]

    Parameters
    ----------
    f:function to be integrated
    x0:lower bound of integration
    x1:upper bound of integration
    n:number of intervals

    Return:
    ------
    Numerical integration of function f(x) in interval [x0, x1]
    """
    # initialization
    # calculate x interval
    delta_x = (float(x1) - float(x0)) / n

    xk = x0
    fxk = f(xk)

    # integration result
    result = 0.0

    # for each interval
    # k = 0, 1, 2, ..., (n-1)
    for k in xrange(n):
        # k+1-th x
        xk1 = xk + delta_x
        # k+1-th f(x)
        fxk1 = f(xk1)
        # k-th area
        F_k = (fxk + fxk1) * delta_x * 0.5
        # accumulate to integration result
        result += F_k
        xk = xk1
        fxk = fxk1
    # end k loop

    # return integration result
    return result
# end of function trapezoid1()


def simpson2(f, x0, x1, n=100):
    """
    Numerical integration

    Assume f(x) is a 2nd order polynomial between x[k] and x[k+2]

    Parameters
    ----------
    f:function to be integrated
    x0:lower bound of integration
    x1:upper bound of integration
    n:number of intervals

    Return:
    ------
    Numerical integration of function f(x) in interval [x0, x1]
    """
    # initialization
    # calculate x interval
    # if n is an odd number make it an even number
    if (n%2) : n += 1
    delta_x = (float(x1) - float(x0)) / n

    xk = x0
    fxk = f(xk)

    # integration result
    result = 0.0

    # for each two-interval
    # k = 0, 2, 4, ..., (n-1)
    for k in xrange(0, n, 2):
        # k+1-th x
        xk1 = xk + delta_x
        # k+1-th f(x)
        fxk1 = f(xk1)

        # k+2-th x
        xk2 = xk1 + delta_x
        # k+2-th f(x)
        fxk2 = f(xk2)

        # k-th area
        F_k = (fxk + 4*fxk1 + fxk2) * (delta_x / 3.0)

        # accumulate to integration result
        result += F_k
        xk = xk2
        fxk = fxk2
    # end k loop

    # return integration result
    return  result
# end of function simpson2()


def func(x):
    return exp(x)
# end of function func()


def Func(x):
    return exp(x)
# end of function Func()


