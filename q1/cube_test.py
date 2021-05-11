import unittest
import cube


class test_cube(unittest.TestCase):

    def test_volume_allintegers(self):
        self.assertEqual(cube.volume(3, 3, 3), 27)

    def test_volume_allFloats(self):
        self.assertEqual(cube.volume(2.34, 2.543, 5.3), 31.538286)

    def test_volume_StringSHOULDFAIL(self):
        self.assertRaises(AssertionError, cube.volume, 3,'3', '3a')

    def test_volume_MixNumbers(self):
        self.assertEqual(cube.volume(3, 3, 0.5), 4.5)

    def test_volume_MixNumbers_SHOULDFAIL(self):
        self.assertNotEqual(cube.volume(3, 3, 1.5), 4.5)

    def test_volume_negative_Numbers(self):
      self.assertEqual(cube.volume(3, -3, 3), -27)

if __name__ == '__main__':
    unittest.main()
