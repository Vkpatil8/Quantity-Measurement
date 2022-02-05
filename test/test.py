
from quantity_measurement import QuantityMeasurement


class Test:

    def test_compare_two_having_zero_values(self):
        """
            desc: check two object using equal method having zero length

        """
        expected = 0
        first_obj = QuantityMeasurement.compareValue(0)
        assert first_obj == expected

    def test_raise_exception_on_not_null_value(self):
        """
            desc: check object using equal method having null value in one object and same unit
        """
        expected = True
        first_obj = QuantityMeasurement.equalLength(None)
        assert first_obj == expected

    def test_raise_exception_on_different_type(self):
        """
            desc: check two object using equal method having type of one object equal to another
        """
        first_obj = QuantityMeasurement.typeCheck("a", "a")
        expected = True
        assert first_obj == expected

    def test_raise_exception_on_different_value(self):
        """
            desc: check two object using equal method having value of one object equal to another
        """
        first_obj = QuantityMeasurement.valueCheck("a", "a")
        expected = True
        assert first_obj == expected
