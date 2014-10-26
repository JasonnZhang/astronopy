import numpy as np
import scipy as sp
from diman import *
from dictionaries import *

# # # General # # #
bigG = Quantity(6.67384*ten(-11), [m, m, m], [kg, s, s]) #(m^3)/(kg(s^2))
c = Quantity(299792458, [m], [s]) #m/s
hubble = Quantity(67.8/1000000, [km], [s, pc]) #(km/(s*pc))
wien = Quantity(0.0028977721, [m, K], []) #m K
stefan = Quantity((5.670373*ten(-8)), [kg], [s, s, s, K, K, K, K]) #W(m^-2)(K^-4) (converted to base SI units)

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
sunLuminosity = Quantity(3.846*ten(26), [kg, m, m], [s, s, s]) #watts

# # # Earth # # #
earthMass = Quantity(5976*ten(24), [kg], []) #kg
earthDensity = Quantity(5515, [kg], [m, m, m]) #kg/m^3
earthSurfTemp = Quantity(287, [K], []) #K
earthSurfGrav = Quantity(9.78, [m], [s, s]) #m/s^2
earthRadius = Quantity(6378, [km], []) #km
earthMoonDist = Quantity(384400, [km], []) #km


def kepler3(period, semimajor, m1, m2):
  period.convert([s], [])
  semimajor.convert([m], [])
  m1.convert([kg], [])
  m2.convert([kg], [])






















#############################################################
#stellar classdefs
class Binary(object):
    def __init__(self, stars=[]):
        self.stars = stars
    def calcMass1(self):
        if(self.stars[0].mass==None):
            self.stars[0].mass = self.stars[1].mass*self.stars[1].rad_vel/self.stars[0].rad_vel
        print("Mass = " + str(self.stars[0].mass))
    def calcRadVel1(self):
        if(self.stars[0].rad_vel==None):
            self.stars[0].rad_vel = sself.tars[1].mass*self.stars[1].rad_vel/self.stars[0].mass
    def calcMass2(self):
        if(self.stars[1].mass==None):
            self.stars[1].mass = self.stars[0].mass*self.stars[0].rad_vel/self.stars[1].rad_vel
        print("Mass = " + str(self.stars[1].mass))
    def calcRadVel2(self):
        if(self.stars[1].rad_vel==None):
            self.stars[1].rad_vel = self.stars[0].mass*self.stars[0].rad_vel/self.stars[1].mass
        print("Mass = " + str(self.stars[1].mass))
    def putData(self):
        #for item in stars put()
        print("Star 1==================")
        self.stars[0].put()
        print("Star 2==================")
        self.stars[1].put()
class Star(object):
    def __init__(self, mass=None, rad_vel=None):
        self.mass = mass
        self.rad_vel = rad_vel
    def put(self):
        print("Mass = " +str(self.mass))
        print("Radial Velocity = " + str(self.rad_vel))















#module.py
'''
# # # Catalog # # #
-Kepler's law-
-Distance mod-
-Wien's law-
-Escape velocity-
Planetary temperature
Luminosity & app brightness
'''
def kepler3(period, semimajor, m1, m2, work=True):
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

def modulus(d, appmag, absmag, work=True):
  if d == None:
    return Quantity(10**((0.2*(appmag.value-absmag.value))+1), [pc], [])
  elif appmag == None:
    convd = convert(d, [pc], [])
    return Quantity(5*(np.log10(convd.value)-1) + absmag.value, [mag], [])
  elif absmag == None:
    convd = convert(d, [pc], [])
    return Quantity(appmag.value - (-5*(np.log10(convd.value)-1)), [mag], [])

def wiensLaw(lba, T, work=True):
  if lba == None:
    return Quantity(wien.value/T.value, [m], [])
  elif T == None:
    return Quantity(wien.value/lba.value, [K], [])

def escapeVel(escape_velocity, mass, radius, work=True):
  if escape_velocity == None:
    mass = convert(mass, [kg], [])
    radius = convert(radius, [m], [])
    return Quantity(np.sqrt((2*bigG.value*mass.value)/radius.value), [m], [s])
  elif mass == None:
    escape_velocity = convert(escape_velocity, [m], [s])
    radius = convert(radius, [m], [])
    return Quantity(((escape_velocity**2)*radius.value)/(2*bigG.value), [kg], [])
  elif radius == None:
    escape_velocity = convert(escape_velocity, [m], [s])
    mass = convert(mass, [kg], [])
    return Quantity((2*bigG.value*mass.value)/(escape_velocity.value**2), [m], [])

'''
def planetTemp(temp, luminosity, albedo, distance, work=True):
  if temp == None:
    convert(luminosity, [m, m, kg], [s, s, s])
    convert(distance, [m], [])
    return Quantity((((luminosity.value*(1-albedo))/(16*stefan.value*np.pi))**0.25)*(distance.value**-0.5), [K], [])
  elif luminosity == None:
    convert(temp, [K], [])
    convert(distance, [m], [])
    return #something
  elif albedo == None:
    convert(luminosity, [m, m, kg], [s, s, s])
    convert(distance, [m], [])
    convert(temp, [K], [])
    return #something
  elif distance == None:
    convert(luminosity, [m, m, kg], [s, s, s])
    convert(temp, [K], [])
    return #something
'''



