#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
f=open('../../comparaison/irsmk/comparison.txt','w')
f64= open('64.txt','w')
f32= open('32.txt','w')
f1=open('./exe/t.txt','r')
f2=open('../../32/irsmk/exe/t.txt','r')
i = 0 
l1 = f1.readlines()
l2 = f2.readlines()
while ('results' not in l1[i]):
	i =i+1
i = i+2
z = i+11
while(i<z):
	
	f64.write(l1[i][27:])
	f32.write(l2[i][27:])
	i= i+2
while ('results' not in l1[i]):
	i =i+1
i = i+2
z = i+11
while(i<z):
	
	f64.write(l1[i][27:])
	f32.write(l2[i][27:])
	i= i+2
while ('results' not in l1[i]):
	i =i+1
i = i+2
z = i+11
while(i<z):
	
	f64.write(l1[i][27:])
	f32.write(l2[i][27:])
	i= i+2
f64.close()
f32.close()
##############################################
#fin de prendre les info
#############################################

f64= open('64.txt','r')
f32= open('32.txt','r')
l1 = f64.readlines()
l2 = f32.readlines()
i=0
f.write("---------------------------"+"\n")
f.write("comparaison entre 64 et 32"+"\n")
f.write("   petit jeux données  "+"\n")
Min = float(l1[1]) - float(l2[1])
Max = float(l1[1]) - float(l2[1])
moy=0
pe=0
f1= open('../../comparaison/irsmk/statistics.txt','w')
f1.write('####################################################################################################'+'\n')
f1.write('#                        statistics of comparaison between 64 and 32 data                          #'+'\n')
f1.write('####################################################################################################'+'\n')
f1.write('\n')
f1.write('\n')
f1.write('for our experience we have calculate the error x64- x32 for each step and we have this result:' +'\n')
while (i<6):
	l1c = float(l1[i]) - float(l2[i])
	f.write(str(l1c) + "\n")
	if l1c < Min:
		Min = l1c
	if l1c > Max:
		Max = l1c
	if (l1c!=0):
		moy = moy+l1c
		pe =pe+1
	i= i+1
######################################################################
f1.write("---------------------------------------------------------------------------"+"\n")
f1.write("   petit jeux données  "+"\n")
moy = moy/5
pe = (pe*100)/5
f1.write('           the total satatistic are : ' '\n')
f1.write('average of error: ' + str(moy)+ '\n' )
f1.write('\n')
f1.write('Error min: ' +str(Min)+ '\n')
f1.write('\n')
f1.write('Error max: ' +str(Max)+'\n')
f1.write('\n')

f1.write('error percentage: '+ str(pe) +'%'+'\n')
#########################################################################""
f.write("---------------"+"\n")
f.write("   moyen jeux données  "+"\n")

Min = float(l1[11]) - float(l2[11])
Max = float(l1[11]) - float(l2[11])
moy=0
pe=0
while (i<11):
	l1c = float(l1[i]) - float(l2[i])
	f.write(str(l1c) + "\n")
	if l1c < Min:
		Min = l1c
	if l1c > Max:
		Max = l1c
	if (l1c!=0):
		moy = moy+l1c
		pe =pe+1
	i= i+1
######################################################################
f1.write("---------------------------------------------------------------------------"+"\n")
f1.write("   moyen jeux données  "+"\n")
moy = moy/5
pe = (pe*100)/5
f1.write('           the total satatistic are : ' '\n')
f1.write('average of error: ' + str(moy)+ '\n' )
f1.write('\n')
f1.write('Error min: ' +str(Min)+ '\n')
f1.write('\n')
f1.write('Error max: ' +str(Max)+'\n')
f1.write('\n')

f1.write('error percentage: '+ str(pe) +'%'+'\n')
#########################################################################""

f.write("---------------"+"\n")
f.write("   grand jeux données  "+"\n")

Min = float(l1[16]) - float(l2[16])
Max = float(l1[16]) - float(l2[16])
moy=0
pe=0
while (i<16):
	l1c = float(l1[i]) - float(l2[i])
	f.write(str(l1c) + "\n")
	if l1c < Min:
		Min = l1c
	if l1c > Max:
		Max = l1c
	if (l1c!=0):
		moy = moy+l1c
		pe =pe+1
	i= i+1
######################################################################
f1.write("---------------------------------------------------------------------------"+"\n")
f1.write("   moyen jeux données  "+"\n")
moy = moy/5
pe = (pe*100)/5
f1.write('           the total satatistic are : ' '\n')
f1.write('average of error: ' + str(moy)+ '\n' )
f1.write('\n')
f1.write('Error min: ' +str(Min)+ '\n')
f1.write('\n')
f1.write('Error max: ' +str(Max)+'\n')
f1.write('\n')

f1.write('error percentage: '+ str(pe) +'%'+'\n')
#########################################################################""

os.system('rm -Rf 64.txt 32.txt ')
