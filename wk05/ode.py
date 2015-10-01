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
    mTimeStep = int((te - ti) * 1.0 / deltaT)

    # number of states == length of initial state vector
    nStates = len(x0)

    # tuple of time step index
    #   0, 1, ..., mTimeStep - 1
    listK = tuple(range(mTimeStep))
    # tuple of time step
    #   because time step will be constant,
    #   define as a tuple instead of a list
    listT = tuple(ti + deltaT * i for i in listK)
    # if ti, te, deltaT are given as 0.0, 1.0, 0.1
    #   then mTimStep will be 10
    #   and listT will be [0:0.1:0.9];
    #       len(listT) == 10

    # pre-allocate memory space
    #   to store state vector of each time step
    listX = [tuple(x0)]  # init x buffer

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
        xk1 = listX[k + 1]

        # state loop
        for i in xrange(nStates):
            # apply forward Euler method
            xk1[i] = xk[i] + sk[i] * deltaT
        # end state loop at time step k

        # update xk to next step
        xk = xk1
    # end time step loop
    return listT, listX
# end function fwd_euler()


tau = 0.5
m_kg = 10.0
c = 100.0
k = 1000.0


def func(xk, tk):
    """
    Differential equation

    m x2dot(t) + c xdot(t) + k x(t) = u(t)
    u(t) = 1

    Use m, c, k defined outside of this function
    Parameters
    ----------
    xk : state vector at time step k
         xk[0] = x
         xk[1] = xdot
    tk : time at time step k

    Returns
    -------
    xdot : list of derivatives
    """
    # step input
    u = 1

    y1 = xk[0]
    y2 = xk[1]

    y1dot = y2
    y2dot = (u - (k * y1 + c * y2)) / m_kg

    return (y1dot, y2dot)
# end function func()


def exact(t):
    """
    Exact solution of a 1-DOF mechanical vibration
    Ref : Rao, Mechanical Vibration, 2nd ed,
        ISBN 0-201-55693-6, Example 4.3
    """
    # step input
    u = 1
    # natural frequency (rad/sec)
    wn = sqrt(k / m_kg)
    # damping ratio
    zeta = c / (2.0 * m_kg * wn)

    s = sqrt(1.0 - zeta * zeta)
    s1 = 1.0 / s

    # damped frequency (rad/sec)
    wd = wn * s
    # phase (rad)
    phi = atan(zeta * s)

    y1 = (u / k) * (1.0 - s1 * exp(-zeta * wn * t) * cos(wd * t - phi))

    return y1
# end function exact


if "__main__" == __name__:
    help(fwd_euler)

    ti_sec = 0.0
    te_sec = 2.0
    delta_T_sec = 0.01
    x0 = (0.0, 0.0)
    vT, vX = fwd_euler(func, x0, ti_sec, te_sec, delta_T_sec)
    delta_T_sec = 0.001
    vT01, vX01 = fwd_euler(func, x0, ti_sec, te_sec, delta_T_sec)

    # exact solution
    vXexact = tuple([exact(tk) for tk in vT])

    import pylab

    pylab.plot(vT, vX, label='fwd Euler (0.01)')
    pylab.plot(vT01, vX01, label='fwd Euler (0.001)')
    pylab.plot(vT, vXexact, 'k', label='exact')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('x')
    pylab.xlabel('t')
    pylab.show()

    vP, vV = zip(*vX)
    vP01, vV01 = zip(*vX01)

    pylab.plot(vP, vV, label='fwd Euler (0.01)')
    pylab.plot(vP01, vV01, label='fwd Euler (0.001)')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('xdot')
    pylab.xlabel('x')
    pylab.show()
