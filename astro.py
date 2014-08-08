import numpy as np

#quantity.py
class Quantity(object):
  def __init__(self, value, numUnits, denUnits):
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

def simplify(qty):
  for x in xrange(0, len(qty.numUnits)):  
    for item in qty.numUnits:
      if item in qty.denUnits:
        qty.numUnits.remove(item)
        qty.denUnits.remove(item)
  qty.put()
    
#units.py
class Units(object):
  def __init__(self, abbr, name, dictionary):
    self.abbr = abbr # unit abbreviation (i.e. 'm')
    self.name = name # unit name (i.e. 'meters')
    self.dictionary = dictionary # dictionary associated (i.e. mDict)

  # The convert() function only works for units that are proportional to each other (i.e. km <==> m). It does not work for non-linear conversions, like K <==> C. Therefore, a special if statement needs to be written in the convert() function to handle that specific conversion. The associated dictionary for K and C should be empty as well.

# # # Mass # # #
kgDict = {
  'kg': 1, 
  'g': 1000, 
  'msun': 1/1989000000000000000000000000000, 
  'mearth': 1/(5976*(10**24))
  }
kg = Units("kg", "kilograms", kgDict)

gDict = {
  'kg': 1/kgDict.get('g'), 
  'g': 1, 
  'msun': (1/kgDict.get('g'))*kgDict.get('msun'),
  'mearth': (1/kgDict.get('g'))*kgDict.get('mearth')
  }
g = Units("g", "grams", gDict)

msunDict = {
  'kg': 1989000000000000000000000000000, 
  'g': 1989000000000000000000000000000000, 
  'msun': 1,
  'mearth': (1989000000000000000000000000000)*kgDict.get('mearth')
  }
msun = Units("msun", "solar mass", msunDict)


mearthDict = {
  'kg': (5976*(10**24)), 
  'g': 1.9891*(10**33), 
  'msun': 3.0024584*(10**-6),
  'mearth': 1
  }
mearth = Units("mearth", "earth mass", mearthDict)

# # # Time # # #
sDict = {
  's': 1, 
  'hrs': (1/3600), 
  'days': (1/86400)
  }
s = Units("s", "seconds", sDict)
  
hrsDict = {
  's': 3600, 
  'hrs': 1, 
  'days': 24
  }
hrs = Units("hrs", "hours", hrsDict)

daysDict = {
  's': 86400, 
  'hrs': 24, 
  'days': 1
  }
days = Units("days", "days", daysDict)

# # # Length # # #
kmDict = {
  'km': 1,
  'm': 1000,
  'AU': 1/149597871,
  'pc': 1/(3.08567758*(10**13)),
  'ly': 1/(9.4605284*(10**12))
  }
km = Units("km", "kilometers", kmDict)

mDict = {
  'km': 0.001,
  'm': 1,
  'AU': (0.001)*(1/149597871),
  'pc': (0.001)*(1/(3.08567758*(10**13))),
  'ly': (0.001)*(1/(9.4605284*(10**12)))
  }
m = Units("m", "meters", mDict)

AUDict = {
  'km': 149597871,
  'm': 1000*149597871,
  'AU': 1,
  'pc': 1/206264.806,
  'ly': 1/63239.7263
  }
AU = Units("AU", "astronomical units", AUDict)

pcDict = {
  'km': (3.08567758*(10**13)),
  'm': (3.08567758*(10**16)),
  'AU': 1/AUDict.get('pc'),
  'pc': 1,
  'ly': 3.26163344
  }
pc = Units("pc", "parsecs", pcDict)

lyDict = {
  'km': (9.4605284*(10**12)),
  'm': (9.4605284*(10**15)),
  'AU': 1/AUDict.get('ly'),
  'pc': 1/pcDict.get('ly'),
  'ly': 1
  }
ly = Units("ly", "light-years", lyDict)
  
# # # Temperature # # #
# Empty dictionary for non linear conversions (should be handled in convert())
KDict = {}
K = Units("K", "Kelvin", KDict)

CDict = {}
C = Units("C", "Celsius", CDict)

FDict = {}
F = Units("F", "Fahrenheit", FDict)

# # # Magnitude # # #
# There is only one unit of magnitude, so the dictionary should be empty.
magDict = {}
mag = Units("mag", "magnitude", magDict)
  
#constants.py

# This is really helpful: http://physics.nist.gov/cuu/Units/units.html

