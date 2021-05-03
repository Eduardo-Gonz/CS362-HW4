import unittest
import volume

class TestVolume(unittest.TestCase):
    # Passing conditions
    def test_valid(self):
        self.assertEqual(volume.calc_volume(9), 729.0)
        self.assertEqual(volume.calc_volume(8.78), 676.84)
        self.assertEqual(volume.calc_volume("8.78"), 676.84)
    # Failing Conditions
    def test_invalid(self):
        self.assertRaises(ValueError,volume.calc_volume, "hi")
        self.assertRaises(ValueError,volume.calc_volume, "-90adf")
    # Out of Range Conditions
    def test_range(self):
        self.assertEqual(volume.calc_volume(-90), "Enter a number greather than zero.")
        self.assertEqual(volume.calc_volume(0), "Enter a number greather than zero.")


if __name__ == "__main__":
    unittest.main()