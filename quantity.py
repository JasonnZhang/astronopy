import numpy as np

class Quantity(object):
  def __init__(self, value, numUnits, denUnits):
    self.value = value # numerical value
    self.numUnits = numUnits # array of units in the numerator, i.e. {kg.abbr, m.abbr, m.abbr}
    self.denUnits = denUnits # array of units in the denominator, i.e. {s.abbr, s.abbr}
  def put(self):
    strNumUnits = ''
    strDenUnits = ''
    for item in self.numUnits:
      strNumUnits += item
    for item in self.denUnits:
      strDenUnits += item
      # should probably add something here to concatenate like units (instead of something like 'mm')
    print "%s  %s/%s" % (self.value, self.numUnits, self.denUnits)

class Units(object):
  def __init__(self, abbr, name, category):
    self.abbr = abbr # unit abbreviation (i.e. 'm')
    self.name = name # unit name (i.e. 'meters')
    self.category = category # unit category (i.e. 'length')