# # # General # # #
bigG = Quantity(6.67384*(10**-11), [m, m, m], [kg, s, s]) #(m^3)/(kg(s^2))
c = Quantity(299792458, [m], [s]) #m/s
hubble = Quantity(67.8/1000000, [km], [s, pc]) #(km/(s*pc))
wien = Quantity(0.0028977721, [m, K], []) #m K
stefan = Quantity((5.670373*(10**-8)), [kg], [s, s, s, K, K, K, K]) #W(m^-2)(K^-4) (converted to base SI units)

# # # Sun # # #
sunCoronaTemp = Quantity(1000000, [K], []) #K
sunChromTemp = Quantity(10000, [K], []) #K
sunPhotoTemp = Quantity(6000, [K], []) #K
sunCoreTemp = Quantity(15000000, [K], []) #K
sunMass = Quantity(1989000000000000000000000000000, [kg], []) #kg
sunRadius = Quantity(695590000, [m], []) #m
# sunDensity = Quantity(1.41, [g], [cm, cm, cm]) #g/cm^3
sunAbsMag = Quantity(4.8, [mag], [])
sunAppMag = Quantity(-26.7, [mag], [])
sunEqRotPeriod = Quantity(25.04, [days], []) #days
sunPoleRotPeriod = Quantity(30, [days], []) #days

# # # Earth # # #
earthMass = Quantity(5976*(10**24), [kg], []) #kg
earthDensity = Quantity(5515, [kg], [m, m, m]) #kg/m^3
earthSurfTemp = Quantity(287, [K], []) #K
earthSurfGrav = Quantity(9.78, [m], [s, s]) #m/s^2
earthRadius = Quantity(6378, [km], []) #km
earthMoonDist = Quantity(384400, [km], []) #km



#convert.py
def convert(q, newNumUnits, newDenUnits):
    a = 1
    b = 1
    for (i, item) in enumerate(newNumUnits):
        a *= getConvFactor(q.numUnits[i], newNumUnits[i])
        # debugging only print "numconvfac = " + str(getConvFactor(q.numUnits[i], newNumUnits[i]))
    for (j, item) in enumerate(newDenUnits):
        b *= getConvFactor(q.denUnits[j], newDenUnits[j])
        # debugging only print "denconvfac = " + str(getConvFactor(q.denUnits[j], newDenUnits[j]))
    
    x = (a*(q.value))/b
    return Quantity(x, newNumUnits, newDenUnits)
    
def getConvFactor(m, n):
    # load dictionaries
    return m.dictionary[n.abbr]


    

#module.py
'''
# # # Catalog # # #
Kepler's law
Distance mod
Planetary temperature** missing some algebra
Escape velocity** missing some algebra
Wien's law
Luminosity & app brightness
'''
def kepler3(period, semimajor, m1, m2, work='true'):
  if period == None:
    convm1 = convert(m1, [kg], [])
    convm2 = convert(m2, [kg], [])
    conva = convert(semimajor, [m], [])
    return Quantity((4*(np.pi**2)*(conva.value**3))/(bigG.value*(convm1.value+convm2.value))**0.5, [s], [])
  elif semimajor == None:
    convperiod = convert(period, [s], [])
    convm1 = convert(m1, [kg], [])
    convm2 = convert(m2, [kg], [])
    return Quantity((((convperiod.value**2)*(bigG.value*(convm1.value+convm2.value))/(4*(np.pi**2)*(conva.value**3)))**0.666666666666666), [m], [])
  elif m1 == None:
    convperiod = convert(period, [s], [])
    convm2 = convert(m2, [kg], [])
    conva = convert(semimajor, [m], [])
    return Quantity(((4*(np.pi**2)*(conva.value**3))/(bigG.value*(convperiod.value**2)))-convm2.value, [kg], [])
  elif m2 == None:
    convperiod = convert(period, [s], [])
    convm1 = convert(m1, [kg], [])
    conva = convert(semimajor, [m], [])
    return Quantity(((4*(np.pi**2)*(conva.value**3))/(bigG.value*(convperiod.value**2)))-convm1.value, [kg], [])

def modulus(d, appmag, absmag, work='true'):
  if d == None:
    return Quantity(10**((0.2*(appmag-absmag))+1), [pc], [])
  elif appmag == None:
    convd = convert(d, [pc], [])
    return Quantity(5*(np.log10(convd.value)-1) + absmag, [mag], [])
  elif absmag == None:
    convd = convert(d, [pc], [])
    return Quantity(appmag - (-5*(np.log10(convd.value)-1)), [mag], [])

def wienslaw(lba, T, work='true'):
  if lba == None:
    return Quantity(wien.value/T.value, [m], [])
  elif T == None:
    return Quantity(wien.value/lba.value [K], [])


