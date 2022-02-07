"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 06-02-2022 13:30:00
@Title : solve test case 1.5
"""

from quantity_measurement import QuantityMeasurement


class Test:

    def test_compare_two_having_zero_values(self):
        """
            desc: check two object using equal method having zero length

        """
        first_obj = QuantityMeasurement("Feet", 0)
        second_obj = QuantityMeasurement("Feet", 0)
        assert first_obj == second_obj

    def test_raise_exception_on_null_value(self):
        """
            desc: check object using equal method having null value in one object and same unit
        """
        first_obj = QuantityMeasurement("Feet", 1)
        second_obj = QuantityMeasurement("Feet", 1)
        assert first_obj == second_obj

    def test_for_checking_reference(self):
        """
            desc: check object using equal method have same reference
        """
        first_obj = QuantityMeasurement("Feet", 0)
        second_obj = first_obj
        assert first_obj == second_obj

    def test_raise_exception_on_different_type_values(self):
        """
            desc: check object using equal method having type of one object and same unit
        """
        first_obj = QuantityMeasurement("Feet", 0.0)
        second_obj = QuantityMeasurement("Feet", 0)
        assert first_obj == second_obj

    def test_raise_exception_on_unequal(self):
        """
            desc: check two object using equal method having value of one object equal to another
        """
        first_obj = QuantityMeasurement("Feet", 1)
        second_obj = QuantityMeasurement("Feet", 1)
        assert first_obj == second_obj


