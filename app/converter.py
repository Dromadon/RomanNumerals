#-*- coding: utf-8 -*-

NUMERALS_TO_ROMAN = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

def convert(numeral):
  if numeral in NUMERALS_TO_ROMAN.keys():
    return NUMERALS_TO_ROMAN[numeral]

  elif numeral <= 3:
    return 'I'*numeral

  else:
    return 'IV'
