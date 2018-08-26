import pytest

from app.converter import convert

class TestConverter:

  def test_should_convert_1_to_I(self):
    # Given
    number = 1
    expected = 'I'

    # When
    result = convert(number)

    # Then
    assert expected == result
