import copy
class Quantity(object):
  def __init__(self, value, units):
    self.value = value # numerical value
    self.units = units # array of units in the numerator, i.e. [[m, 2], [s, -1]]
    '''for x in xrange(0, len(self.numUnits)):  
      for item in self.numUnits:
        if item in self.denUnits:
          self.numUnits.remove(item)
          self.denUnits.remove(item)'''

      
  def put(self):
    strUnits = ''
    for item in self.units:
      strUnits+=('('+str(item[0].abbr)+'^'+str(item[1])+')')
    print "%s  %s" % (self.value, strUnits)
    
  '''def simplify(self):
    listOfUnits = []
    for entry in self.units:
      if len(entry)==1:
        entry = [entry[0], 1]
    for item1 in self.units:
      for item2 in self.units:
        if item1[0] == item2[0]:
          listOfUnits.append([item1[0], (item1[1]+item2[1])])
    self.units = listOfUnits
  '''
  def convert(self, newUnits):
    print('Ensure dimensional match manually!')
    a = 1
    for (i, item) in enumerate(newUnits):
        a *= (getConvFactor(self.units[i][0], newUnits[i][0])**newUnits[i][1])
    x = (a*(self.value))
    self.value = x
    self.units = newUnits
    self.put()
    
    
  def power(self, power):
    newQty = copy.deepcopy(self)
    for item in newQty.units:
      item[1]=item[1]*power
    #self = Quantity(self.value**power, newUnits)
    newQty.value = newQty.value**power
    return newQty
  def multiplyBy(self, factor):
    a = self
    b = factor
    c = Quantity(1, [])
    c.value = a.value*b.value
    for f in xrange(len(a.units)):
      c.units.append(a.units[f])
    for g in xrange(len(b.units)):
      c.units.append(b.units[g])
    return c
  def divideBy(self, dividend):
    b = copy.deepcopy(dividend)
    b.power(-1)
    return self.multiplyBy(b)
  def add(self, addend):
    #print('Ensure dimensional match manually!')
    a = addend
    a.convert(self.units)
    q = Quantity((self.value)+(a.value), self.units)
    return q
  def subtract(self, subtrahend):
    #print('Ensure dimensional match manually!')
    a = subtrahend
    a.convert(self.units)
    q = Quantity((self.value)-(a.value), self.units)
    return q
  ## end untested stuff
class Units(object):
  def __init__(self, abbr, name, dictionary, unitType):
    self.abbr = abbr # unit abbreviation (i.e. 'm')
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



# # # Mass # # #
kgDict = {
  'kg': 1, 
  'g': 1000, 
  'msun': 1.0/1989000000000000000000000000000, 
  'mearth': 1.0/(5976*(10**24))
  }
kg = Units("kg", "kilograms", kgDict, "mass")

gDict = {
  'kg': 1.0/kgDict.get('g'), 
  'g': 1, 
  'msun': (1.0/kgDict.get('g'))*kgDict.get('msun'),
  'mearth': (1.0/kgDict.get('g'))*kgDict.get('mearth')
  }
g = Units("g", "grams", gDict, "mass")

msunDict = {
  'kg': 1989000000000000000000000000000, 
  'g': 1989000000000000000000000000000000, 
  'msun': 1,
  'mearth': (1989000000000000000000000000000)*kgDict.get('mearth')
  }
msun = Units("msun", "solar mass", msunDict, "mass")


mearthDict = {
  'kg': (5976*(10**24)), 
  'g': 1.9891*(10**33), 
  'msun': 3.0024584*(10**-6),
  'mearth': 1
  }
mearth = Units("mearth", "earth mass", mearthDict, "mass")

# # # Time # # #
sDict = {
  's': 1, 
  'hrs': (1.0/3600), 
  'days': (1.0/86400)
  }
s = Units("s", "seconds", sDict, "time")
  
hrsDict = {
  's': 3600, 
  'hrs': 1, 
  'days': 24
  }
hrs = Units("hrs", "hours", hrsDict, "time")

daysDict = {
  's': 86400, 
  'hrs': 24, 
  'days': 1
  }
days = Units("days", "days", daysDict, "time")

# # # Length # # #
kmDict = {
  'km': 1,
  'm': 1000,
  'AU': 1.0/149597871,
  'pc': 1.0/(3.08567758*(10**13)),
  'ly': 1.0/(9.4605284*(10**12))
  }
km = Units("km", "kilometers", kmDict, "length")

mDict = {
  'km': 0.001,
  'm': 1,
  'AU': (0.001)*(1.0/149597871),
  'pc': (0.001)*(1.0/(3.08567758*(10**13))),
  'ly': (0.001)*(1.0/(9.4605284*(10**12)))
  }
m = Units("m", "meters", mDict, "length")

AUDict = {
  'km': 149597871,
  'm': 1000*149597871,
  'AU': 1,
  'pc': 1.0/206264.806,
  'ly': 1.0/63239.7263
  }
AU = Units("AU", "astronomical units", AUDict, "length")

pcDict = {
  'km': (3.08567758*(10**13)),
  'm': (3.08567758*(10**16)),
  'AU': 1.0/AUDict.get('pc'),
  'pc': 1,
  'ly': 3.26163344
  }
pc = Units("pc", "parsecs", pcDict, "length")

lyDict = {
  'km': (9.4605284*(10**12)),
  'm': (9.4605284*(10**15)),
  'AU': 1.0/AUDict.get('ly'),
  'pc': 1.0/pcDict.get('ly'),
  'ly': 1
  }
ly = Units("ly", "light-years", lyDict, "length")
  
# # # Temperature # # #
# Empty dictionary for non linear conversions (should be handled in convert())
KDict = {}
K = Units("K", "Kelvin", KDict, "temperature")

CDict = {}
C = Units("C", "Celsius", CDict, "temperature")

FDict = {}
F = Units("F", "Fahrenheit", FDict, "temperature")

# # # Magnitude # # #
# There is only one unit of magnitude, so the dictionary should be empty.
magDict = {}
mag = Units("mag", "magnitude", magDict, "magnitude")
