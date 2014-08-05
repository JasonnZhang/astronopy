import numpy as np

class Quantity(object):
  def __init__(self, value, numUnits, denUnits):
    self.value = value # numerical value
    self.numUnits = numUnits # array of units in the numerator, i.e. {units.kg, units.m, units.m}
    self.denUnits = denUnits # array of units in the denominator, i.e. {units.s, units.s}
  def put(self):
    strNumUnits = ''
    strDenUnits = ''
    for item in numUnits:
      strNumUnits += item
    for item in denUnits:
      strDenUnits += item
      # should probably add something here to concatenate like units (instead of something like 'mm')
    print "%s  %s/%s" % (self.value, self.numUnits, self.denUnits)

