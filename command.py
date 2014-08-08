#Run this file
import os

def chdirimp(addr='C:/'):
	
	os.chdir(addr)
	import astro as ap # AstronoPy? Can't use 'as'
	print dir(ap)
	

#Here, run chdirimp(addr_of_astronopy) to change directory, import astro modules, and list functions
