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

  def test_should_convert_4_and_9(self):
    # Given
    numbers = [4, 9]
    expected = ['IV', 'IX']

    # When
    result = [convert(number) for number in numbers]

    # Then
    assert expected == result

  def test_should_convert_direct_numerals(self):
    # Given
    numbers = [1, 5, 10, 50, 100, 500, 1000]
    expected = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    # When
    result = [convert(number) for number in numbers]

    # Then
    assert expected == result

  def test_should_convert_from_6_to_8(self):
    # Given
    numbers = [6, 7, 8]
    expected = ['VI', 'VII', 'VIII']

    # When
    result = [convert(number) for number in numbers]

    # Then
    assert expected == result
