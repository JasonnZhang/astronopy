# Okay so this module is completely experimental. I want to see if I can make the units conversion code more lightweight and pretty by using graph theory. If it works, I'll merge this into the astro.py main module.

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

def simplify(qty):
  for x in xrange(0, len(qty.numUnits)):  
    for item in qty.numUnits:
      if item in qty.denUnits:
        qty.numUnits.remove(item)
        qty.denUnits.remove(item)
  qty.put()
    
#units.py
class Units(object):
  def __init__(self, abbr, name, unitType):
    self.abbr = abbr # unit abbreviation (i.e. 'm')
    self.name = name # unit name (i.e. 'meters')
    self.unitType = unitType

km = Units("km", "kilometers", "length")
m = Units("m", "meters", "length")
AU = Units("AU", "astronomical units", "length")
pc = Units("pc", "parsecs", "length")
ly = Units("ly", "light-years", "length")



def shortestPath(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


# Length

lengthLinkGraph = {'m': 'km', 'km': 'AU', 'AU': 'ly', 'ly': 'pc', 'pc': 'm'}
lengthFactorGraph = {'m': 0.001, 'km': 6.68458712*(10**-9), 'AU': 1.58128451*(10**-5), 'ly': 0.306594845, 'pc': 3.08567758*(10**16)}

def getConvFactor(lengthLinkGraph, start, end):
  factor = 1
  for node in shortestPath(lengthLinkGraph, start.abbr, end.abbr): # replace start and end with start unit &nd end unit
    factor *= lengthFactorGraph.get(node)
  return factor


