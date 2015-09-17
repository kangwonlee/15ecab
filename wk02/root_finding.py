# -*- coding: cp949 -*-
def sequential(f, x0):
    xi = float(x0)
    delta_x = 1e-6
    counter = 0
    while True:
        fi = f(xi)
        if abs(fi) < epsilon:
            break
        xi += delta_x
        counter += 1
    print "seq_counter =", counter
    return xi
# end of sequential()


def bisection(f, xl, xh):
    counter = 0
    while True:
        xn = 0.5 * (xl + xh)

        fxn = f(xn)
        fxh = f(xh)

        if fxn * fxh < 0:
            xl = xn
        else:
            xh = xn
        counter += 1
        if abs(xh - xl) < epsilon:
            break
    print "bis_counter =", counter
    return xn
# end of bisection


def newton(f, df, x0):
    """
    뉴튼 랩슨법
    초기 위치 x0 에서 f(x)를 계산하고 그 절대값이 epsison 보다 작으면 중단
    미분을 이용해 접선의 방정식을 구해 풀면서 전진
    수렴이 빠르나 해를 구하지 못할 때도 있다.
    (docstring)
    """
    xi = float(x0)
    counter = 0
    while True:
        fi = f(xi)
        if abs(fi) < epsilon:
            break
        else:
            xi += (-fi / df(xi))
        counter += 1
    print "nr_counter =", counter
    return xi
# end of Newton Raphson


def func(x):
    return 1.0 * x * x - 2.0
# end of func()
# inspired by Scratch example


def dfunc(x):
    return 2.0 * x
# end of dfunc()
# for later use


# |x| < epsilon == (x = 0)
epsilon = 1e-3

if "__main__" == __name__:
    # initial value
    x0 = "0.01"

    # call sequential method
    x_seq = sequential(func, x0)
    print "x_seq =", x_seq
    print "f(x_seq) =", func(x_seq)

    # call bisection method
    x_bis = bisection(func, 0.01, 2.0)
    print "x_bis =", x_bis
    print "f(x_bis) =", func(x_bis)

    # call Newton Raphson method
    x_nr = newton(func, dfunc, 2.0)
    print "x_nr =", x_nr
    print "f(x_nr) =", func(x_nr)
