"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 07-02-2022 11:45:00
@Title : solve test case 1.8
"""
from measurement_exception import MeasurementException


class QuantityMeasurement:
    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def __eq__(self, other):
        """
            desc: check two object using equal method
        """
        if self.length is None or other.length is None:
            raise MeasurementException("Null Value")
        if self.unit != other.unit and other.length == self.length:
            raise MeasurementException("Different units don't have same length")
        if type(self.length) != type(other.length):
            raise MeasurementException("Have different type")
        if self.unit == other.unit and other.length == self.length:
            return True
