#-*- coding: utf-8 -*-

NUMERALS_TO_ROMAN = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
ROMAN_BASE = [1, 5, 10, 50, 100, 500, 1000]

def convert(numeral):
  if numeral in NUMERALS_TO_ROMAN.keys():
    return NUMERALS_TO_ROMAN[numeral]

  else:
    lower_base, upper_base = get_base(numeral)

    if upper_base - numeral == 1:
      return 'I'+NUMERALS_TO_ROMAN[upper_base]
    else:
      if lower_base == 1:
        return 'I'*numeral
      else:
        return NUMERALS_TO_ROMAN[lower_base]+'I'*(numeral-lower_base)



def get_base(numeral):
  lower_base = max([i for i in ROMAN_BASE if i < numeral])
  upper_base = min([i for i in ROMAN_BASE if i > numeral])
  return lower_base, upper_base

