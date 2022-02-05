"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 05-02-2022 22:20:00
@Title : solve test case 1.2
"""
from measurement_exception import MeasurementException


class QuantityMeasurement:
    @staticmethod
    def equalLength(a):

        if a is not None:
            return a
        else:
            raise MeasurementException("Null")

    @staticmethod
    def typeCheck(a, b):
        if type(a) != type(b):
            raise MeasurementException("Not equal")
        return True
