"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 07-02-2022 11:30:00
@Title : solve test case 1.3
"""
from measurement_exception import MeasurementException


class QuantityMeasurement:

    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def __eq__(self, other):
        if self.unit == other.unit and self.length != other.length:
            raise MeasurementException("Not equal")
        if self.unit is None and other.length is None:
            raise MeasurementException("Null Value")
        return True


