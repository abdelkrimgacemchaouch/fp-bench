#!/usr/bin/env python
import os
path = os.getcwd() # trouver le dossier ou nous sommes
for element in os.listdir(path):
     if os.path.isdir(element): # si l'element est un dossier
	 a = element              
	 c = path + '/' + a # on prend le chemin de sous dossier
	 for e in os.listdir(c):	
		if os.path.isfile(c + '/CMakeLists.txt'):
			print('ok')
			os.chdir(c + '/exe/')	
			
			os.system('cmake ..')
			os.system('make')
			os.chdir(path)
			break 	
		else:
			print('n')
			os.chdir(c)
			os.system('./*.sh')
			os.chdir(path)
			break
os.system('python run.py')

	
