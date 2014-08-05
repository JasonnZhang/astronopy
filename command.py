#Run this file
import os

def chdirimp(addr='C:/'):
	
	os.chdir(addr)
	import astro as ap # AstronoPy? Can't use 'as'
	import convert as cv
	import constant as cs
	from units import *
	from quantity import *
	
	print dir(ac)
	print dir(cv)
	print dir(cs)

#Here, run chdirimp(addr_of_astronopy) to change directory, import astro modules, and list functions
