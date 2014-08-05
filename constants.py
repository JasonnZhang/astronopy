from quantity import *
from units import *

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
earthDensity = Quantity(5515, [kg.abbr], [m.abbr, m.abbr, m.abbr) #kg/m^3
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
