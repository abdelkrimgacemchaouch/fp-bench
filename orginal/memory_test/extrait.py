#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
f=open('resultat.txt','w')
f1=open('t.txt','r')
l = f1.readlines()
i =0
while('I4VEC Memory Test' not in l[i]):	
	i = i+1 
a = i
while (i<208):
	if ( 'I4VEC Memory Test' in l[i]) :
		#l[i] = l[i+4]
		i = i+4
	if('R4VEC Memory Test' in l[i+1]) or ('R8VEC Memory Test' in l[i+1]) or('I4MAT Memory Test' in l[i+1]) or ('R4MAT Memory Test' in l[i+1] or 'R8MAT Memory Test' in l[i+1]):
		i = i+5
	
	
	else: 
		i = i+1	
	f.write(l[i])
f.close()
f=open('resultat.txt','r')
i = 0
l = f.readlines()
f.close()
f = open ('resultat.txt','w') 
while(i < 173):
	if (len(l[i])==1):
		f.write(l[i+1])
		i =i+2
	else:
		f.write(l[i])
		i = i+1
	
f.close ()
f1.close ()
f=open('resultat.txt','r')
l = f.readlines()
f1=open('fichier1.txt','w')
f2=open('fichier2.txt','w')
f3=open('fichier3.txt','w')
f4=open('fichier4.txt','w')
f5=open('fichier5.txt','w')
f6=open('fichier6.txt','w')
f7=open('fichier7.txt','w')
i=0
while (i<167):
	l1 = l[i][0:7]
	f1.write(l1 + "\n")
	l2 = l[i][11:20]
	f2.write(l2 + "\n")	
	i =i+1
a= 0
while(a<83):
	l3 = l[a][21:26] 
	f3.write(l3 + "\n")
	l4 = l[a][30:38]
	f4.write(l4 + "\n")
	l5 = l[a][49]
	f5.write(l5 + "\n")
	l6 = l[a][50]
	f6.write("\n")
	f7.write("\n")		
	a=a+1
while(a<167):
	l3 = l[a][29:34] 
	f3.write(l3 + "\n")
	l4 = l[a][42:48]
	f4.write(l4 + "\n")
	l5 = l[a][50:55]
	f5.write(l5 + "\n")
	l6 = l[a][59:67]
	f6.write(l6 +"\n")
	l7 = l[a][77]
	f7.write(l7 +"\n")	
	a=a+1

