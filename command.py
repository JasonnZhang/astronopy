import os
def chdirimp(addr='C:/'):
	os.chdir(addr)
	import astro as ap
	print dir(ap)
