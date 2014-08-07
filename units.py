from quantity import *

class Units(object):
  def __init__(self, abbr, name, dictionary):
    self.abbr = abbr # unit abbreviation (i.e. 'm')
    self.name = name # unit name (i.e. 'meters')
    self.category = category # unit category (i.e. 'length')


# In initUnits(), we define all units and initialize an associated dictionary containing conversions to other units of the same type.

# The convert() function only works for units that are proportional to each other (i.e. km <==> m). It does not work for non-linear conversions, like K <==> C. Therefore, a special if statement needs to be written in the convert() function to handle that specific conversion. The associated dictionary for K and C should be empty as well.

def initUnits():
  # # # Mass # # #
  kg = Units("kg", "kilograms", kgDict)
  kgDict = {
    kg: 1, 
    g: 1000, 
    msun: 1/1989000000000000000000000000000, 
    mearth: 1/(5976*(10**24))
    }
  
  g = Units("g", "grams", gDict)
  gDict = {
    kg: 1/kgDict.get(g), 
    g: 1, 
    msun: gDict.get(kg)*kgDict.get(msun),
    mearth: gDict.get(kg)*kgDict.get(mearth)
    }
  
  msun = Units("msun", "solar mass", msunDict)
  msunDict = {
    kg: 1/kgDict.get(msun), 
    g: 1/gDict.get(msun), 
    msun: 1,
    mearth: msunDict.get(kg)*kgDict.get(mearth)
    }
  
  mearth = Units("mearth", "earth mass", mearthDict)
  mearthDict = {
    kg: 1/kgDict.get(mearth), 
    g: 1/gDict.get(mearth), 
    msun: 1/msunDict.get(mearth),
    mearth: 1
    }
  
  # # # Time # # #
  s = Units("s", "seconds", sDict)
  sDict = {
    s: 1, 
    hrs: (1/3600), 
    days: (1/86400)
    }
    
  hrs = Units("hrs", "hours", hrsDict)
  hrsDict = {
    s: 3600, 
    hrs: 1, 
    days: 24
    }
  
  days = Units("days", "days", daysDict)
  daysDict = {
    s: 86400, 
    hrs: 24, 
    days: 1
    }
  
  # # # Length # # #
  km = Units("km", "kilometers", kmDict)
  kmDict = {
    km: 1,
    m: 1000,
    AU: 1/149597871,
    pc: 1/(3.08567758*(10**13)),
    ly: 1/(9.4605284*(10**12))
    }
  
  m = Units("m", "meters", mDict)
  mDict = {
    km: 1/1000,
    m: 1,
    AU: (1/1000)(1/149597871),
    pc: (1/1000)(1/(3.08567758*(10**13))),
    ly: (1/1000)(1/(9.4605284*(10**12)))
    }
  
  AU = Units("AU", "astronomical units", AUDict)
  AUDict = {
    km: 1/kmDict.get(AU),
    m: 1000/kmDict.get(AU),
    AU: 1,
    pc: 1/206264.806,
    ly: 1/63239.7263
    }
  
  pc = Units("pc", "parsecs", pcDict)
  pcDict = {
    km: 1/kmDict.get(pc),
    m: 1/mDict.get(pc),
    AU: 1/AUDict.get(pc),
    pc: 1,
    ly: 3.26163344
    }
  ly = Units("ly", "light-years", lyDict)
  lyDict = {
    km: 1/kmDict.get(ly),
    m: 1/mDict.get(ly),
    AU: 1/AUDict.get(ly),
    pc: 1/pcDict.get(ly),
    ly: 1
    }
    
  # # # Temperature # # #
  # Empty dictionary for non linear conversions (should be handled in convert())
  K = Units("K", "Kelvin", KDict)
  KDict = {}
  
  C = Units("C", "Celsius", CDict)
  CDict = {}
  
  F = Units("F", "Fahrenheit", FDict)
  FDict = {}
  
  # # # Magnitude # # #
  # There is only one unit of magnitude, so the dictionary should be empty.
  mag = Units("mag", "magnitude", magDict)
  magDict = {}

