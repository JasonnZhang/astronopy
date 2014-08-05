import * units

# # # Constants # # #

sun = dict(absMag=4.8,appMag=-26.7,temp=5800,coronaTemp=1000000)

#All temperatures in K
#All masses in kg
'''
sunAbsMag = 4.8
sunAppMag = -26.7
sunTemp = 5800 #K
sunCoronaTemp = 1000000 #K
sunChromTemp = 10000 #K
sunPhotoTemp = 6000 #K
sunCoreTemp = 15000000 #K
sunMass = 1989000000000000000000000000000 #kg
sunFlux = 1370 #W/m^2
sunRadius = 695590000 #m
sunDensity = 1.41 #g/cm^3
sunEscapeSpeed = 618 #km/s
sunSurfGrav = 27.9 #times Earth's
sunEqRotPeriod = 25.04 #days
sunPoleRotPeriod = 30 #days
sunAge = 4570000000 #years
sunOblique = 7.25 #degrees

earthMass = 5976*(10**24) #kg
earthDensity = 5515 #kg/m^3
earthSurfTemp = 287 #K
earthSurfGrav = 9.78 #m/s^2
earthRadius = 6378 #km
earthMoonDist = 384400 #km
'''

stefan = (5.670373*(10**-8) #W(m^-2)(K^-4)
wien = 0.0028977721 #m K
hubble = 67.8 #(km/s)/Mpc


bigG = Quantity(6.67384*(10**-11), [m.abbr, m.abbr, m.abbr], [kg.abbr, s.abbr, s.abbr]) #(m^3)/(kg(s^2))
c = Quantity(299792458, [m.abbr], [s.abbr]) #m/s


#Milankovitch cycles - don't know if we need these
