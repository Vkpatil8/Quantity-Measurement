"""
@Author: Vishal Patil
@Date: 05-02-2022 11-00-00
@Last Modified by: Vishal Patil
@Last Modified time: 05-02-2022 24:00:00
@Title : solve test case 1.4
"""
from measurement_exception import MeasurementException


class QuantityMeasurement:
    @staticmethod
    def compareValue(a):
        if a == 0:
            return 0
        else:
            raise MeasurementException("Not Null")

    @staticmethod
    def equalLength(a):
        if a is None:
            return True
        else:
            raise MeasurementException("Not Null")

    @staticmethod
    def typeCheck(a, b):
        if type(a) == type(b):
            return True
        else:
            raise MeasurementException("Not equal type")

    @staticmethod
    def valueCheck(a, b):
        if a == b:
            return True
        else:
            raise MeasurementException("Not equal values")
