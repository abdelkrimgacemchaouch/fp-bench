#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
f=open('../../comparaison/fem1d/comparison.txt','w')
f641= open('641.txt','w')
f321= open('321.txt','w')
f642= open('642.txt','w')
f322= open('322.txt','w')
f643= open('643.txt','w')
f323= open('323.txt','w')
f644= open('644.txt','w')
f324= open('324.txt','w')

f1=open('resultat.txt','r')
f2=open('../../32/fem1d/resultat.txt','r')
i = 0 
l1 = f1.readlines()
l2 = f2.readlines()
while ('ALEFT' not in l1[i]):
	i= i +1

i= i+2
z=i+5
while(i < z):
	f641.write(l1[i][18:27]+ "\n")
	f321.write(l2[i][18:27]+ "\n")
	f642.write(l1[i][33:44]+ "\n")
	f322.write(l2[i][33:44]+ "\n")
	f643.write(l1[i][49:60]+ "\n")
	f323.write(l2[i][49:60]+ "\n")
	f644.write(l1[i][66:72]+ "\n")
	f324.write(l2[i][66:72]+ "\n")	
	i= i+1
f641.close()
f642.close()
f643.close()
f644.close()
f321.close()
f322.close()
f323.close()
f324.close()
f641= open('641.txt','r')
f321= open('321.txt','r')
f642= open('642.txt','r')
f322= open('322.txt','r')
f643= open('643.txt','r')
f323= open('323.txt','r')
f644= open('644.txt','r')
f324= open('324.txt','r')
l641 = f641.readlines()
l321 = f321.readlines()
l642 = f642.readlines()
l322 = f322.readlines()
l643 = f643.readlines()
l323 = f323.readlines()
l644 = f644.readlines()
l324 = f324.readlines()
z= i+5 
i=0
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

f.write("------------------------------------------------------------------------"+"\n")
f.write("--------------------- comparaison entre 64 et 32 -----------------------"+"\n")
Min =float(l641[0]) - float(l321[0])
Max = float(l641[0]) - float(l321[0])
moy = 0
pe =0
while(i < 5):
  	l1c = float(l641[i]) - float(l321[i])
  	l2c = float(l642[i]) - float(l322[i])
  	l3c = float(l643[i]) - float(l323[i])
 	l4c = float(l644[i]) - float(l324[i])
	if min(l1c , l2c ,l3c , l4c) < Min:
		Min = min(l1c , l2c ,l3c ,l4c)
	if max(l1c , l2c ,l3c ,l4c) > Max:
		Max = max(l1c , l2c ,l3c , l4c)
	if (l1c!=0) or (l2c!=0) or (l3c!=0) or (l4c!=0):
		pe= pe+1
		moy= l1c + l2c + l3c +l4c+ moy
	f.write(str(i+1)+"  "+ str(l1c)+"   "+str(l2c)+"   "+ str(l3c)+"  "+str(l4c)+ "  "+"\n")
	f.write("------------------------------------------------------------------------"+"\n")
		
	i=i+1
f= open('../../comparaison/fem1d/statistics.txt','w')
f.write('####################################################################################################'+'\n')
f.write('#                        statistics of comparaison between 64 and 32 data                           #'+'\n')
f.write('####################################################################################################'+'\n')
f.write('\n')
f.write('\n')
f.write('for our experience we have calculate the error x64- x32 and we have this result:' +'\n')
f.write('\n')
moy= moy/5
f.write('average of error: ' + str(moy)+ '\n' )
f.write('\n')
f.write('Error min: ' +str(Min)+ '\n')
f.write('\n')
f.write('Error max: ' +str(Max)+'\n')
f.write('\n')
pe= (pe * 100) /(5)
f.write('error percentage: '+ str(pe) +'%'+'\n')

f.close()
os.system('rm -Rf 641.txt 642.txt 643.txt 321.txt 322.txt 323.txt')
