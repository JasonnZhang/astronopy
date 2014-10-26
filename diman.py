from dictionaries import *
#quantity.py
class Quantity(object):
  def __init__(self, value, numUnits, denUnits=[]):
    self.value = value # numerical value
    self.numUnits = numUnits # array of units in the numerator, i.e. {kg.abbr, m.abbr, m.abbr}
    self.denUnits = denUnits # array of units in the denominator, i.e. {s.abbr, s.abbr}
    for x in xrange(0, len(self.numUnits)):  
      for item in self.numUnits:
        if item in self.denUnits:
          self.numUnits.remove(item)
          self.denUnits.remove(item)
  def put(self):
    strNumUnits = ''
    strDenUnits = ''
    for index, item in enumerate(self.numUnits):
      if index == 0:
        strNumUnits += (item.abbr)
      else:
        strNumUnits += ("*"+item.abbr)
    for index, item in enumerate(self.denUnits):
      if index == 0:
        strDenUnits += (item.abbr)
      else:
        strDenUnits += ("*"+item.abbr)
      # should probably add something here to concatenate like units (instead of something like 'mm')
    print "%s  %s/%s" % (self.value, strNumUnits, strDenUnits)
  ## Quantity math operations
  def simplify(self):
    for x in xrange(0, len(self.numUnits)):  
      for item in self.numUnits:
        if item in self.denUnits:
          self.numUnits.remove(item)
          self.denUnits.remove(item)
    self.put()
  def convert(self, newNumUnits, newDenUnits=[]):
    a = 1
    b = 1
    for (i, item) in enumerate(newNumUnits):
        a *= getConvFactor(self.numUnits[i], newNumUnits[i])
        # debugging only print "numconvfac = " + str(getConvFactor(self.numUnits[i], newNumUnits[i]))
    for (j, item) in enumerate(newDenUnits):
        b *= getConvFactor(self.denUnits[j], newDenUnits[j])
        # debugging only print "denconvfac = " + str(getConvFactor(self.denUnits[j], newDenUnits[j]))
    x = (a*(self.value))/b
    self = Quantity(x, newNumUnits, newDenUnits) 
    self.put()
  def invert(self):
    if self.value != 0:
      inv = Quantity(self.value**-1, self.denUnits, self.numUnits)
    else:
      inv = Quantity(0, self.denUnits, self.numUnits)
    inv.put()
    return inv
  def multiplyBy(self, factor):
    c = Quantity(1, [], [])
    c.value = a.value*b.value
    for f in xrange(len(a.numUnits)):
      c.numUnits.append(a.numUnits[f])
    for g in xrange(len(b.numUnits)):
      c.numUnits.append(b.numUnits[g])
    for h in xrange(len(a.denUnits)):
      c.denUnits.append(a.denUnits[h])
    for j in xrange(len(b.denUnits)):
      c.denUnits.append(b.denUnits[j])
    c.simplify()
    return c

  def divideBy(self, dividend):
    a = self
    b = dividend.invert()
    if(b.value==0):
      print('Cannot divide by zero!')
      return
    else:
      c = Quantity(1, [], [])
      c.value = a.value*b.value
      for f in xrange(len(a.numUnits)):
        c.numUnits.append(a.numUnits[f])
      for g in xrange(len(b.numUnits)):
        c.numUnits.append(b.numUnits[g])
      for h in xrange(len(a.denUnits)):
        c.denUnits.append(a.denUnits[h])
      for j in xrange(len(b.denUnits)):
        c.denUnits.append(b.denUnits[j])
      c.simplify()
      return c
    
#units.py
class Units(object):
  def __init__(self, abbr, name, dictionary, unitType):
    self.abbr = abbr # unit abbreviation (i.e. '_m')
    self.name = name # unit name (i.e. 'meters')
    self.dictionary = dictionary
    self.unitType = unitType

  # The convert() function only works for units that are proportional to each other (i.e. km <==> m). It does not work for non-linear conversions, like K <==> C. Therefore, a special if statement needs to be written in the convert() function to handle that specific conversion. The associated dictionary for K and C should be empty as well.

def ten(p):
  return 10**p



#convert.py
def getConvFactor(m, n):
    # load dictionaries
    return m.dictionary[n.abbr]

def toBaseUnits(value, full_unit_name_plural):
  parsed_input = full_unit_name_plural.upper()
  if parsed_input=='WATTS':
    return Quantity(value, [kg, m, m], [s, s, s])
  elif parsed_input=='JOULES':
    return Quantity(value, [kg, m, m], [s, s])
  elif parsed_input=='NEWTONS':
    return Quantity(value, [kg, m], [s, s, s])
  elif parsed_input=='PASCALS':
    return Quantity(value, [kg], [m, s, s])
  elif parsed_input=='HERTZ':
    return Quantity(value, [], [s])
  else:
    print('Unrecognized! Choose watts, joules, newtons, pascals, or hertz.')
    return
