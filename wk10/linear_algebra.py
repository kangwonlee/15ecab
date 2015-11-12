# -*- coding: cp949 -*-


def dot(a, b):
    """
    크기가 같은 두 벡터 a, b의 내적 dot product
    """
    # 벡터 a의 크기
    n = len(a)
    # 벡터 b의 크기는 같을 것이라고 가정한다
    #   (어떤 경우 오류가 발생할 수 있는가?)

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
