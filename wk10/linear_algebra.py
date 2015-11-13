# -*- coding: cp949 -*-
from pprint import pprint


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

    result = [0.0] * n_row
    for i in xrange(n_row):
        result[i] = dot(A[i], x)

    return result


def multiply_matrix_matrix(A, B):
    n_row = len(A)
    n_column = len(B[0])
    n_dummyA = len(A[0])
    n_dummyB = len(B)

    if n_dummyA != n_dummyB :
        print "matrix size incorrect"
        return None

    result = []
    for i_row in xrange(n_row):
        result_row = [0.0] * n_column
        for j_column in xrange(n_column):
            result_row[j_column] = 0.0
            for k_dummy in xrange(n_dummyA):
                result_row[j_column] += A[i_row][k_dummy] * B[k_dummy][j_column]

        result.append(result_row)

    return result


def gauss_elimination(A, b):
    """
    1�� �ٿ� ���� ������ Ax = b ���� x �� ����
    A: ��� ���
    b: ��� ����
    """

    n_row = len(A)
    n_column = len(A[0])

    # Augmented Matrix �� ����

    Ab = []
    for i_row in xrange(n_row):
        Ab_row = [0.0] * (n_column + 1)
        for j_column in xrange(n_column):
            Ab_row[j_column] = A[i_row][j_column]
        Ab_row[n_column] = b[i_row]
        Ab.append(Ab_row)

    # pivot �ݺ���
    for i_pivot in xrange(n_row):
        # pivot �Ʒ� �� �ݺ���
        for j_row in xrange(i_pivot + 1, n_row):
            ratio = -Ab[j_row][i_pivot] / float(Ab[i_pivot][i_pivot])
            # �� �ݺ���
            for k_column in xrange(n_column + 1):
                Ab[j_row][k_column] += ratio * Ab[i_pivot][k_column]
    # �� �ݺ����� ������ ���� �� �밢�� �Ʒ� ��Ҵ� ��� 0

    pprint(Ab)

    # ��� ���� ���� ����
    x = [0.0] * n_row

    # �������Թ�

    for i_row in xrange(n_row - 1, -1, -1):
        s = Ab[i_row][-1]

        for k_column in xrange(i_row + 1, n_row):
            s -= Ab[i_row][k_column] * x[k_column]

        x[i_row] = s / Ab[i_row][i_row]

    print x

    return x


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

    A_matrix = [[1, 2],
                [3, 4]]
    B_matrix = [[1, 0],
                [0, 1]]

    C_matrix = multiply_matrix_matrix(A_matrix, B_matrix)
    print "A ="
    pprint(A_matrix)
    print "B ="
    pprint(B_matrix)
    print "C ="
    pprint(C_matrix)


if "__main__" == __name__:
    main()
