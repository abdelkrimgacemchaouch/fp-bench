#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
###############creation de dossier de comparaison###############
#os.mkdir(os.getcwd() +'/comparaison') #cree dossier 
#os.system('chmod -R  777 ./comparaison') 
##########obtenir les dossier des bench#################
os.chdir(os.getcwd()+'/orginal/')
path = os.getcwd() 
#print(path)
for l in os.listdir(path):
	if os.path.isdir(l):
		 a = l	
		 #os.mkdir('../comparaison/' + a)
		 if os.path.isfile(path + '/' + a + '/comp.py'):
			os.chdir(path + '/' + a)	
			os.system('python comp.py')
			os.chdir(path)
			print(a)
		 else:
			print(a  +': we do not have compartive file !!!!!')
		 
