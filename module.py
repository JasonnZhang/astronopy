from sympy.solvers import solve
from sympy import Symbol

import numpy as np

stefan = 5.670373*(10**-8) #W(m^-2)(K^-4)
wien = 0.0028977721 #m K
hubble = 67.8 #(km/s)/Mpc
bigG = 6.67384*(10**-11) #(m^3)/(kg(s^2))
c = 299792458 #m/s


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

'''def distancemod(solveFor):
    m = Symbol('m')
    M = Symbol('M')
    d = Symbol('d')
    
    if (solveFor.upper()=='DISTANCE'):
        m = input('Apparent magnitude: ')
        M = input('Absolute magnitude: ')
        return solve(power(10, 
'''
