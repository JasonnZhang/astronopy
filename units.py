class Units(object):
  def __init__(self, abbr, name, dictionary):
    self.abbr = abbr # unit abbreviation (i.e. 'm')
    self.name = name # unit name (i.e. 'meters')
    self.category = category # unit category (i.e. 'length')

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
    msun: gDict.get(kg)*kgDict.get(msun)
    mearth: gDict.get(kg)*kgDict.get(mearth)
    }
  
  msun = Units("msun", "solar mass", msunDict)
  msunDict = {
    kg: 1/kgDict.get(msun), 
    g: 1/gDict.get(msun), 
    msun: 1
    mearth: msunDict.get(kg)*kgDict.get(mearth)
    }
  
  mearth = Units("mearth", "earth mass", mearthDict)
  mearthDict = {
    kg: 1/kgDict.get(mearth), 
    g: 1/gDict.get(mearth), 
    msun: 1/msunDict.get(mearth)
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
  
  
  m = Units("m", "meters", mDict)
  AU = Units("AU", "astronomical units", auDict)
  pc = Units("pc", "parsecs", pcDict)
  ly = Units("ly", "light-years", lyDict)
  
