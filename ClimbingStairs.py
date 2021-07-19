import unittest


class ClimbingStairs(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        elif n == 2:
            return 2

        else:
            return self.climbStairs(self, n - 1) + self.climbStairs(self, n - 2)

class ClimbingStairsTest(unittest.TestCase):
    def test_BaseCase(self):
        n = 1
        self.assertEqual(ClimbingStairs.climbStairs(self, n), 1)

    def test_BaseCase(self):
        n = 2
        self.assertEqual(ClimbingStairs.climbStairs(self, n), 2)

    def test_ThreeStairs(self):
        n = 3
        self.assertEqual(ClimbingStairs.climbStairs(self, n), 3)

    def test_FourStairs(self):
        n = 4
        self.assertEqual(ClimbingStairs.climbStairs(self, n), 5)

    def test_ThreeStairs(self):
        n = 5
        self.assertEqual(ClimbingStairs.climbStairs(self, n), 8)

















