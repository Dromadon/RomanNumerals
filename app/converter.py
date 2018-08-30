#-*- coding: utf-8 -*-

NUMERALS_TO_ROMAN = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
ROMAN_BASE = [1, 5, 10, 50, 100, 500, 1000]
POWER_OF_TEN = [1000, 100, 10, 1]

def convert(numeral):
  if numeral == 0:
    return ""
  if numeral in NUMERALS_TO_ROMAN.keys():
    return NUMERALS_TO_ROMAN[numeral]

  power, quotient = get_quotient_and_power(numeral)

  if power == 1:
    lower_base, upper_base = get_base(numeral)

    if upper_base - numeral == 1:
      return 'I'+NUMERALS_TO_ROMAN[upper_base]
    else:
      if lower_base == 1:
        return 'I'*numeral
      else:
        return NUMERALS_TO_ROMAN[lower_base]+'I'*(numeral-lower_base)
  else:
    return NUMERALS_TO_ROMAN[power]*quotient + convert(numeral - power*quotient)


def get_base(numeral):
  lower_base = max([i for i in ROMAN_BASE if i < numeral])
  upper_base = min([i for i in ROMAN_BASE if i > numeral])
  return lower_base, upper_base

def get_quotient_and_power(numeral):
  power = max([i for i in POWER_OF_TEN if i <= numeral])
  return power, int(numeral/power)
