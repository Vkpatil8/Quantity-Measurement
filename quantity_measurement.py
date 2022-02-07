"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 07-02-2022 12:20:00
@Title : solve use case & testcases for comparing two unit values
"""
from measurement_exception import MeasurementException


class QuantityMeasurement:
    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def convert(self, unit, length):
        """
           desc: convert values from one unit to another unit
        """
        return unit * length

    def __eq__(self, other):
        """
           desc: check two object using equal method
        """
        if other.length is None:
            raise MeasurementException("Null")
        if self.unit != other.unit or other.length != self.length:
            return self.convert(self.unit, self.length) == self.convert(other.unit, other.length)
        if self.unit != other.unit and other.length == self.length:
            raise MeasurementException("Different units don't have same length")
        if self.length != other.length:
            raise MeasurementException("Values are different")
        if type(self.length) != type(other.length):
            raise MeasurementException("Have different type")
        if self.unit == other.unit and other.length == self.length:
            return True
