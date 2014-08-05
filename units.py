class Units(object):
  def __init__(self, abbr, name, category):
    self.abbr = abbr # unit abbreviation (i.e. 'm')
    self.name = name # unit name (i.e. 'meters')
    self.category = category # unit category (i.e. 'length')

def initUnits():
  # # # Mass # # #
  kg = Units("kg", "kilograms", "mass")
  g = Units("g", "grams", "mass")
  msun = Units("msun", "solar mass", "mass")
  mearth = Units("mearth", "earth mass", "mass")
  
  # # # Length # # #
  km = Units("km", "kilometers", "length")
  m = Units("m", "meters", "length")
  AU = Units("AU", "astronomical units", "length")
  pc = Units("pc", "parsecs", "length")
  ly = Units("ly", "light-years", "length")
  
  # # # Time # # #
  s = Units("s", "seconds", "time")
  hrs = Units("hrs", "hours", "time")
  days = Units("days", "days", "time")
