"""
    @Author : vishal patil
    @Date :   05-02-2022
"""


class MeasurementException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
