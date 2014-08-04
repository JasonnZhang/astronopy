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

constantStefan = 5.670373*(10**-8) #W(m^-2)(K^-4)


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

# Kepler's Law (p^2 = a^3)
def kepler3(a='default',P='default',work='pls'):
    if a == 'default' and P!='default':
        a = P ** (0.666666)
        print('Orbital radius A = ',a)
        if work == 'pls':
            print('''P^2 = a^3
                    a = P^(2/3)
                    a =''',a)
    elif P == 'default' and a!='default':
        P = a ** (1.5)
        print('Period = ',P)
        if work == 'pls':
            print('''P^2 = a^3
                    P = a ** (3/2)
                    P = ''',P)
    else
        print('Syntax:  kepler3(a, p, work)') # Maybe information about the formula can go here.
        
# Distance Modulus   
def modulus(d='default', appmag='default', absmag='default', work='yas')
    if d == 'default' and appmag!='default' and absmag!='default':
        d = 10 ** (((appmag-absmag)/5)+1)
        print('Distance d in pc = ', d)
        if work == 'yas':
            print('''d = 10^(((m-M)/5)+1)
                    d = ''', d)
    elif appmag=='default' and d!='default' and absmag!='default':
        appmag = 5*log(d/10, 10) + absmag
        print('Apparent magnitude m = ', appmag)
        if work == 'yas':
            print('''m = 5log(0.1d)+M
                    m = ''', appmag)
    elif absmag == 'default' and appmag!='default' and d!='default':
        absmag = -5*log(d/10, 10) + appmag
        print('Absolute magnitude M = ', absmag)
        if work == 'yas':
            print('''M = -5log(0.1d)+m
                    M = ''', absmag)
    else
        print('Syntax:  modulus(d, appmag, absmag, work)') # Maybe information about the formula can go here.

# Temperature of a planet
# Process: To find the expected temperature of a planet, you need to set the rate of energy radiated by the planet equal to the rate of energy absorbed by the planet. 
def tempOfPlanet(T='default', L='default', a='default', d='default', work='ofc')
    if T=='default' and L!='default' and a!='default' and d!='default'
        fourthroot = (L*(1-a))/(16*constantStefan*pi)
        T = (fourthroot**0.25)*(d**-0.5)
        print('Temperature T in K = ', T)
        if T > 100 or T < 0
            print('The planet is most likely not habitable. Liquid water cannot exist at this temperature.')
        if work == 'ofc':
            print('''4(pi)(R^2)(sigma)(T^4) = (pi)(R^2)(Lsun)(1-a)/(4(pi)(d^2))
                    T = ((Lsun(1-a)/16(sigma)(pi))^0.25) * (d^-0.5)
                    T = ''', T)
    elif L=='default' and T!='default' and a!='default' and d!='default'
        #I don't feel like doing the algebra here...
        if work == 'ofc':
            #print work
    elif a=='default' and L!='default' and T!='default' and d!='default'
        #Much algebra very tired
        if work == 'ofc':
            #print work
    elif d=='default' and L!='default' and a!='default' and T!='default'
        #Lack of paper nearby
        if work == 'ofc':
            #print work
    else
        print('Syntax:  tempOfPlant(temperature, luminosity of star, albedo, distance from star, work)') # Maybe information about the formula can go here.


        


