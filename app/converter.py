#-*- coding: utf-8 -*-

NUMERALS_TO_ROMAN = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
POWER_OF_TEN = [1000, 100, 10, 1]

def convert(numeral):
  if numeral == 0:
    return ""

  power, quotient = get_quotient_and_power(numeral)

  if quotient == 0:
    roman = NUMERALS_TO_ROMAN[power]
  if quotient == 9:
    roman =  NUMERALS_TO_ROMAN[power]+NUMERALS_TO_ROMAN[power*10]
  if 5 <= quotient <= 8:
    roman = NUMERALS_TO_ROMAN[power*5]+NUMERALS_TO_ROMAN[power]*(quotient - 5)
  if quotient == 4:
    roman = NUMERALS_TO_ROMAN[power]+NUMERALS_TO_ROMAN[power*5]
  if 1 <= quotient <= 3:
    roman = NUMERALS_TO_ROMAN[power]*quotient

  return roman + convert(numeral - power*quotient)

def get_quotient_and_power(numeral):
  power = max([i for i in POWER_OF_TEN if i <= numeral])
  return power, int(numeral/power)
