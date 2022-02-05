import unittest

from quantity_measurement import QuantityMeasurement


class Test(unittest.TestCase):

    def test_compare_two_having_zero_values(self):
        """
            desc: check two object using equal method having zero length

        """
        expected = 0
        first_obj = QuantityMeasurement.equalLength(0)
        self.assertEqual(first_obj, expected)
