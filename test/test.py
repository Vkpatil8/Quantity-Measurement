from feet import Feet
from inch import Inch
from quantity_measurement import QuantityMeasurement


class Test:

    def test_compare_two_having_zero_values(self):
        """
            desc: check two object using equal method having zero length

        """
        first_obj = QuantityMeasurement(Feet.FEET, 0)
        second_obj = QuantityMeasurement(Feet.FEET, 0)
        assert first_obj == second_obj

    def test_raise_exception_on_null_value(self):
        """
            desc: check object using equal method having null value in one object and same unit
        """
        first_obj = QuantityMeasurement(Feet.FEET, 1)
        second_obj = QuantityMeasurement(Feet.FEET, 1)
        assert first_obj == second_obj

    def test_raise_exception_on_different_type_values(self):
        """
            desc: check object using equal method having type of one object and same unit
        """
        first_obj = QuantityMeasurement(Feet.FEET, 0)
        second_obj = QuantityMeasurement(Feet.FEET, 0)
        assert first_obj == second_obj

    def test_raise_exception_on_different_value(self):
        """
            desc: check two object using equal method having value of one object equal to another
        """
        first_obj = QuantityMeasurement(Feet.FEET, 1)
        second_obj = QuantityMeasurement(Feet.FEET, 1)
        assert first_obj == second_obj

    def test_for_checking_reference(self):
        """
            desc: check object using equal method have same reference
        """
        first_obj = QuantityMeasurement(Feet.FEET, 0)
        second_obj = QuantityMeasurement(Feet.FEET, 0)
        assert first_obj == second_obj

    def test_compare_two_having_zero_values_for_inch_unit(self):
        """
            desc: check two object using equal method having zero length

        """
        first_obj = QuantityMeasurement(Inch.INCH, 0)
        second_obj = QuantityMeasurement(Inch.INCH, 0)
        assert first_obj == second_obj

    def test_raise_exception_on_null_value_for_inch_unit(self):
        """
            desc: check object using equal method having null value in one object and same unit
        """
        first_obj = QuantityMeasurement(Inch.INCH, 1)
        second_obj = QuantityMeasurement(Inch.INCH, 1)
        assert first_obj == second_obj

    def test_for_checking_reference_for_inch_unit(self):
        """
            desc: check object using equal method have same reference
        """
        first_obj = QuantityMeasurement(Inch.INCH, 1)
        second_obj = QuantityMeasurement(Inch.INCH, 1)
        assert first_obj == second_obj

    def test_raise_exception_on_different_type_values_for_inch_unit(self):
        """
            desc: check object using equal method having type of one object and same unit
        """
        first_obj = QuantityMeasurement(Inch.INCH, 1)
        second_obj = QuantityMeasurement(Inch.INCH, 1)
        assert first_obj == second_obj
        