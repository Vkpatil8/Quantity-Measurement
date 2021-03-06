"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 07-02-2022 12:20:00
@Title : solve use case & testcases for comparing two unit values
"""

import pytest

from feet import Feet
from inch import Inch
from quantity_measurement import QuantityMeasurement
from yard import Yard


class Test:
    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 0.0, Feet.FEET, 0.0), (Inch.INCH, 0.0, Inch.INCH, 0.0),
                              (Yard.YARD, 0.0, Yard.YARD, 0.0)])
    def test_compare_two_having_zero_values(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check two object using equal method having zero length

        """
        first_obj = QuantityMeasurement(first_unit, first_length)
        second_obj = QuantityMeasurement(second_unit, second_length)
        assert first_obj == second_obj

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 0.0, Feet.FEET, 0.0), (Inch.INCH, 3.0, Inch.INCH, 3.0),
                              (Yard.YARD, 6.0, Yard.YARD, 6.0)])
    def test_raise_exception_on_null_value(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check object using equal method having null value in one object and same unit
        """
        first_obj = QuantityMeasurement(first_unit, first_length)
        second_obj = QuantityMeasurement(second_unit, second_length)
        assert first_obj == second_obj

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 1.0, Inch.INCH, 12.0), (Inch.INCH, 12.0, Feet.FEET, 1.0)])
    def test_for_checking_reference(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check object using equal method have same reference
        """
        first_obj = QuantityMeasurement(first_unit, first_length)
        second_obj = first_obj
        assert first_obj == second_obj

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 0.0, Feet.FEET, 0.0), (Inch.INCH, 3, Inch.INCH, 3),
                              (Yard.YARD, 6, Yard.YARD, 6)])
    def test_raise_exception_on_different_type_values(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check object using equal method having type of one object and same unit
        """
        first_obj = QuantityMeasurement(first_unit, first_length)
        second_obj = QuantityMeasurement(second_unit, second_length)
        assert first_obj == second_obj

    @pytest.mark.parametrize('first_unit, first_length, second_unit, second_length',
                             [(Feet.FEET, 1.0, Inch.INCH, 12.0), (Inch.INCH, 12.0, Feet.FEET, 1.0),
                              (Feet.FEET, 3.0, Yard.YARD, 1.0), (Yard.YARD, 1.0, Feet.FEET, 3.0),
                              (Yard.YARD, 1, Inch.INCH, 36)])
    def test_check_equality(self, first_unit, first_length, second_unit, second_length):
        """
            desc: check two object using equal method having value of one object equal to another
        """
        first_obj = QuantityMeasurement(first_unit, first_length)
        second_obj = QuantityMeasurement(second_unit, second_length)
        assert first_obj == second_obj
