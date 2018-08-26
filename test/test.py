import pytest

from app.converter import convert

class TestConverter:

  def test_should_convert_from_1_to_3(self):
    # Given
    numbers = [1,2,3]
    expected = ['I','II','III']

    # When
    result = [convert(number) for number in numbers]

    # Then
    assert expected == result
