#Run this file

def chdirimp(addr='C:/'):
	import os
	os.chdir(addr)
	import module as astro
	import convert as conv
	import const as const
	dir(astro)
	dir(conv)
	dir(const)

#Here, run chdirimp(addr_of_astronopy) to change directory, import astro modules, and list functions
