#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
os.system('python extrait.py')
path = os.getcwd()
os.chdir('../../32/memory_test')
os.system('python extrait.py')
os.chdir(path)
f=open('../../comparaison/memory_test/comparison.txt','w')
f1=open('fichier1.txt','r')
f2=open('../../32/memory_test/fichier1.txt','r')
####################################
f3=open('fichier2.txt','r')
f4=open('../../32/memory_test/fichier2.txt','r')
###################################
f5=open('fichier3.txt','r')
f6=open('../../32/memory_test/fichier3.txt','r')
##################################
f7=open('fichier4.txt','r')
f8=open('../../32/memory_test/fichier4.txt','r')
##################################
##################################
f9=open('fichier5.txt','r')
f10=open('../../32/memory_test/fichier5.txt','r')
##################################
##################################
f11=open('fichier6.txt','r')
f12=open('../../32/memory_test/fichier6.txt','r')
##################################
##################################
f13=open('fichier7.txt','r')
f14=open('../../32/memory_test/fichier7.txt','r')
##################################
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
##################################
l7 = f7.readlines()
l8 = f8.readlines()
###########################
l9 = f9.readlines()
l10 = f10.readlines()
###########################
l11 = f11.readlines()
l12 = f12.readlines()
###########################
l13 = f13.readlines()
l14 = f14.readlines()
#########################
##########  MIN4  ######################################################
def min(a, b, c, d, e) :
    l = [a, b, c, d, e]
    
    Min= l[0]
    for i in range(len(l)):
	if Min > l[i]:
		Min = l[i]
    return Min

		 
##########################################################################
##########  MAX4  ######################################################
def max(a, b, c, d ,e) :
    tab1 = [a, b, c, d ,e]
    
    Max= tab1[0]
    for i in range(len(tab1)):
	if Max < tab1[i]:
		Max = tab1[i]
    return Max	 
##########################################################################
##########  MIN 8 ######################################################
def minn(a, b, c, d, e, f , g) :
    l = [a, b, c, d, e, f, g]
    
    Min= l[0]
    for i in range(len(l)):
	if Min > l[i]:
		Min = l[i]
    return Min

		 
##########################################################################
##########  MAX 8 ######################################################
def maxx(a, b, c, d, e, f , g) :
    tab1 = [a, b, c, d, e, f , g]
    
    Max= tab1[0]
    for i in range(len(tab1)):
	if Max < tab1[i]:
		Max = tab1[i]
    return Max	 
##########################################################################
i= 0 
f.write("------------------------------------------comparaison entre 64 et 32 -------------------------------------- " +"\n")
f.write("-----------------------------------------------------------------------------------------------------------" + "\n")
f.write("                                              I4VEC Memory Test                                                             "+"\n")
###############################################################################################################################
f1= open('../../comparaison/memory_test/statistics.txt','w')
f1.write('####################################################################################################'+'\n')
f1.write('#                        statistics of comparaison between 64 and 32 data                           #'+'\n')
f1.write('####################################################################################################'+'\n')
f1.write('\n')
f1.write('for our experience we have calculate the error x64- x32 and we have this result:' +'\n')
f1.write('\n')
f1.write("-----------------------------------------------------------------------------------------------------------" + "\n")
f1.write("                                              I4VEC Memory Test                                                             "+"\n")
################################################################################################################################
Min=float(l1[0]) - float(l2[0])
Max=float(l1[0]) - float(l2[0])
moy =0
pe=0
while(i<28):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
	l4c = float(l7[i]) - float(l8[i])
	l5c = float(l9[i]) - float(l10[i])
###########################################################################
	if min(l1c , l2c ,l3c, l4c, l5c) < Min:
		Min = min(l1c , l2c ,l3c, l4c ,l5c)
	if max(l1c , l2c ,l3c ,l4c ,l5c) > Max:
		Max = max(l1c , l2c ,l3c, l4c,l5c)
	if (l1c!=0) or (l2c!=0) or (l3c!=0) or (l4c!=0) or (l5c!=0) :
		pe= pe+1
		moy= l1c + l2c + l3c + l4c +l5c+ moy	
