# # # Mass # # #
kgDict = {
  'kg': 1, 
  'g': 1000, 
  'msun': 1/1989000000000000000000000000000, 
  'mearth': 1/(5976*(10**24))
  }
kg = Units("kg", "kilograms", kgDict, "mass")

gDict = {
  'kg': 1/kgDict.get('g'), 
  'g': 1, 
  'msun': (1/kgDict.get('g'))*kgDict.get('msun'),
  'mearth': (1/kgDict.get('g'))*kgDict.get('mearth')
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
  'hrs': (1/3600), 
  'days': (1/86400)
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
  'AU': 1/149597871,
  'pc': 1/(3.08567758*(10**13)),
  'ly': 1/(9.4605284*(10**12))
  }
km = Units("km", "kilometers", kmDict, "length")

mDict = {
  'km': 0.001,
  'm': 1,
  'AU': (0.001)*(1/149597871),
  'pc': (0.001)*(1/(3.08567758*(10**13))),
  'ly': (0.001)*(1/(9.4605284*(10**12)))
  }
m = Units("m", "meters", mDict, "length")

AUDict = {
  'km': 149597871,
  'm': 1000*149597871,
  'AU': 1,
  'pc': 1/206264.806,
  'ly': 1/63239.7263
  }
AU = Units("AU", "astronomical units", AUDict, "length")

pcDict = {
  'km': (3.08567758*(10**13)),
  'm': (3.08567758*(10**16)),
  'AU': 1/AUDict.get('pc'),
  'pc': 1,
  'ly': 3.26163344
  }
pc = Units("pc", "parsecs", pcDict, "length")

lyDict = {
  'km': (9.4605284*(10**12)),
  'm': (9.4605284*(10**15)),
  'AU': 1/AUDict.get('ly'),
  'pc': 1/pcDict.get('ly'),
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
