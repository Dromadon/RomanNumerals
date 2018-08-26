#-*- coding: utf-8 -*-

NUMERALS_TO_ROMAN = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
ROMAN_BASE = [1, 5, 10, 50, 100, 500, 1000]

def convert(numeral):
  if numeral in NUMERALS_TO_ROMAN.keys():
    return NUMERALS_TO_ROMAN[numeral]

  elif numeral == 4:
    return 'IV'

  else:
    base = get_base(numeral)
    if base == 1:
      return 'I'*numeral
    else:
      return NUMERALS_TO_ROMAN[base]+'I'*(numeral-base)



def get_base(numeral):
  lower_base = max([i for i in ROMAN_BASE if i < numeral])
  return lower_base

