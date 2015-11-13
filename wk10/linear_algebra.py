# -*- coding: cp949 -*-


def dot(a, b):
    """
    ũ�Ⱑ ���� �� ���� a, b�� ���� dot product
    """
    # ���� a�� ũ��
    n = len(a)
    # ���� b�� ũ��� ���� ���̶�� �����Ѵ�
    #   (� ��� ������ �߻��� �� �ִ°�?)

    result = 0.0
    for i in xrange(n):
        result += a[i] * b[i]
    return result


def multiply_matrix_vector(A, x):
    n_row = len(A)
    n_column = len(A[0])

    result = [0.0] * n_row
    for i in xrange(n_row):
        result[i] = dot(A[i], x)

    return result


def main():
    a_vector = [1.0, 0.0]
    b_vector = [3.0, 4.0]
    a_dot_b = dot(a_vector, b_vector)

    print "a =", a_vector
    print "b =", b_vector
    print ("a dot b =", a_dot_b)

    A_matrix = [[0.0, 1.0],
                [1.0, 0.0]]
    x_vector = [3.0, 4.0]
    A_x = multiply_matrix_vector(A_matrix, x_vector)
    print "A :"
    from pprint import pprint
    pprint(A_matrix, width=20)
    print "x =", x_vector
    print "A*x =", A_x


if "__main__" == __name__:
    main()
