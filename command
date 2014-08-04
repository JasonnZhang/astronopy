Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def chdirimp(url='C:/'):
	import os
	os.chdir(url)
	import module as astro
	import convert as conv
	import const as const
	dir(astro)
	dir(conv)
	dir(const)
	
