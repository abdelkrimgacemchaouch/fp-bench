#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
path = os.getcwd()
os.chdir(path)  
for element in os.listdir(path):
     if os.path.isdir(element): # si l'element est un dossier
	 a = element              
	 c = path + '/' + a # on prend le chemin de sous dossier
	 for e in os.listdir(c):	
		if os.path.isfile(c + '/CMakeLists.txt'):
			print('------------------------------------------------------')
			os.chdir(c + '/exe/')	
			p = os.system('perf stat -e r530110 -e r531010 -e r532010 -e r534010 -e r538010 ./*.out> z.txt 2>&1')
			os.chdir(path)
			break 	
		else:
			print('------------------------------------------------------')
			os.chdir(c)
			p = os.system('perf stat -e r530110 -e r531010 -e r532010 -e r534010 -e r538010 ./*.out> z.txt 2>&1')
			os.chdir(path)
			break
f=open(path + '/b.txt','w')
#f.write(output + "\n")
f.close()
