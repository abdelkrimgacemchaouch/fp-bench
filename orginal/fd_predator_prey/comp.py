#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
#################################################################################################
# comparaison des resutat de 64 bit avec les reference
#################################################################################################
#########################
#comparaison 100
#########################
os.system('python a.py')
os.system('javac modi.java')
os.system('java modi')
f=open('../../comparaison/fd_predator_prey/comparison64_100.txt','w')
f1=open('./rf1_100.txt','r')
f2=open('./trf1_100.txt','r')
####################################
f3=open('./rf2_100.txt','r')
f4=open('./trf2_100.txt','r')
###################################
f5=open('./rf3_100.txt','r')
f6=open('./trf3_100.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
f.write("--------------------------------------------------------------------------------------"+"\n")
f.write("--------------------------- comparaison 64 avec refernece 100 ------------------------"+"\n")
for i in range(100):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
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
	
	f.write(str(l1c) + a+"||" + str(l2c) + b + "||" + str(l3c) +"\n")
	f.write("--------------------------------------------------------------------------------------"+"\n")
f.close()	
#########################
#comparaison 1000
#########################
os.system('javac modi1000.java')
os.system('java modi1000')
f=open('../../comparaison/fd_predator_prey/comparison64_1000.txt','w')
f1=open('./rf1_1000.txt','r')
f2=open('./trf1_1000.txt','r')
####################################
f3=open('./rf2_1000.txt','r')
f4=open('./trf2_1000.txt','r')
###################################
f5=open('./rf3_1000.txt','r')
f6=open('./trf3_1000.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
f.write("--------------------------------------------------------------------------------------"+"\n")
f.write("--------------------------- comparaison 64 avec refernece 1000 -----------------------"+"\n")
for i in range(1000):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
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
	f.write(str(l1c) + a+ "||" + str(l2c) + b + "||" + str(l3c) +"\n")
	f.write("--------------------------------------------------------------------------------------"+"\n")
f.close()	
#########################
#comparaison 10000
#########################
os.system('javac modi10000.java')
os.system('java modi10000')
f=open('../../comparaison/fd_predator_prey/comparison64_10000.txt','w')
f1=open('./rf1_10000.txt','r')
f2=open('./trf1_10000.txt','r')
####################################
f3=open('./rf2_10000.txt','r')
f4=open('./trf2_10000.txt','r')
###################################
f5=open('./rf3_10000.txt','r')
f6=open('./trf3_10000.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
f.write("--------------------------------------------------------------------------------------"+"\n")
f.write("--------------------------- comparaison 64 avec refernece 10000-----------------------"+"\n")
for i in range(10000):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
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
	f.write(str(l1c) + a+ "||" + str(l2c) + b + "||" + str(l3c) +"\n")
	f.write("--------------------------------------------------------------------------------------"+"\n")
f.close()
os.system('rm -Rf trf1_100.txt trf2_100.txt trf3_100.txt  rf1_1000.txt rf2_1000.txt rf3_1000.txt trf1_1000.txt trf2_1000.txt trf3_1000.txt  rf1_1000.txt rf2_1000.txt rf3_1000.txt trf1_10000.txt trf2_10000.txt trf3_10000.txt  rf1_10000.txt rf2_10000.txt rf3_10000.txt')
#################################################################################################
# comparaison des resutat de 32 bit avec les reference
#################################################################################################
#########################
#comparaison 100
#########################
os.chdir('../../32/fd_predator_prey/')
os.system('python a.py')
os.system('javac modi.java')
os.system('java modi')
f=open('../../comparaison/fd_predator_prey/comparison32_100.txt','w')
f1=open('./rf1_100.txt','r')
f2=open('./trf1_100.txt','r')
####################################
f3=open('./rf2_100.txt','r')
f4=open('./trf2_100.txt','r')
###################################
f5=open('./rf3_100.txt','r')
f6=open('./trf3_100.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
f.write("--------------------------------------------------------------------------------------"+"\n")
f.write("--------------------------- comparaison 32 avec refernece 100 ------------------------"+"\n")
for i in range(100):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
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
	f.write(str(l1c) + a+ "||" + str(l2c) + b + "||" + str(l3c) +"\n")
	f.write("--------------------------------------------------------------------------------------"+"\n")
f.close()	
#########################
#comparaison 1000
#########################
os.system('javac modi1000.java')
os.system('java modi1000')
f=open('../../comparaison/fd_predator_prey/comparison32_1000.txt','w')
f1=open('./rf1_1000.txt','r')
f2=open('./trf1_1000.txt','r')
####################################
f3=open('./rf2_1000.txt','r')
f4=open('./trf2_1000.txt','r')
###################################
f5=open('./rf3_1000.txt','r')
f6=open('./trf3_1000.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
f.write("--------------------------------------------------------------------------------------"+"\n")
f.write("--------------------------- comparaison 32 avec refernece 1000------------------------"+"\n")
for i in range(1000):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
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
	f.write(str(l1c) + a+ "||" + str(l2c) + b + "||" + str(l3c) +"\n")
	f.write("--------------------------------------------------------------------------------------"+"\n")
f.close()	
#########################
#comparaison 10000
#########################
os.system('javac modi10000.java')
os.system('java modi10000')
f=open('../../comparaison/fd_predator_prey/comparison32_10000.txt','w')
f1=open('./rf1_10000.txt','r')
f2=open('./trf1_10000.txt','r')
####################################
f3=open('./rf2_10000.txt','r')
f4=open('./trf2_10000.txt','r')
###################################
f5=open('./rf3_10000.txt','r')
f6=open('./trf3_10000.txt','r')
l1 = f1.readlines()
l2 = f2.readlines()
###########################
l3 = f3.readlines()
l4 = f4.readlines()
###########################
l5 = f5.readlines()
l6 = f6.readlines()
###########################
f.write("--------------------------------------------------------------------------------------"+"\n")
f.write("--------------------------- comparaison 32 avec refernece 1000 -----------------------"+"\n")
for i in range(10000):
	l1c = float(l1[i]) - float(l2[i])
	l2c = float(l3[i]) - float(l4[i])
	l3c = float(l5[i]) - float(l6[i])
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
	f.write(str(l1c) + a+ "||" + str(l2c) + b + "||" + str(l3c) +"\n")
	f.write("--------------------------------------------------------------------------------------"+"\n")
f.close()	
	
os.system('rm -Rf trf1_100.txt trf2_100.txt trf3_100.txt  rf1_1000.txt rf2_1000.txt rf3_1000.txt trf1_1000.txt trf2_1000.txt trf3_1000.txt  rf1_1000.txt rf2_1000.txt rf3_1000.txt trf1_10000.txt trf2_10000.txt trf3_10000.txt  rf1_10000.txt rf2_10000.txt rf3_10000.txt')
