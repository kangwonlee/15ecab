import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.pardir, 'wk10')))

import linear_algebra as la

n = 1000
A = [[0.0] * n for k in xrange(n)]
A[350][359] = 1.0
A[700][5] = 7.0
A[700][819] = 0.7
A[880][651] = 8.6
A[880][959] = 1.4

w = zip([1.0] * n)

v = la.multiply_matrix_matrix(A, w)

print("len(v) = %d" % len(v))
print("len(v[0]) = %d" % len(v[0]))
print("v[700] = %s" % v[700])
print("v[880] = %s" % v[880])
