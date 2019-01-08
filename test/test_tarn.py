import unittest
import src.tarn as t


class TestTarn(unittest.TestCase):

    def test_tarn_calc(self):
        arr1 = [1, 3, 4, 3, 2, 1, 5, 4, 7, 2, 1, 3, 5, 7]
        arr2 = [1, 2, 3, 1]
        arr3 = [2, 1, 1, 1, 2, 1, 1, 7, 1]
        arr4 = [7, 1, 1, 2, 1, 1, 1, 2, 1]
        print('test_tarn_calc')
        self.assertEqual(t.tarn_calc(arr1), 24)
        self.assertEqual(t.tarn_calc(arr2), 0)
        self.assertEqual(t.tarn_calc(arr3), 5)
        self.assertEqual(t.tarn_calc(arr4), 5)


if __name__ == '__main__':
    unittest.main()