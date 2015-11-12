import unittest
import math

import linear_algebra as la


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


if "__main__" == __name__:
    unittest.main()
