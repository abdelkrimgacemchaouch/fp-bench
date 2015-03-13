#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
path =  os.getcwd()

for element in os.listdir(path):
     if os.path.isdir(element): # si l'element est un dossier
	 a = element              
	 c = path + '/' + a # on prend le chemin de sous dossier
	 for e in os.listdir(c):	
		if os.path.isfile(c + '/CMakeLists.txt'):
			
			os.chdir(c + '/exe/')	
			
	
			#les preformance de chaque fichier et on les sauvgarde on z.txt
			
			p = os.system('python perf.py')
		

			os.chdir(path)
			break 	
		else:
			
			os.chdir(c)
			#les preformance de chaque fichier et on les sauvgarde on z.txt
			p = os.system('python perf.py')
						
				
			
			os.chdir(path)
			break
#on l'ance le fichier pour savoir tous les performance de nos programmes
p = os.system('python inn.py')














	