######################################################################"""""	
	a = ""
	b= ""
	c=""
	o= ""
	d= len(str(l1c))
	x= len(str(l2c))
	y= len(str(l3c))
	g= len(str(l4c))
	while(d< 15):
		d=d+1
		a = a + " "	
	while(x< 15):
		x=x+1
		b = b + " "	
	while(y< 15):
		y=y+1
		c = c + " "
	while(g< 15):
		g=g+1
		o = o + " "
	f.write(str(l1c) + a+ "||" + str(l2c) + b+ "||" + str(l3c) + c +"||"+str(l4c)+ o + "||" +str(l5c)+ "\n")
	f.write("-----------------------------------------------------------------------------------------------------------" + "\n")
	i = i+1
f.write("-----------------------------------------------------------------------------------------------------------" + "\n")
#####################################################################"""
moy= moy/28
f1.write('average of error: ' + str(moy)+ '\n' )
f1.write('\n')
f1.write('Error min: ' +str(Min)+ '\n')
f1.write('\n')
f1.write('Error max: ' +str(Max)+'\n')
f1.write('\n')
pe= (pe * 100) /(28)
f1.write('error percentage: '+ str(pe) +'%'+'\n')
f1.write("-----------------------------------------------------------------------------------------------------------"+"\n")
############################################################################################################
f.write("                                             R4VEC Memory Test                                                             "+"\n")
Min=float(l1[i+1]) - float(l2[i+1])
Max=float(l1[i+1]) - float(l2[i+1])
moy =0
pe=0
f1.write("                                             R4VEC Memory Test                                                             "+"\n")

while(i<55):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
	l4c = float(l7[i]) - float(l8[i])
	l5c = float(l9[i]) - float(l10[i])
	a = ""
	b= ""
	c=""
	o=""
	###########################################################################
	if min(l1c , l2c ,l3c, l4c, l5c) < Min:
		Min = min(l1c , l2c ,l3c, l4c, l5c)
	if max(l1c , l2c ,l3c ,l4c, l5c) > Max:
		Max = max(l1c , l2c ,l3c, l4c,l5c)
	if (l1c!=0) or (l2c!=0) or (l3c!=0) or (l4c!=0) or (l5c!=0) :
		pe= pe+1
		moy= l1c + l2c + l3c + l4c +l5c+ moy	
	######################################################################"""""	

	d= len(str(l1c))
	x= len(str(l2c))
	y= len(str(l3c))
	g= len(str(l4c))
	while(d< 15):
		d=d+1
		a = a + " "	
	while(x< 15):
		x=x+1
		b = b + " "	
	while(y< 15):
		y=y+1
		c = c + " "
	while(g< 15):
		g=g+1
		o = o + " "
	f.write(str(l1c) + a+ "||" + str(l2c) + b+ "||" + str(l3c) + c +"||"+str(l4c)+ o + "||" +str(l5c)+ "\n")
	f.write("-----------------------------------------------------------------------------------------------------------" + "\n")
	i = i+1
f.write("-----------------------------------------------------------------------------------------------------------"+ "\n")
#####################################################################"""
moy= moy/28
f1.write('average of error: ' + str(moy)+ '\n' )
f1.write('\n')
f1.write('Error min: ' +str(Min)+ '\n')
f1.write('\n')
f1.write('Error max: ' +str(Max)+'\n')
f1.write('\n')
pe= (pe * 100) /(28)
f1.write('error percentage: '+ str(pe) +'%'+'\n')
f1.write("-----------------------------------------------------------------------------------------------------------"+"\n")
############################################################################################################

f.write("                                           R8VEC Memory Test                                                             "+"\n")
#######################################################################################################################################
f1.write("                                           R8VEC Memory Test                                                             "+"\n")
Min=float(l1[i+1]) - float(l2[i+1])
Max=float(l1[i+1]) - float(l2[i+1])
moy =0
pe=0
##########################################################################################################
while(i<83):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
	l4c = float(l7[i]) - float(l8[i])
	l5c = float(l9[i]) - float(l10[i])
	###########################################################################
	if min(l1c , l2c ,l3c, l4c, l5c) < Min:
		Min = min(l1c , l2c ,l3c, l4c,l5c)
	if max(l1c , l2c ,l3c ,l4c,l5c) > Max:
		Max = max(l1c , l2c ,l3c, l4c,l5c)
	if (l1c!=0) or (l2c!=0) or (l3c!=0) or (l4c!=0) or (l5c!=0) :
		pe= pe+1
		moy= l1c + l2c + l3c + l4c +l5c+ moy	
	######################################################################"""""
	a = ""
	b= ""
	c=""
	o=""
	d= len(str(l1c))
	x= len(str(l2c))
	y= len(str(l3c))
	g= len(str(l4c))
	while(d< 15):
		d=d+1
		a = a + " "	
	while(x< 15):
		x=x+1
		b = b + " "	
	while(y< 15):
		y=y+1
		c = c + " "
	while(g< 15):
		g=g+1
		o = o + " "
	f.write(str(l1c) + a+ "||" + str(l2c) + b+ "||" + str(l3c) + c +"||"+str(l4c)+ o + "||" +str(l5c)+ "\n")
	f.write("-----------------------------------------------------------------------------------------------------------" + "\n")
	i = i+1
