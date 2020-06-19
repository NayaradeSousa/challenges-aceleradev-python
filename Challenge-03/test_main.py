"""
*******************************Codenation's Aceleradev Python Challenge 03.*********************************************
Write a test that you can test offline the Dark sky api call and the conversion to celsius offline.
Use the Pytest library and the following data to test the get_temperature function.

lat = -14.235004
lng = -51.92528
temperature = 62
expected = 16

The function to be tested is in the main.py file and the test implementation must be done in the
test_main.py file. The objective of this challenge is that you practice creating unit tests, so
create the tests thinking about the possible scenarios of error and success, so that your tests
can cover the largest number of cases.
************************************************************************************************************************
"""
from unittest.mock import patch
from main import get_temperature
import pytest

# list of expected values for each place (latitude and longitude)
expected_values = [(62, -14.235004, -51.92528, 16), (72, 52.539133, 13.484044, 22), (17, 15.356987, -45.152367, -8)]


@pytest.mark.parametrize('fahrenheit, lat, lng, expected', expected_values)
def test_get_temperature_by_lat_lng(fahrenheit, lat, lng, expected):
    """
    This test create a mock object in Json format and realize tests in the
    'get_temperature' method.
    :param fahrenheit: temperature in Fahrenheit
    :param lat: latitude
    :param lng: longitude
    :param expected: temperature in Celsius
    """
    mock_patcher = patch('main.requests.get')
    temperature = {"currently": {"temperature": fahrenheit}}

    mock_get = mock_patcher.start()
    mock_get.return_value.json.return_value = temperature
    response = get_temperature(lat, lng)
    mock_patcher.stop()

    assert expected == response
