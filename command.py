#Run this file

def chdirimp(addr='C:/'):
	import os
	os.chdir(addr)
	import astro as ap # AstronoPy? Can't use 'as'
	import convert as cv
	import constant as cs
	
	print dir(ac)
	print dir(cv)
	print dir(cs)

#Here, run chdirimp(addr_of_astronopy) to change directory, import astro modules, and list functions
