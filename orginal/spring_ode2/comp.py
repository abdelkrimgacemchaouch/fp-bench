#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
path =  os.getcwd()
os.system('javac modi.java')
os.system('java modi')
os.chdir('../../32/spring_ode2')
os.system('javac modi.java')
os.system('java modi')
os.chdir(path)

f=open('../../comparaison/spring_ode2/comparison.txt','w')
f1=open('fichier1_64.txt','r')
f2=open('../../32/spring_ode2/fichier1_64.txt','r')
####################################
f3=open('fichier2_64.txt','r')
f4=open('../../32/spring_ode2/fichier2_64.txt','r')
###################################
f5=open('fichier3_64.txt','r')
f6=open('../../32/spring_ode2/fichier3_64.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
##########  MIN  ######################################################
def min(a, b, c) :
    l = [a, b, c]
    
    Min= l[0]
    for i in range(len(l)):
	if Min > l[i]:
		Min = l[i]
    return Min

		 
##########################################################################
##########  MAX  ######################################################
def max(a, b, c) :
    tab1 = [a, b, c]
    
    Max= tab1[0]
    for i in range(len(tab1)):
	if Max < tab1[i]:
		Max = tab1[i]
    return Max	 
##########################################################################

f.write('-----------------------------------------------------------------------'+"\n")
f.write('-------------------------- comparaison entre 64 et 32 -----------------'+"\n")
f.write('-----------------------------------------------------------------------'+"\n")
Min= float(l1[0]) - float(l2[0])
Max= float(l1[0]) - float(l2[0])
moy=0
pe=0
for i in range(101):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
	if min(l1c , l2c ,l3c) < Min:
		Min = min(l1c , l2c ,l3c)
	if max(l1c , l2c ,l3c ) > Max:
		Max = max(l1c , l2c ,l3c)
	if (l1c!=0) or (l2c!=0) or (l3c!=0)  :
		pe= pe+1
		moy= l1c + l2c + l3c  + moy	
	a = ""
	b= ""	
	d= len(str(l1c))
	x= len(str(l2c))
	
	while(d< 30):
		d=d+1
		a = a + " "	
	while(x< 30):
		x=x+1
		b = b + " "
	f.write(str(l1c) + a + "||" + str(l2c) + b +"||" + str(l3c) +"\n")
	f.write('-----------------------------------------------------------------------'+"\n")
f.close()	
f= open('../../comparaison/spring_ode2/statistics.txt','w')
f.write('####################################################################################################'+'\n')
f.write('#                        statistics of comparaison between 64 and 32 data                           #'+'\n')
f.write('####################################################################################################'+'\n')
f.write('\n')
f.write('for our experience we have calculate the error x64- x32 and we have this result:' +'\n')
f.write('\n')
moy= moy/101
f.write('average of error: ' + str(moy)+ '\n' )
f.write('\n')
f.write('Error min: ' +str(Min)+ '\n')
f.write('\n')
f.write('Error max: ' +str(Max)+'\n')
f.write('\n')
pe= (pe * 100) /(101)
f.write('error percentage: '+ str(pe) +'%'+'\n')

os.system('rm -Rf fichier1_64.txt fichier2_64.txt fichier3_64.txt ../../32/spring_ode2/fichier1_32.txt ../../32/spring_ode2/fichier2_32.txt ../../32/spring_ode2/fichier3_32.txt  ')
os.system('cp xv_phase.png ../../comparaison/spring_ode2/xv_phase.png64.png ')
os.system('cp xv_time.png ../../comparaison/spring_ode2/xv_time.png64.png ')
os.chdir('../../32/spring_ode2')
os.system('cp xv_phase.png ../../comparaison/spring_ode2/xv_phase.png32.png ')
os.system('cp xv_time.png ../../comparaison/spring_ode2/xv_time.png32.png ')
