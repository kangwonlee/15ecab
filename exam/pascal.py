def pascal(n):
    """
    calculate Pascal's triangle of n rows
    :param n:
    :return: list of list of Pascal's triangle
    """

    result = [[1, 1]]
    for row in xrange(2, n + 1):
        previous_row = result[-1]
        new_row = [0] * (row + 1)
        new_row[0] = new_row[-1] = 1
        for column in xrange(1, row):
            new_row[column] = previous_row[column - 1] + previous_row[column]
        result.append(new_row)

    return result


def pascal_matrix():
    p = [[0.0]*20 for k in xrange(20)]
    for i in xrange(20):
        p[i][1] = 1.0
        p[i][i] = 1.0
    for i in xrange(18):
        a = i + 2
        for k in xrange(19):
            b = k + 1
            p[a][b] = p[a-1][b-1] + p[a-1][b]
    return p


def main():
    triangle = pascal(20)
    rect = pascal_matrix()
    for i, row in enumerate(triangle):
        print('%2d %s' % (i + 1, row))
        print('%2d %s' % (i + 1, rect[i]))


if __name__ == '__main__':
    main()
