import numpy as np
#import scipy as sp
import convert as cv
import units as units
units.initUnits()
import constants as cs


# # # General Pythoning Tips # # #
# Don't use fractions. Python hates fractions. Convert to decimal floats.
# You can do functions within functions, a la C2K(K2F(n)).
# 3 is cursed. Use int(pi). (http://xkcd.com/1275/)



#quantity.py
class Quantity(object):
  def __init__(self, value, numUnits, denUnits):
    self.value = value # numerical value
    self.numUnits = numUnits # array of units in the numerator, i.e. {kg.abbr, m.abbr, m.abbr}
    self.denUnits = denUnits # array of units in the denominator, i.e. {s.abbr, s.abbr}
  def put(self):
    strNumUnits = ''
    strDenUnits = ''
    for item in self.numUnits:
      strNumUnits += item
    for item in self.denUnits:
      strDenUnits += item
      # should probably add something here to concatenate like units (instead of something like 'mm')
    print "%s  %s/%s" % (self.value, self.numUnits, self.denUnits)
    
#units.py
class Units(object):
  def __init__(self, abbr, name, dictionary):
    self.abbr = abbr # unit abbreviation (i.e. 'm')
    self.name = name # unit name (i.e. 'meters')
    self.dictionary = dictionary # dictionary associated (i.e. mDict)


# In initUnits(), we define all units and initialize an associated dictionary containing conversions to other units of the same type.

# The convert() function only works for units that are proportional to each other (i.e. km <==> m). It does not work for non-linear conversions, like K <==> C. Therefore, a special if statement needs to be written in the convert() function to handle that specific conversion. The associated dictionary for K and C should be empty as well.

def initUnits():
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
  
#constants.py
# This is really helpful: http://physics.nist.gov/cuu/Units/units.html
initUnits()

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
# sunDensity = Quantity(1.41, [g.abbr], [cm.abbr, cm.abbr, cm.abbr]) #g/cm^3
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


#convert.py
def convert(q, newNumUnits, newDenUnits):
    a = 1
    b = 1
    for (i, item) in enumerate(newNumUnits):
        a *= getConvFactor(q.numUnits[i], newNumUnits[i])
        
    for (j, item) in enumerate(newDenUnits):
        b *= getConvFactor(q.denUnits[j], newDenUnits[j])
    x = (a*q)/b
    return Quantity(x, newNumUnits, newDenUnits)
    
def getConvFactor(m, n):
    # load dictionaries
    return m.dictionary[n]







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

# Kepler's Law (p^2 = a^3)
def kepler3(a='solve',P='solve',work='pls'):
    if a == 'solve' and P!='solve':
        a = P ** (0.66666666666666666)
        print('Orbital radius A = ',a)
        if work == 'pls':
            print("""P^2 = a^3
                    a = P^(2/3)
                    a =""",a)
    elif P == 'solve' and a!='solve':
        P = a ** (1.5)
        print('Period = ',P)
        if work == 'pls':
            print("""P^2 = a^3
                    P = a ** (3/2)
                    P = """,P)
    else:
        print('Syntax:  kepler3(a, p, work)') # Maybe information about the formula can go here.
        
# Distance Modulus   
def modulus(d='solve', appmag='solve', absmag='solve', work='yas'):
    if d == 'solve' and appmag!='solve' and absmag!='solve':
        d = 10 ** (((appmag-absmag)/5)+1)
        print('Distance d in pc = ', d)
        if work == 'yas':
            print("""d = 10^(((m-M)/5)+1)
                    d = """, d)
    elif appmag=='solve' and d!='solve' and absmag!='solve':
        appmag = 5*log(d/10, 10) + absmag
        print('Apparent magnitude m = ', appmag)
        if work == 'yas':
            print("""m = 5log(0.1d)+M
                    m = """, appmag)
    elif absmag == 'solve' and appmag!='solve' and d!='solve':
        absmag = -5*log(d/10, 10) + appmag
        print('Absolute magnitude M = ', absmag)
        if work == 'yas':
            print("""M = -5log(0.1d)+m
                    M = """, absmag)
    else:
        print('Syntax:  modulus(d, appmag, absmag, work)') # Maybe information about the formula can go here.

