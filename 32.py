#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
import shutil
#-----------------copier les dossier et cree les source 32-----------#
src= os.getcwd()  + '/orginal' #dossier source 	
des = os.getcwd() + '/32'      #dossier cible
shutil.copytree(src, "/home/abdlkrim/mes_bench/tesr/32") #copier le contenu de dossier 64
#-----------------------------------fin------------------------------#
#----------------------changer de 64 -> 32----------------#
os.chdir(os.getcwd()+'/32/') 
path = os.getcwd()
#print(path)
for l in os.listdir(path):
	if os.path.isdir(l):
		 a = l
		 os.chdir(path + '/' + a) # on prend le chemin de sous dossier	              
		 c = os.getcwd()		
		 for e in os.listdir(c):	
			if os.path.isfile(c + '/CMakeLists.txt'):
				os.system('rm -Rf ./exe')
				os.system('mkdir ./exe')
				os.system('cp perf.py ./exe')
				os.system('cp a.py ./exe')
				os.chdir(c + '/src/')
				for e in os.listdir(os.getcwd()):
					if os.path.isfile(e):	
						i=0
						l1=""
						while(e[i] != '.') and (e[i] !='~'):
							l1= e[0:i+1]
							i = i + 1
						
					
						if os.path.isfile(l1 + ".c") :	
							result=file(os.getcwd() +"/"+ l1 +".c","r").read().replace("double", "float")
							file(os.getcwd() +"/"+ l1 + ".c","w").write(result)
						if os.path.isfile(l1 + ".cpp") :	
							result=file(os.getcwd() +"/"+ l1 +".cpp","r").read().replace("double", "float")
							file(os.getcwd() +"/"+ l1 + ".cpp","w").write(result)
				os.chdir(path)
				break
			else:
				os.chdir(c )
				for e in os.listdir(os.getcwd()):
					if os.path.isfile(e) :	
						i=0
						l1=""
						while(e[i] != '.') and (e[i] !='~') and (e !='readme'):
							l1= e[0:i+1]
							i = i + 1
							print(l1)
					
						if os.path.isfile(l1 + ".c"):	
							result=file(os.getcwd() +"/"+ l1 +".c","r").read().replace("double", "float")
							file(os.getcwd() +"/"+ l1 + ".c","w").write(result)
						if os.path.isfile(l1 + ".cpp") :	
							result=file(os.getcwd() +"/"+ l1 +".cpp","r").read().replace("double", "float")
							file(os.getcwd() +"/"+ l1 + ".cpp","w").write(result)
				os.chdir(path)
				break
#--------------------------------------------fin---------------------------------------------------------------------------------------#
print(os.getcwd())
p = os.system('python install.py')
#p1= os.system('python performence.py')
