"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 06-02-2022 18:00:00
@Title : solve test for comparing two unit values
"""
from measurement_exception import MeasurementException


class QuantityMeasurement:
    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def convert(self, unit, length):
        return unit * length

    def __eq__(self, other):
        if self.length is None or other.length is None:
            raise MeasurementException("Null Value")
        if self.unit != other.unit or other.length != self.length:
            return self.convert(self.unit, self.length) == self.convert(other.unit, other.length)
        if self.unit != other.unit and other.length == self.length:
            raise MeasurementException("Different units don't have same length")
        if type(self.length) != type(other.length):
            raise MeasurementException("Have different type")
        if self.unit == other.unit and other.length == self.length:
            return True
