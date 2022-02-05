
import pytest

from measurement_exception import MeasurementException
from quantity_measurement import QuantityMeasurement


class Test:

    def test_compare_two_having_zero_values(self):
        """
            desc: check two object using equal method having zero length

        """
        expected = 0
        first_obj = QuantityMeasurement.equalLength(0)
        assert first_obj == expected

    def test_raise_exception_on_null_value(self):
        """
            desc: check two object using equal method having null value in one object and same unit
        """
        with pytest.raises(MeasurementException) as exception:
            expected = None
            first_obj = QuantityMeasurement.equalLength(None)
            first_obj == expected
        assert exception.value.message == "Null"


