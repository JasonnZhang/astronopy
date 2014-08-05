import numpy as np

class Quantity(object):
  def __init__(self, value, numUnits, denUnits):
    self.value = value
    self.numUnits = numUnits
    self.denUnits = denUnits
  def put(self):
    print "%s  %s/%s" % (self.value, self.numUnits, self.denUnits)
  
