from sympy.solvers import solve
from sympy import Symbol

import numpy as np

stefan = 5.670373*ten(-8) #W(m^-2)(K^-4)
wien = 0.0028977721 #m K
hubble = 67.8 #(km/s)/Mpc
bigG = 6.67384*ten(-11) #(m^3)/(kg(s^2))
c = 299792458 #m/s

def ten(p):
    return 10**p
    


# # # Sun # # #
sunCoronaTemp = ten(6) #K
sunChromTemp = ten(5) #K
sunPhotoTemp = 6*ten(3) #K
sunCoreTemp = 1.5*ten(7) #K
sunRadius = 6.96342*ten(8) #m
sunMass = 1.989*ten(30) #kg
sunVolume = 1.41*ten(21) #m
sunLuminosity = 3.846*ten(26) #W
sunDistance = 1.496*ten(11) #m
sunAbsMag = 4.83
sunAppMag = -26.74
sunDensity = 1.41 #g/cm^3
sunEqRotPeriod = 25.04 #days
sunPoleRotPeriod = 30 #days

# # # Earth # # #
earthMass = 5976*ten(24) #kg
earthDensity = 5515 #kg/m^3
earthSurfTemp = 287 #K
earthSurfGrav = 9.78 #m/s^2
earthRadius = 6378 #km
earthMoonDist = 384400 #km

def stefanBoltzmann(solveFor):
    L = Symbol('L')
    r = Symbol('r')
    e = Symbol('e')
    T = Symbol('T')
    
    if (solveFor.upper()=='LUMINOSITY'):    
        r = input('Radius (m): ')
        e = input('Emissivity (blackbody = 1) (unitless): ')
        T = input('Temperature (K): ')
        return solve(((4*np.pi*(r**2))*e*stefan*(T**4))-L, L)
    elif (solveFor.upper()=='RADIUS'):    
        L = input('Luminosity (kg*(m**2)/(s**2)): ')
        e = input('Emissivity (blackbody = 1) (unitless): ')
        T = input('Temperature (K): ')
        return solve(((4*np.pi*(r**2))*e*stefan*(T**4))-L, r)
    elif (solveFor.upper()=='TEMPERATURE'):    
        r = input('Radius (m): ')
        e = input('Emissivity (blackbody = 1) (unitless): ')
        L = input('Luminosity (kg*(m**2)/(s**2)): ')
        return solve(((4*np.pi*(r**2))*e*stefan*(T**4))-L, T)

def kepler3(solveFor):
    m = Symbol('m')
    P = Symbol('P')
    a = Symbol('a')

    if (solveFor.upper()=='MASS'):
        P = input('Period (s): ')
        a = input('Semimajor axis (m): ')
        return solve((((4*(np.pi**2))/(bigG*m))*(a**3)) - (P**2), m)
    elif (solveFor.upper()=='PERIOD'):
        m = input('Mass sum (kg): ')
        a = input('Semimajor axis (m): ')
        return solve((((4*(np.pi**2))/(bigG*m))*(a**3)) - (P**2), P)
    elif (solveFor.upper()=='SEMIMAJOR'):
        P = input('Period (s): ')
        m = input('Mass sum (kg): ')
        return solve((((4*(np.pi**2))/(bigG*m))*(a**3)) - (P**2), a)

def distanceMod(solveFor):
    m = Symbol('m')
    M = Symbol('M')
    d = Symbol('d')
    
    if (solveFor.upper()=='DISTANCE'):
        m = input('Apparent magnitude: ')
        M = input('Absolute magnitude: ')
        return solve(10**((0.2*(m-M))+1)-d, d)
    elif (solveFor.upper()=='APPMAG'):
        d = input('Distance (pc): ')
        M = input('Absolute magnitude: ')
        return solve(10**((0.2*(m-M))+1)-d, m)
    elif (solveFor.upper()=='ABSMAG'):
        d = input('Distance (pc): ')
        m = input('Apparent magnitude: ')
        return solve(10**((0.2*(m-M))+1)-d, M)

def redshift(solveFor):
    o = Symbol('o')
    e = Symbol('e')
    z = Symbol('z')
    print('Remember that z = v/c or that the z-value is in terms of the speed of light.')
    if (solveFor.upper()=='OBS'):
        e = input('Emitted wavelength (any unit of length): ')
        z = input('Redshift (unitless): ')
        return solve(((o-e)/e)-z, o)
    if (solveFor.upper()=='EMIT'):
        o = input('Observed wavelength (any unit of length): ')
        z = input('Redshift (unitless): ')
        return solve(((o-e)/e)-z, e)
    if (solveFor.upper()=='REDSHIFT'):
        o = input('Observed wavelength (any unit of length): ')
        e = input('Emitted wavelength (any unit of length): ')
        return solve(((o-e)/e)-z, z)
