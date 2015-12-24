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


def main():
    triangle = pascal(20)
    for i, row in enumerate(triangle):
        print('%2d %s' % (i + 1, row))


if __name__ == '__main__':
    main()
