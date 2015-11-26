import unittest
import math

import linear_algebra as la
import gauss_jordan as gj
import eigenanalysis as ea


class TestLinearAlgebra(unittest.TestCase):
    def test_dot_01(self):
        a = (1.0, 1.0)
        b = (1.0, 1.0)
        c = la.dot(a, b)
        expected = 2.0

        self.assertSequenceEqual(a, (1.0, 1.0))
        self.assertSequenceEqual(b, (1.0, 1.0))

        self.assertAlmostEqual(c, expected)

    def test_dot_02(self):
        a = [1.0, 1.0]
        b = [1.0, 0.0]
        c = la.dot(a, b)
        expected = 1.0

        self.assertAlmostEqual(c, expected)

    def test_dot_03(self):
        a = [1.0, 1.0]
        b = [0.0, 1.0]
        c = la.dot(a, b)
        expected = 1.0

        self.assertAlmostEqual(c, expected)

    def test_dot_04(self):
        a = [1.0, 2.0, 3.0]
        b = [0.0, 1.0, 0.0]
        c = la.dot(a, b)
        expected = 2.0

        self.assertAlmostEqual(c, expected)

    def test_dot_05(self):
        a = [ 3.0, 4.0]
        b = [-4.0, 3.0]
        c = la.dot(a, b)
        expected = 0.0

        self.assertAlmostEqual(c, expected)

    def test_multiply_matrix_vector_01(self):
        A = [[1.0, 1.0],
             [1.0, 1.0]]
        b = [1.0, 1.0]
        c = la.multiply_matrix_vector (A, b)
        expected = [2.0, 2.0]

        self.assertSequenceEqual(c, expected)

    def test_multiply_matrix_vector_02(self):

        base_angle_deg = 30
        base_angle_rad = math.radians(base_angle_deg)
        b = [math.cos(base_angle_rad), math.sin(base_angle_rad)]

        for angle_deg in xrange(361):
            angle_rad = math.radians(angle_deg)
            cos = math.cos(angle_rad)
            sin = math.sin(angle_rad)
            A = [[cos, -sin],
                 [sin,  cos]]
            c = la.multiply_matrix_vector (A, b)
            expected_angle_deg = angle_deg + base_angle_deg
            expected_angle_rad = math.radians(expected_angle_deg)
            expected = [math.cos(expected_angle_rad), math.sin(expected_angle_rad)]

            self.assertEqual(len(c), len(expected))

            for k in xrange(len(expected)):
                self.assertAlmostEqual(c[k], expected[k])

    def test_multiply_matrix_matrix_01(self):
        A = [[1.0, 1.0],
             [1.0, 1.0]]
        B = [[1.0, -1.0],
             [-1.0, 1.0]]
        C = la.multiply_matrix_matrix(A, B)
        expected = [[0.0, 0.0],
                    [0.0, 0.0]]

        self.assertSequenceEqual(C, expected)

    def test_multiply_matrix_matrix_02(self):

        for angle_deg in xrange(361):
            angle_rad = math.radians(angle_deg)
            cos = math.cos(angle_rad)
            sin = math.sin(angle_rad)
            A = [[cos, -sin],
                 [sin,  cos]]

            angle2_deg = - angle_deg
            angle2_rad = math.radians(angle2_deg)
            cos2 = math.cos(angle2_rad)
            sin2 = math.sin(angle2_rad)
            B = [[cos2, -sin2],
                 [sin2,  cos2]]

            C = la.multiply_matrix_matrix (A, B)
            expected = [[1.0, 0.0],
                        [0.0, 1.0]]

            self.assertEqual(len(C), len(expected))

            for k in xrange(len(expected)):
                self.assertEqual(len(C[k]), len(expected[k]))
                for j in xrange(len(expected[k])):
                    self.assertAlmostEqual(C[k][j], expected[k][j])

    def test_multiply_matrix_matrix_03(self):
        A = [[11, 12, 13],
             [21, 22, 23]]
        B = [[111, 112],
             [121, 122],
             [131, 132]]
        C = la.multiply_matrix_matrix(A, B)

        BT = zip(*B)

        expected = [[la.dot(A[0], BT[0]), la.dot(A[0], BT[1])],
                    [la.dot(A[1], BT[0]), la.dot(A[1], BT[1])]]

        self.assertSequenceEqual(C, expected)

    def test_gauss_elimination_01(self):
        A = [[3, 2, 1],
             [2, 3, 2],
             [1, 2, 3]]

        b = [1, 2, 3]

        x = la.gauss_elimination(A, b)

        expected = [0.0, 0.0, 1.0]

        self.assertSequenceEqual(x, expected)

        self.assertSequenceEqual(A, [[3, 2, 1],
                                     [2, 3, 2],
                                     [1, 2, 3]])

        self.assertSequenceEqual(b, [1, 2, 3])

    def test_gauss_jordan_01(self):
        A = [[3, 2, 1],
             [2, 3, 2],
             [1, 2, 3]]

        A_inverse = gj.gauss_jordan(A)

        result = la.multiply_matrix_matrix(A, A_inverse)

        self.assertEqual(len(A), len(A_inverse))
        for i in xrange(len(A)):
            self.assertEqual(len(A[i]), len(A_inverse[i]))

            for j in xrange(len(A[i])):
                if i == j:
                    self.assertAlmostEqual(result[i][j], 1.0)
                else:
                    self.assertAlmostEqual(result[i][j], 0.0)

    def test_power_method_01(self):
        A = [[3, 2, 1],
             [2, 3, 2],
             [1, 2, 3]]

        lamda, x = ea.power_method(A)

        self.assertGreater(abs(lamda), 0.0)

        Ax = la.multiply_matrix_vector(A, x)

        self.assertEqual(len(A), len(Ax))

        for i in xrange(len(A)):
            self.assertAlmostEqual(Ax[i], lamda*x[i])

    def test_power_method_02(self):
        A = [[3, 2, 1],
             [2, 3, 2],
             [1, 2, 3]]

        lamda, x = ea.power_method(A)

        A_minus_lambda_I = [[3-lamda, 2, 1],
                            [2, 3-lamda, 2],
                            [1, 2, 3-lamda]]

        z = la.multiply_matrix_vector(A_minus_lambda_I, x)

        self.assertEqual(len(A), len(z))

        for i in xrange(len(z)):
            self.assertAlmostEqual(z[i], 0.0)

    def test_power_method_03(self):
        A = [[3, 0.2, 0.1],
             [0, 2, 0.2],
             [0, 0, 1]]

        lamda, x = ea.power_method(A)
        Ax = la.multiply_matrix_vector(A, x)

        self.assertEqual(len(A), len(Ax))

        for i in xrange(len(A)):
            self.assertAlmostEqual(Ax[i], lamda*x[i])

    def test_jacobi_method00(self):
        A = [[-1.0, -0.5, -0.2],
             [-0.5, -2.0, -1.0],
             [-0.2, -1.0, -3.0]]

        lamda1, x1 = ea.jacobi_method (A)
        self.assertEqual(len(A), len(lamda1))
        self.assertEqual(len(A[0]), len(lamda1[0]))
        self.assertEqual(len(A), len(x1))
        self.assertEqual(len(A[0]), len(x1[0]))

        Ax1 = la.multiply_matrix_matrix(A, x1)
        # check A V = Lambda V
        for k_pivot in xrange(len(A)):
            # diagonal term
            lambda_i = lamda1[k_pivot][k_pivot]

            # off diagonal
            for i_row in xrange(len(A)):
                self.assertAlmostEqual(Ax1[i_row][k_pivot],lambda_i * x1[i_row][k_pivot])

        # check VT A V = Lambda
        x1TAx1 = la.multiply_matrix_matrix(zip(*x1), Ax1)

        for i_row in xrange(0, len(A) - 1):
            # check diagonal
            self.assertAlmostEqual(x1TAx1[i_row][i_row], lamda1[i_row][i_row])
            # check off-diagonal
            for j_column in xrange(i_row + 1, len(A)):
                self.assertAlmostEqual(x1TAx1[i_row][j_column], 0.0)


if "__main__" == __name__:
    unittest.main()
