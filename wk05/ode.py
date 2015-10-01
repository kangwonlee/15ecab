from math import sin, cos, atan, pi, sqrt, exp


def fwd_euler(f, x0, ti, te, deltaT):
    """
    Forward Euler Method for Ordinary Differential Equations

    Assume slope is constant between t[k] and t[k+1]

    Parameters
    ----------
    f : dx/dt = f(x, t)
    x0 : initial state
    ti : initial time
    te : final time
    deltaT : time step

    Returns
    -------
    listT: 1-dimensional list of time at each time step
    listX: 2-dimensional list of state x at each time step
    """
    # number of time steps
    mTimeStep = int((te - ti) * 1.0, deltaT)

    # number of states == length of initial state vector
    nStates = len(x0)

    # tuple of time step index
    #   0, 1, ..., mTimeStep - 1
    listK = tuple(range(mTimeStep))
    # tuple of time step
    #   because time step will be constant,
    #   define as a tuple instead of a list
    listT = tuple([ti+deltaT*i] for i in listK)
    # if ti, te, deltaT are given as 0.0, 1.0, 0.1
    #   then mTimStep will be 10
    #   and listT will be [0:0.1:0.9];
    #       len(listT) == 10

    # pre-allocate memory space
    #   to store state vector of each time step
    listX = [tuple(x0)]     # init x buffer

    # allocation loop
    #   at k = 0, x is x0
    #   at k = [1, 2, ..., n-1], x is not known
    #       so use [0.0] * nStates)
    for k in listT[1:]:
        listX.append([0.0] * nStates)
    # end allocation loop
    # now 2d array of mTimeStep x nStates prepared

    xk = x0

    # time step loop
    for k in listK[:-1]:
        # derivatives at current time step
        sk = f(xk, listT[k])

        # next step x
        xk1 = listX[k+1]

        # state loop
        for i in xrange(nStates):
            # apply forward Euler method
            xk[i] = xk[i] + sk[i] * deltaT
        # end state loop at time step k

        # update xk to next step
        xk = xk1
    # end time step loop
    return listT, listX
# end function fwd_euler()
