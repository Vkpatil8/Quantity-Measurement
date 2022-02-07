from quantity_measurement import QuantityMeasurement


class Test:

    def test_compare_two_having_zero_values(self):
        """
            desc: check two object using equal method having zero length

        """
        first_obj = QuantityMeasurement("Feet", 0)
        second_obj = QuantityMeasurement("Feet", 0)
        assert first_obj == second_obj
