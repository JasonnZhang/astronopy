from quantity import *
from units import *


# Since initUnits() isn't working, I'm going to try initializing units here.


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
    'km': 1/1000,
    'm': 1,
    'AU': (1/1000)*(1/149597871),
    'pc': (1/1000)*(1/(3.08567758*(10**13))),
    'ly': (1/1000)*(1/(9.4605284*(10**12)))
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


























# This is really helpful: http://physics.nist.gov/cuu/Units/units.html



# # # General # # #
bigG = Quantity(6.67384*(10**-11), [m.abbr, m.abbr, m.abbr], [kg.abbr, s.abbr, s.abbr]) #(m^3)/(kg(s^2))
c = Quantity(299792458, [m.abbr], [s.abbr]) #m/s
hubble = Quantity(67.8/1000000, [km.abbr], [s.abbr, pc.abbr]) #(km/(s*pc))
wien = Quantity(0.0028977721, [m.abbr, K.abbr], []) #m K
stefan = Quantity((5.670373*(10**-8)), [kg.abbr], [s.abbr, s.abbr, s.abbr, K.abbr, K.abbr, K.abbr, K.abbr]) #W(m^-2)(K^-4) (converted to base SI units)

# # # Sun # # #
sunCoronaTemp = Quantity(1000000, [K.abbr], []) #K
sunChromTemp = Quantity(10000, [K.abbr], []) #K
sunPhotoTemp = Quantity(6000, [K.abbr], []) #K
sunCoreTemp = Quantity(15000000, [K.abbr], []) #K
sunMass = Quantity(1989000000000000000000000000000, [kg.abbr], []) #kg
sunRadius = Quantity(695590000, [m.abbr], []) #m
sunDensity = Quantity(1.41, [g.abbr], [cm.abbr, cm.abbr, cm.abbr]) #g/cm^3
sunAbsMag = Quantity(4.8, [mag.abbr], [])
sunAppMag = Quantity(-26.7, [mag.abbr], [])
sunEqRotPeriod = Quantity(25.04, [days.abbr], []) #days
sunPoleRotPeriod = Quantity(30, [days.abbr], []) #days

# # # Earth # # #
earthMass = Quantity(5976*(10**24), [kg.abbr], []) #kg
earthDensity = Quantity(5515, [kg.abbr], [m.abbr, m.abbr, m.abbr]) #kg/m^3
earthSurfTemp = Quantity(287, [K.abbr], []) #K
earthSurfGrav = Quantity(9.78, [m.abbr], [s.abbr, s.abbr]) #m/s^2
earthRadius = Quantity(6378, [km.abbr], []) #km
earthMoonDist = Quantity(384400, [km.abbr], []) #km


'''
# # # Constants # # #


sunFlux = 1370 #W/m^2
sunSurfGrav = 27.9 #times Earth's
sunAge = 4570000000 #years
sunOblique = 7.25 #degrees


'''




#Milankovitch cycles - don't know if we need these
