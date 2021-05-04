import unittest
import name

class TestAverage(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(name.make_name("Eduardo", "Gonzalez"), "Eduardo Gonzalez")
        self.assertEqual(name.make_name("Jesus", "Christ"), "Jesus Christ")
        self.assertEqual(name.make_name("John", "Appleseed"), "John Appleseed")

    def test_fail(self):
        with self.subTest(msg="Integers"):
            self.assertEqual(name.make_name(7, 8), "7 8")
        with self.subTest(msg="Integers"):
            self.assertEqual(name.make_name("8", "9"), "8 9")
        with self.subTest(msg="TypeError"):
            self.assertEqual(name.make_name("Marco", 8), "Marco 8")
        with self.subTest(msg="TypeError"):
            self.assertEqual(name.make_name("hello", 10), "hello 10")

if __name__ == "__main__":
    unittest.main()