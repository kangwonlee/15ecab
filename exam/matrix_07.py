import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.pardir, 'wk10')))

import linear_algebra as la


def main():
    A = [[4.0, -2.0, 0.0],
         [-2.0, 8.0, -6.0],
         [0.0, -6.0, 6.0]]
    b = [0.0, 2.0, 2.0]

    result = la.gauss_elimination(A, b)
    print("result = %s" % result)


if __name__ == '__main__':
    main()
