from quantity_measurement import QuantityMeasurement


class Test:

    def test_compare_two_having_zero_values(self):
        """
            desc: check two object using equal method having zero length

        """
        first_obj = QuantityMeasurement("Feet", 0)
        second_obj = QuantityMeasurement("Feet", 0)
        assert first_obj == second_obj

    def test_raise_exception_on_not_null_value(self):
        """
            desc: check object using equal method having null value in one object and same unit
        """

        first_obj = QuantityMeasurement("Feet", 0)
        second_obj = QuantityMeasurement("Feet", 0)
        assert first_obj == second_obj

    def test_raise_exception_on_different_reference(self):
        """
            desc: check two object using equal method having type of one object equal to another
        """
        first_obj = QuantityMeasurement("Feet", 0)
        second_obj = first_obj
        assert first_obj == second_obj
