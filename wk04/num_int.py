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