# Temperature of a planet
# Process: To find the expected temperature of a planet, you need to set the rate of energy radiated by the planet equal to the rate of energy absorbed by the planet. 
def tempOfPlanet(T='solve', L='solve', a='solve', d='solve', work='ofc'):
    if T=='solve' and L!='solve' and a!='solve' and d!='solve':
        fourthroot = (L*(1-a))/(16*cs.stefan*pi)
        T = (fourthroot**0.25)*(d**-0.5)
        print('Temperature T in K = ', T)
        if T > 100 or T < 0:
            print('The planet is most likely not habitable. Liquid water cannot exist at this temperature.')
        if work == 'ofc':
            print("""4(pi)(R^2)(sigma)(T^4) = (pi)(R^2)(Lsun)(1-a)/(4(pi)(d^2))
                    T = ((Lsun(1-a)/16(sigma)(pi))^0.25) * (d^-0.5)
                    T = """, T)
    elif L=='solve' and T!='solve' and a!='solve' and d!='solve':
        #I don't feel like doing the algebra here...
        if work == 'ofc':
            print("work goes here")
    elif a=='solve' and L!='solve' and T!='solve' and d!='solve':
        #Much algebra very tired
        if work == 'ofc':
            print("work goes here")
    elif d=='solve' and L!='solve' and a!='solve' and T!='solve':
        #Lack of paper nearby
        if work == 'ofc':
            print("work goes here")
    else:
        print('Syntax:  tempOfPlant(temperature, luminosity of star, albedo, distance from star, work)') # Maybe information about the formula can go here.

# Escape velocity
def escapeVelocity(v='solve', M='solve', r='solve', work ='mhm'):
    if v=='solve' and M!='solve' and r!='solve':
        v = ((2*cs.bigG*M)/r)**0.5
        print('Escape velocity v in m/s = ', v)
        if work == 'mhm':
            print("""v = sqrt(2GM/r)
                    v = """, v)
    elif M=='solve' and v!='solve' and r!='solve':
        # Lazy again to solve for mass
        if work == 'mhm':
            print("work goes here")
    elif r=='solve' and v!='solve' and M!='solve':
        # 2 algebra 2 function
        if work == 'mhm':
            print("work goes here")
    else:
        print('Syntax:  escapeVeloity(velocity, mass, radius, work)')   

# Wien's Law
def wien(w='solve', T='solve', work='yes'):
    if w=='solve' and T!='solve':
        w = cs.wien/T
        print('Max wavelength lambda in m = ', w)
        if work =='yes':
            print("""lambda = c/T
                    lambda = """, w)
    elif T=='solve' and w!='solve':
        T = cs.wien/w
        print('Temperature T in K = ', T)
        if work == 'yes':
            print("""lambda = c/T
                    T = c/lambda
                    T = """, T)
    else:
        print('Syntax:  wien(max_wavelength, temperature, work)')
        
# Luminosity <==> Apparent Brightness
def lumAppBright(b='solve', L='solve', d='solve', work='hmu'):
    if b=='solve' and L!='solve' and d!='solve':
        b = L/(4*pi*(d**2))
        print('Apparent brightness b in W/m^2 = ', b)
        if work == 'hmu':
            print("""b = L/4*pi*d^2
                    b = """, b)
    elif L=='solve' and b!='solve' and d!='solve':
        L = 4*pi*b*(d**2)
        print('Luminosity L in W = ', L)
        if work == 'hmu':
            print("""b = L/4*pi*d^2
                    L = 4(pi)(b)(d^2)
                    L = """, L)
    elif d=='solve' and b!='solve' and L!='solve':
        d = sqrt(L/(4*pi*b))
        print('Distance d in m = ', d)
        if work == 'hmu':
            print("""b = L/4*pi*d^2
                    d = sqrt(L/(4*pi*b))
                    d = """, d)
    else:
        print('Syntax:  lumAppBright(apparent_brightness, luminosity, distance, work)')
