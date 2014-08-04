import numpy as np
import scipy as sp
import convert as conv
import constants as const

# # # General Pythoning Tips # # #
# Don't use fractions. Python hates fractions. Convert to decimal floats.
# You can do functions within functions, a la C2K(K2F(n)).
# 3 is cursed. Use int(pi). (http://xkcd.com/1275/)

###### We should find and replace 'default' with 'solve'. What do you think? -A ######



# # # Formulae, or things with 2 or more numbers # # #


# Kepler's Law (p^2 = a^3)
def kepler3(a='default',P='default',work='pls'):
    if a == 'default' and P!='default':
        a = P ** (0.66666666666666666)
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
        fourthroot = (L*(1-a))/(16*const.constantStefan*pi)
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

# Escape velocity
def escapeVelocity(v='default', M='default', r='default', work ='mhm')
    if v=='default' and M!='default' and r!='default
        v = sqrt((2*const.bigG)/r)
        print('Escape velocity v in m/s = ', v)
        if work == 'mhm'
            print('''v = sqrt(2GM/r)
                    v = ''', v)
    elif M=='default' and v!='default' and r!='default
        # Lazy again to solve for mass
        if work == 'mhm'
            #print work
    elif r=='default' and v!='default' and M!='default
        # 2 algebra 2 function
        if work == 'mhm'
            #print work
    else
        print('Syntax:  escapeVeloity(velocity, mass, radius, work)')   

# Wien's Law
def wien(w='default', T='default', work='yes')
    if w=='default' and T!='default'
        w = const.wien/T
        print('Max wavelength lambda in m = ', w)
        if work =='yes'
            print('''lambda = c/T
                    lambda = ''', w)
    elif T=='default' and w!=default
        T = const.wien/w
        print('Temperature T in K = ', T)
        if work == 'yes'
            print('''lambda = c/T
                    T = c/lambda
                    T = ''', T)
    else
        print('Syntax:  wien(max_wavelength, temperature, work)')
        
# Luminosity <==> Apparent Brightness
def lumAppBright(b='default', L='default', d='default', work='hmu')
    if b=='default' and L!='default' and d!='default'
        b = L/(4*pi*(d**2))
        print('Apparent brightness b in W/m^2 = ', b)
        if work == 'hmu'
            print('''b = L/4*pi*d^2
                    b = ''', b)
    elif L=='default' and b!='default' and d!='default'
        L = 4*pi*b*(d**2)
        print('Luminosity L in W = ', L)
        if work == 'hmu'
            print('''b = L/4*pi*d^2
                    L = 4(pi)(b)(d^2)
                    L = ''', L)
    elif d=='default' and b!=default and L!='default'
        d = sqrt(L/(4*pi*b))
        print('Distance d in m = ', d)
        if work == 'hmu'
            print('''b = L/4*pi*d^2
                    d = sqrt(L/(4*pi*b))
                    d = ''', d)
    else
        print('Syntax:  lumAppBright(apparent_brightness, luminosity, distance, work)')

            
