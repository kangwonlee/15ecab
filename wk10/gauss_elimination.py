# -*- coding: cp949 -*-
import linear_algebra as la
from pprint import pprint


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
    A = [[3, 2, 1],
         [2, 3, 2],
         [1, 2, 3]]
    b = [1,
         2,
         3]

    x = gauss_elimination(A, b)

    Ax = la.multiply_matrix_vector(A, x)
    print Ax, '==', b


if "__main__" == __name__:
    main()
