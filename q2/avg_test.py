import unittest
import avg

goodList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
badList = [1, 2, 3, 4, 'a', 6, 7, 8, 9, 10]
emptyList = []
negativeList = [1, 2, -2, 4, -3]


class test_avg(unittest.TestCase):

    def testGoodList(self):
        self.assertEqual(avg.avg(goodList), 5.5)

    def testBadList(self):
        self.assertRaises(AssertionError, avg.avg, badList)

    def testEmptyList(self):
        self.assertEqual(avg.avg(emptyList), 0)

    def testNegativeNumbers(self):
        self.assertEqual(avg.avg(negativeList), 0.4)

    def testSuperLongList(self):
        self.assertEqual(avg.avg(list(range(1, 2001))), 1000.5)


if __name__ == '__main__':
    unittest.main()
