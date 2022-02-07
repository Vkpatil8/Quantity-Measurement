"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 05-02-2022 11:20:00
@Title : Quantity Measurement TDD Problem
"""
from measurement_exception import MeasurementException


class QuantityMeasurement:

    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def __eq__(self, other):
        if self.unit == other.unit and self.length == other.length:
            return True
        raise MeasurementException("Not equal")