f.write("-----------------------------------------------------------------------------------------------------------"+ "\n")
#####################################################################"""
moy= moy/28
f1.write('average of error: ' + str(moy)+ '\n' )
f1.write('\n')
f1.write('Error min: ' +str(Min)+ '\n')
f1.write('\n')
f1.write('Error max: ' +str(Max)+'\n')
f1.write('\n')
pe= (pe * 100) /(28)
f1.write('error percentage: '+ str(pe) +'%'+'\n')
f1.write("-----------------------------------------------------------------------------------------------------------"+"\n")
############################################################################################################

f.write("                                           I4MAT Memory Test                                                             "+"\n")
#######################################################################################################################################
f1.write("                                           I4MAT Memory Test                                                              "+"\n")
Min=float(l1[i+1]) - float(l2[i+1])
Max=float(l1[i+1]) - float(l2[i+1])
moy =0
pe=0
##########################################################################################################


while(i<167):

	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
	l4c = float(l7[i]) - float(l8[i])
	l5c = float(l9[i]) - float(l10[i])
	l6c = float(l11[i]) - float(l12[i])
	l7c = float(l13[i]) - float(l14[i])
	###########################################################################
	if minn(l1c , l2c ,l3c, l4c, l5c,l6c, l7c) < Min:
		Min = minn(l1c , l2c ,l3c, l4c, l5c, l6c, l7c)
	if maxx(l1c , l2c ,l3c ,l4c,l5c ,l6c, l7c) > Max:
		Max = maxx(l1c , l2c ,l3c, l4c, l5c , l6c, l7c)
	if (l1c!=0) or (l2c!=0) or (l3c!=0) or (l4c!=0) or (l5c!=0) or(l6c!=0) or (l7c!=0) :
		pe= pe+1
		moy= l1c + l2c + l3c + l4c +l5c+ +l6c +l7c + moy	
	######################################################################"""""
	a = ""
	b= ""
	c=""
	o=""
	k=""
	h=""
	d= len(str(l1c))
	x= len(str(l2c))
	y= len(str(l3c))
	g= len(str(l4c))
	u= len(str(l5c))
	p = len(str(l6c))
	while(d< 15):
		d=d+1
		a = a + " "	
	while(x< 15):
		x=x+1
		b = b + " "	
	while(y< 15):
		y=y+1
		c = c + " "
	while(g< 15):
		g=g+1
		o = o + " "
	while(u< 15):
		u=u+1
		k = k + " "
	while(p< 15):
		p=p+1
		h = h + " "
	
	f.write(str(l1c) + a+"||" + str(l2c) +b+ "||" + str(l3c) + c+"||"+str(l4c)+ o+"||" +str(l5c)+ k+"||"+ str(l6c)  +h+"||"+str(l7c) + "\n")
	f.write("-----------------------------------------------------------------------------------------------------------" + "\n")
	i =i+1
f.write("-----------------------------------------------------------------------------------------------------------"+ "\n")
f.close()	
#####################################################################"""
moy= moy/84
f1.write('average of error: ' + str(moy)+ '\n' )
f1.write('\n')
f1.write('Error min: ' +str(Min)+ '\n')
f1.write('\n')
f1.write('Error max: ' +str(Max)+'\n')
f1.write('\n')
pe= (pe * 100) /(84)
f1.write('error percentage: '+ str(pe) +'%'+'\n')
f1.write("-----------------------------------------------------------------------------------------------------------"+"\n")
############################################################################################################
os.system('rm -Rf fichier1.txt fichier2.txt fichier3.txt fichier4.txt fichier5.txt fichier6.txt fichier7.txt ../../32/memory_test/fichier1.txt ../../32/memory_test/fichier2.txt ../../32/memory_test/fichier3.txt ../../32/memory_test/fichier4.txt ../../32/memory_test/fichier5.txt ../../32/memory_test/fichier6.txt ../../32/memory_test/fichier7.txt')
