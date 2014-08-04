import numpy as np
import scipy as sp

# # # General Pythoning Tips # # #
# Don't use fractions. Python hates fractions. Convert to decimal floats.
# You can do functions within functions, a la C2K(K2F(n)).
# 3 is cursed. Use int(pi). (http://xkcd.com/1275/)

# # # Constants # # #


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

earthMass = 5980000000000000000000000 #kg
earthDensity = 5515 #kg/m^3
earthSurfTemp = 287 #K
earthSurfGrav = 9.78 #m/s^2
earthRadius = 6378 #km
earthMoonDist = 384400 #km

#Milankovitch cycles - don't know if we need these



# # # Conversions, or things with one number # # #

'''
A more elegant way to do these conversions may be something like
convert(n,origUnit,newUnit), although I suspect it would still
take a ridiculous number of lines. It would look something like:

def convert(n,origUnit,newUnit):
    if origUnit == 'ly':
        if newUnit == 'pc':
            return ly * 0.30660
        elif newUnit == 'au':
            return ly * 0.000015812281999789
        ...
    elif origUnit == 'au':
        if newUnit = 'ly':
            return au * 63241.978609626
        ...
    elif origUnit == 'pc':
    ...

You get my point. I guess theoretically you should be able to halve
the number of lines by using the same statement for things like K2C and
C2K; however, Python doesn't think C = K - 273.15 and K = C + 273.15
are the same thing. Therefore, no matter what, the conversions are
going to take a ridiculous amount of space. Dunno, do you like the
above format or the one below? I'm opting for the below format since it
would require the least amount of typing for the user. - C

'''

### TEMPERATURE ###
def K2C(K):
    return K - 273.15
def C2K(C):
    return C + 273.15

def F2K(F):
    return
def K2F(K):
    return

def C2F(C):
    return
def F2C(F):
    return

### LENGTH ###
def pc2m(pc):
    return pc * 30860000000000000
def m2pc(m):
    return m / 30860000000000000
    
def ly2pc(ly):
    return ly / 3.2616
def pc2ly(pc):
    return pc * 3.2616

def au2ly(au):
    return au / 63241.978609626
def ly2au(ly):
    return ly * 63241.978609626

def au2pc(au):
    return au / 206263.36898396
def pc2au(pc):
    return pc * 206263.36898396

### ANGULAR ###
def rad2deg(rad):
    return
def deg2rad(deg):
    return

# # # Formulae, or things with 2 or more numbers # # #

### ORIGINAL PHYSICS SHEET ###
def kepler3(a='default',P='default',work='pls'):
    if a == 'default':
        a = P ** (0.666666)
        print('Orbital radius A =',a)
        if work == 'pls':
            print('''P^2 = a^3
                    a = P^(2/3)
                    a =''',a)
    elif P == 'default':
        P = a ** (1.5)
        print('Period =',P)
        if work == 'pls':
            print('''P^2 = a^3
                    P = a ** (3/2)
                    P =''',P)
