#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
f=open('comparison.txt','w')
f1=open('./64/fichier1_64.txt','r')
f2=open('./32/fichier1_32.txt','r')
####################################
f3=open('./64/fichier2_64.txt','r')
f4=open('./32/fichier2_32.txt','r')
###################################
f5=open('./64/fichier3_64.txt','r')
f6=open('./32/fichier3_32.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
for i in range(10000):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
	f.write(str(l1c) + " " + str(l2c) + " " + str(l3c) +"\n")
f.close()	

