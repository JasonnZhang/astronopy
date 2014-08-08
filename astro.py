import numpy as np
#import scipy as sp
import convert as cv
import units as units
units.initUnits()
import constants as cs
from quantity import *

# # # General Pythoning Tips # # #
# Don't use fractions. Python hates fractions. Convert to decimal floats.
# You can do functions within functions, a la C2K(K2F(n)).
# 3 is cursed. Use int(pi). (http://xkcd.com/1275/)


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
