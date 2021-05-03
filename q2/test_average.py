import unittest
import average

class TestAverage(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(average.calc_avg([5,6,7,8,9]), 7.0)
        self.assertEqual(average.calc_avg([-6,8,9,-10]), 0.25)
        self.assertEqual(average.calc_avg([8,99,1010,39,40]), 239.2)

    def test_fail(self):
        with self.subTest(msg="Empty List"):
            self.assertEqual(average.calc_avg([]), 0)
        with self.subTest(msg="TypeError"):
            self.assertEqual(average.calc_avg(["5", 8, 1, 20]), 34)
        with self.subTest(msg="TypeError"):
            self.assertEqual(average.calc_avg(6), 34)
        with self.subTest(msg="TypeError"):
            self.assertEqual(average.calc_avg("hello"), 0)

if __name__ == "__main__":
    unittest.main()