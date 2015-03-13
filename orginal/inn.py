#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
path =  os.getcwd()
#on ouvert le fichier des instructions et on crees un nouveau fichier pour tous les performence
f3=open(path + '/nombre_insruction.txt','w')
f4=open(path + '/nombre_insruction_flottant.txt','w')
f3.write("=============================================================================================="+"\n")
f3.write("  benchmark  " + "       || " +"Nombre de cycle "  + "    ||"+ " Nombre instruction" "\n")
f4.write("============================================================================================================================="+"\n")
f4.write( "benchmark  " + " || "  "  N operation flottant    " + " || " + "  packed double    "+ " || " + "  saclar simple    " + " || " + "  packed simple    "+ " || " + "  scalar double    " + "\n")
l1 = " "
l2 = " "
l3 = " "
l4 = " "           
l5 = " "
l6 = " "
l7 = " "

for element in os.listdir(path):
     if os.path.isdir(element): # si l'element est un dossier
	 a = element              
	 c = path + '/' + a # on prend le chemin de sous dossier
	 for e in os.listdir(c):	
		if os.path.isfile(c + '/CMakeLists.txt'):
			os.chdir(c + '/exe/')
			f=open(os.getcwd() + "/z.txt",'r')
			cycle = 6
			ins = 7 
			r1 = 7
			r2 = 7
			r3 = 7
			r4 = 7
			r5 = 7
			epb=""
			for l in f :	
				if 'cycles'  in l or 'instructions' in l or 'r530110'  in l or 'r531010' in l or 'r532010'  in l or 'r534010' in l or 'r538010' in l:
					if 'cycles'  in l:
						
						while( l[cycle] != "c"):
							l1 = l[6:cycle+1]
							cycle = cycle+1	
							
					if  'instructions' in l:
						while( l[ins] != "i"):
							l2 = l[7:ins+1]
							ins = ins+1		
					if   'r530110' in l:
						while(l[r1] != "r"):
							l3 = l[7:r1+1] 
							r1 = r1+1
					if  'r531010' in l:
						while(l[r2] != "r"):
							l4 =l[7:r2+1]
							r2 = r2+1 
					if  'r532010' in l:
						while(l[r3] != "r"):
							l5 =l[7:r3+1]
							r3 = r3+1
					if 'r534010' in l:
						while(l[r4] != "r"):
							l6 =l[7:r4+1]
							r4 = r4+1
					if 'r538010' in l:
						while(l[r5] != "r"):
							l7 =l[7:r5+1]
							r5 = r5+1
			epb = a
			while(len(epb) < 24):
				epb = epb + " "
			espl1 =   l1
			while (len (espl1) < 24):
				espl1 = espl1 + " "
			espl2 =  l2
			while (len (espl2) < 18):
				espl2 = espl2 + " "
			espl3 =  l3
			while (len (espl3) < 28):
				espl3 = espl3 + " "
			espl4 =  l4
			while (len (espl4) < 21):
				espl4 = espl4 + " "
			espl5 =  l5
			while (len (espl5) < 21):
				espl5 = espl5 + " "
			espl6 =  l6
			while (len (espl6) < 21):
				espl6 = espl6 + " "
			f3.write(epb + "||" + espl1 +" ||"+ espl2 +"\n")
			f3.write("==========================================================================================="+"\n")
			epb1 = a
			while(len(epb1) < 12):
				epb1 = epb1 + " "			
			f4.write(epb1 +"||" + espl3 +"||" + espl4 +"||" + espl5 +"||" + espl6 +"||" + l7 +"\n")
			f4.write("============================================================================================================================="+"\n")
			f.close()
			os.chdir(path)
			break
		else:
			os.chdir(c)
			f=open(os.getcwd() + "/z.txt",'r')
			cycle = 6
			ins = 7
			r1 = 7
			r2 = 7
			r3 = 7
			r4 = 7
			r5 = 7
			for l in f :
				if 'cycles'  in l or 'instructions' in l or 'r530110'  in l or 'r531010' in l or 'r532010'  in l or 'r534010' in l or 'r538010' in l:		
					if 'cycles'  in l:
						while( l[cycle] != "c"):
							l1 = l[6:cycle+1]
							cycle = cycle+1		
					if  'instructions' in l:
						while( l[ins] != "i"):
							l2 = l[7:ins+1]
							ins = ins+1		
					if   'r530110' in l:
						while(l[r1] != "r"):
							l3 =l[7:r1+2]
							r1 = r1+2
					if  'r531010' in l:
						while(l[r2] != "r"):
							l4 =l[7:r2+2]
							r2 = r2+2
					if  'r532010' in l:
						while(l[r3] != "r"):
							l5 =l[7:r3+2]
							r3 = r3+2
					if 'r534010' in l:
						while(l[r4] != "r"):
							l6 =l[7:r4+2]
							r4 = r4+2
					if 'r538010' in l:
						while(l[r5] != "r"):
							l7 =l[7:r5+2]
							r5 = r5+2
			epb = a
			while(len(epb) < 24):
				epb = epb + " "
			espl1 =   l1
			while (len (espl1) < 24):
				espl1 = espl1 + " "
			espl2 =  l2
			while (len (espl2) < 18):
				espl2 = espl2 + " "
			espl3 =  l3
			while (len (espl3) < 28):
				espl3 = espl3 + " "
			espl4 =  l4
			while (len (espl4) < 21):
				espl4 = espl4 + " "
			espl5 =  l5
			while (len (espl5) < 21):
				espl5 = espl5 + " "
			espl6 =  l6
			while (len (espl6) < 21):
				espl6 = espl6 + " "
			f3.write(epb + "|| " + espl1 +"||"+ espl2 +"\n")
			f3.write("================================================================================================"+"\n")
			epb1 = a
			while(len(epb1) < 12):
				epb1 = epb1 + " "			
			f4.write(epb1 +"||" + espl3 +"||" + espl4 +"||" + espl5 +"||" + espl6 +"||" + l7 +"\n")
			f4.write("============================================================================================================================="+"\n")
			f.close()
			os.chdir(path)
			break
f3.close()
f4.close()
#####################################################################################################################################
os.mkdir(os.getcwd()+'/resultat')
os.system('cp nombre_insruction.txt ./resultat')	 		
os.system('cp nombre_insruction_flottant.txt ./resultat')
os.system('rm -Rf nombre_insruction.txt  nombre_insruction_flottant.txt')







              













	
