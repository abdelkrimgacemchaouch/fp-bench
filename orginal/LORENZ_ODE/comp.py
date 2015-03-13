#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
path = os.getcwd()
os.system('javac modi.java')
os.system('java modi')
os.chdir('../../32/LORENZ_ODE')
os.system('javac modi.java')
os.system('java modi')
os.chdir(path)
f=open('../../comparaison/LORENZ_ODE/comparison.txt','w')
f1=open('fichier1_64.txt','r')
f2=open('../../32/LORENZ_ODE/fichier1_64.txt','r')
####################################
f3=open('fichier2_64.txt','r')
f4=open('../../32/LORENZ_ODE/fichier2_64.txt','r')
###################################
f5=open('fichier3_64.txt','r')
f6=open('../../32/LORENZ_ODE/fichier3_64.txt','r')
###################################
f7=open('fichier4_64.txt','r')
f8=open('../../32/LORENZ_ODE/fichier4_64.txt','r')
###################################
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
l7 = f7.readlines()
l8 = f8.readlines()
###########################\
##########  MIN  ######################################################
def min(a, b, c, d) :
    l = [a, b, c, d]
    
    Min= l[0]
    for i in range(len(l)):
	if Min > l[i]:
		Min = l[i]
    return Min

		 
##########################################################################
##########  MAX  ######################################################
def max(a, b, c, d) :
    tab1 = [a, b, c, d]
    
    Max= tab1[0]
    for i in range(len(tab1)):
	if Max < tab1[i]:
		Max = tab1[i]
    return Max	 
##########################################################################


f.write("--------------------------------------------------------------------"+"\n")
f.write("----------------------- comparaison entre 64 et 32 -----------------"+"\n")
Min= float(l1[0]) - float(l2[0])
Max= float(l1[0]) - float(l2[0])
moy=0
pe=0

for i in range(4000):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
	l4c = float(l7[i]) - float(l8[i])
	if min(l1c , l2c ,l3c, l4c) < Min:
		Min = min(l1c , l2c ,l3c, l4c)
	if max(l1c , l2c ,l3c ,l4c) > Max:
		Max = max(l1c , l2c ,l3c, l4c)
	if (l1c!=0) or (l2c!=0) or (l3c!=0) or (l4c!=0) :
		pe= pe+1
		moy= l1c + l2c + l3c + l4c + moy	
	a = ""
	b= ""
	c=""
	d= len(str(l1c))
	x= len(str(l2c))
	y= len(str(l3c))
	while(d< 30):
		d=d+1
		a = a + " "	
	while(x< 30):
		x=x+1
		b = b + " "	
	while(y< 30):
		y=y+1
		c = c + " "	
	f.write(str(l1c) + a+ "||" + str(l2c) + b+ "||" + str(l3c)+ c+ "||" +str(l4c) +"\n")
	f.write("--------------------------------------------------------------------"+"\n")
	
f.close()	
#############################################################################################################################
##########################################################################################
f= open('../../comparaison/LORENZ_ODE/statistics.txt','w')
f.write('####################################################################################################'+'\n')
f.write('#                        statistics of comparaison between 64 and 32 data                           #'+'\n')
f.write('####################################################################################################'+'\n')
f.write('\n')
f.write('for our experience we have calculate the error x64- x32 and we have this result:' +'\n')
f.write('\n')
moy= moy/4000
f.write('average of error: ' + str(moy)+ '\n' )
f.write('\n')
f.write('Error min: ' +str(Min)+ '\n')
f.write('\n')
f.write('Error max: ' +str(Max)+'\n')
f.write('\n')
pe= (pe * 100) /(4000)
f.write('error percentage: '+ str(pe) +'%'+'\n')

os.system('rm -Rf fichier1_64.txt fichier2_64.txt fichier3_64.txt  ../../32/LORENZ_ODE/fichier1_64.txt ../../32/LORENZ_ODE/fichier2_64.txt ../../32/LORENZ_ODE/fichier3_64.txt')
os.system('cp xyz_3d.png ../../comparaison/LORENZ_ODE/xyz_3d_64.png ')
os.system('cp xyz_time.png ../../comparaison/LORENZ_ODE/xyz_time_64.png ')
os.chdir('../../32/LORENZ_ODE')
os.system('cp xyz_3d.png ../../comparaison/LORENZ_ODE/xyz_3d_32.png ')
os.system('cp xyz_time.png ../../comparaison/LORENZ_ODE/xyz_time_32.png ')

