#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
fichier1 = open('t.txt','w')
os.system('cp ../data/irsmk_input ./')
p = os.system('./be> zz.txt ')
f = open('zz.txt','r')
for l in f:
	fichier1.write(l +"\n")
fichier1.write("----------------------------------------------------------------" + "\n")
f.close()
os.system('rm -Rf irsmk_input ')
os.system('cp ../data/irsmk_input50 ./')
os.system('mv irsmk_input50 irsmk_input ')
p = os.system(' ./be> zz.txt ')
f = open('zz.txt','r')
for l in f:
	fichier1.write(l +"\n")
fichier1.write("----------------------------------------------------------------" + "\n")
f.close()

os.system('rm -Rf irsmk_input ')
os.system('cp ../data/irsmk_input100 ./')
os.system('mv irsmk_input100 irsmk_input ')
p = os.system(' ./be> zz.txt ')
f = open('zz.txt','r')
for l in f:
	fichier1.write(l +"\n")
fichier1.write("----------------------------------------------------------------" + "\n")
f.close()
fichier1.close()
os.system('rm -Rf zz.txt')
