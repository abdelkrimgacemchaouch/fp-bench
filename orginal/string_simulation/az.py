#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
f=open('../../32/string_simulation/string_data.txt','r')
f1=open('string_data.txt','r')
l = f.readlines()
l1 = f1.readlines ()
a =0
for i in range(1301):
	#print(str(len(l[i]))+ " : " + l[i])
	if(len(l[i]) == 1):
		l[i]=l[i+1]
	if(len(l1[i]) == 1):
		l1[i]=l1[i+1]
		

#	print(str(len(l[i]))+ " : " + l[i])
f.close()
f1.close()
f= open ('../../32/string_simulation/string_data.txt','w')
f1= open ('string_data.txt','w')
for i in range(1271):
	f.write(l[i])
	f1.write(l1[i])
f.close()
f1.close()

		
