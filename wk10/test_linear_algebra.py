import unittest
import linear_algebra as la


class TestLinearAlgebra(unittest.TestCase):
    def test_dot_01(self):
        a = [1.0, 1.0]
        b = [1.0, 1.0]
        c = la.dot(a, b)
        expected = 2.0

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


if "__main__" == __name__:
    unittest.main()
