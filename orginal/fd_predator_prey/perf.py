#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
fichier1 = open('z.txt','w')
p = os.system('perf stat -e cycles -e instructions -e r530110 -e r531010 -e r532010 -e r534010 -e r538010 ./a.out 100> zz.txt 2>&1')
f = open('zz.txt','r')
for l in f:
	fichier1.write(l +"\n")
fichier1.write("----------------------------------------------------------------" + "\n")
f.close()
p = os.system('perf stat -e cycles -e instructions -e r530110 -e r531010 -e r532010 -e r534010 -e r538010 ./a.out 1000> zz.txt 2>&1')
f = open('zz.txt','r')
for l in f:
	fichier1.write(l +"\n")
fichier1.write("----------------------------------------------------------------" + "\n")
f.close()
p = os.system('perf stat -e cycles -e instructions -e r530110 -e r531010 -e r532010 -e r534010 -e r538010 ./a.out 10000> zz.txt 2>&1')
f = open('zz.txt','r')
for l in f:
	fichier1.write(l +"\n")
fichier1.write("----------------------------------------------------------------" + "\n")
f.close()
fichier1.close()
os.system('rm -Rf zz.txt')
