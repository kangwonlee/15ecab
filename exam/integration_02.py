def f(x):
    if x < 0 or x > 1:
        result = None
    elif x <= 0.5:
        result = x
    else:
        result = 1.0 - x
    return result


def problem_a():
    x = [i * 0.2 for i in xrange(5)]
    delta_x = x[1] - x[0]
    result = 0.0
    for xk in x:
        Fk = f(xk) * delta_x
        result += Fk
    return result


def problem_b():
    x = [i * 0.2 for i in xrange(6)]
    delta_x = x[1] - x[0]
    result = 0.0
    for k in xrange(5):
        xk = x[k]
        xk1 = x[k + 1]

        Fk = ((f(xk) + f(xk1)) * 0.5) * delta_x
        result += Fk
    return result


def main():
    print("a) = %g" % problem_a())
    print("b) = %g" % problem_b())


if __name__ == '__main__':
    main()
