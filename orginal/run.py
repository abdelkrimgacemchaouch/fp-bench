#!/usr/bin/env python
import os
path =  os.getcwd() # trouver le dossier ou nous sommes

for element in os.listdir(path):
     if os.path.isdir(element): # si l'element est un dossier
	 a = element              
	 c = path + '/' + a # on prend le chemin de sous dossier
	 for e in os.listdir(c):	
		if os.path.isfile(c + '/CMakeLists.txt'):
			print('------------------------------------------------------')
			os.chdir(c + '/exe/')	
			os.system('python a.py') 
			os.chdir(path)
			break 	
		else:
			print('------------------------------------------------------')
			os.chdir(c)
			os.system(' python a.py') 
			os.chdir(path)
			break





















	
