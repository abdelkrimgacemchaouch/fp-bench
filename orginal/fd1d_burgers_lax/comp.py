#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
f50=open('../../comparaison/fd1d_burgers_lax/comparison.txt','w')#stocker la comparaison
fi=open('tab.txt','w')#stoker le rustat sans blabla
fi1=open('../../32/fd1d_burgers_lax/tab.txt','w')
f1=open ('t.txt','r')# fichier de rusltat avec tous ses blala
f2=open ('../../32/fd1d_burgers_lax/t.txt','r')
f641=open('641.txt','w')
f642=open('642.txt','w')
f643=open('643.txt','w')
f644=open('644.txt','w')
f645=open('645.txt','w')
f321=open('../../32/fd1d_burgers_lax/321.txt','w')
f322=open('../../32/fd1d_burgers_lax/322.txt','w')
f323=open('../../32/fd1d_burgers_lax/323.txt','w')
f324=open('../../32/fd1d_burgers_lax/324.txt','w')
f325=open('../../32/fd1d_burgers_lax/325.txt','w')

l = f1.readlines()
l1 =f2.readlines()
i = 0
#########################################
while ( 'STABILITY' not in l[i] ):
	i = i+1
i =i+2
while (i <1176 ):
	if ('STEP'  in l[i] ):
		i = i+4
		fi.write(l[i])        ######################## stoker les vrais resultat
		fi1.write(l1[i])
	else:
		fi.write(l[i])		
		fi1.write(l1[i])
		i =i+1

fi.close()
fi1.close()
#########################################
f=open ('tab.txt','r')
f1=open ('../../32/fd1d_burgers_lax/tab.txt','r')
l= f.readlines()
l1= f1.readlines()
f.close()
f1.close()
fi=open ('tab.txt','w')
f1=open ('../../32/fd1d_burgers_lax/tab.txt','w')
i= 0 
while(i< 889):
	if (len(l[i])==1):	
		
		fi.write(l[i+1])
		f1.write(l1[i+1])
	else:
		fi.write(l[i])
		f1.write(l1[i])
	i= i+1
fi.close()
f1.close()
###################################################################
# récuperation des données fin					  #
###################################################################
f=open ('tab.txt','r')
f1=open ('../../32/fd1d_burgers_lax/tab.txt','r')
l= f.readlines()
l1= f1.readlines()
f.close()
f1.close()
i = 0
while(i < 889):
		f641.write(l[i][4:16]+"\n")
		f321.write(l1[i][4:16]+"\n")
		f642.write(l[i][22:32]+"\n")
		f322.write(l1[i][22:32]+"\n")
		f643.write(l[i][37:48]+"\n")
		f323.write(l1[i][37:48]+"\n")
		f644.write(l[i][55:64]+"\n")
		f324.write(l1[i][55:64]+"\n")
		f645.write(l[i][70:80]+"\n")
		f325.write(l1[i][70:80]+"\n")
		
		i= i+1
f641.close()
f321.close()
f642.close()
f322.close()
f643.close()
f323.close()
f644.close()
f324.close()
f645.close()
f325.close()
############################################################
# decoupage des nombres fin
############################################################
f641=open('641.txt','r')
f642=open('642.txt','r')
f643=open('643.txt','r')
f644=open('644.txt','r')
f645=open('645.txt','r')
f321=open('../../32/fd1d_burgers_lax/321.txt','r')
f322=open('../../32/fd1d_burgers_lax/322.txt','r')
f323=open('../../32/fd1d_burgers_lax/323.txt','r')
f324=open('../../32/fd1d_burgers_lax/324.txt','r')
f325=open('../../32/fd1d_burgers_lax/325.txt','r')
l641 = f641.readlines()
l321 = f321.readlines()
l642 = f642.readlines()
l322 = f322.readlines()
l643 = f643.readlines()
l323 = f323.readlines()
l644 = f644.readlines()
l324 = f324.readlines()
l645 = f645.readlines()
l325 = f325.readlines()
##########  MIN  ######################################################
def min(a, b, c, d, e) :
    l = [a, b, c, d, e]
    
    Min= l[0]
    for i in range(len(l)):
	if Min > l[i]:
		Min = l[i]
    return Min

		 
##########################################################################
##########  MAX  ######################################################
def max(a, b, c, d, e) :
    tab1 = [a, b, c, d, e]
    
    Max= tab1[0]
    for i in range(len(tab1)):
	if Max < tab1[i]:
		Max = tab1[i]
    return Max	 
##########################################################################

i=0
step = 0
##########################################################################################################################
f= open('../../comparaison/fd1d_burgers_lax/statistics.txt','w')
f.write('####################################################################################################'+'\n')
f.write('#                        statistics of comparaison between 64 and 32 data                          #'+'\n')
f.write('####################################################################################################'+'\n')
f.write('\n')
f.write('\n')
f.write('for our experience we have calculate the error x64- x32 for each step and we have this result:' +'\n')

#########################################################################################################################
f50.write("--------------------------------------------------------------------"+"\n")
f50.write('step :  ' + str(step)+"\n")
moyg= 0
moys= 0
pe=0
Is=0
ig=0
pes=0
Maxg=  float(l641[1]) - float(l321[1])
Maxs=  float(l641[1]) - float(l321[1])
Ming=  float(l641[1]) - float(l321[1])
Mins=  float(l641[1]) - float(l321[1])
while (i<889):
	if(len(l642[i])==1):
		step = step +1
		f50.write("--------------------------------------------------------------------"+"\n")
		f50.write('step :  ' + str(step)+"\n")
		###################fichier de statistique###########################################
		f.write ("--------------------------------------------------------------------"+"\n")
		f.write('\n')
		moys= moys/Is
		pes = (pes*100)/Is
		f.write('average of error: ' + str(moys)+ '\n' )
		f.write('\n')
		f.write('Error min: ' +str(Mins)+ '\n')
		f.write('\n')
		f.write('Error max: ' +str(Maxs)+'\n')
		f.write('\n')
		f.write('error percentage: '+ str(pes) +'%'+'\n')
		moys= 0
		if step < 81 :
			Maxs=  float(l641[i+1]) - float(l321[i+1])
			Mins=  float(l641[1+i]) - float(l321[i+1])
		pes= 0
		Is= 0
		f.write('step :  ' + str(step)+"\n")
		f.write ("--------------------------------------------------------------------"+"\n")
		######################################################################################
	else:
		l1 = float(l641[i]) - float(l321[i])
		l2 = float(l642[i]) - float(l322[i])
		l3 = float(l643[i]) - float(l323[i])
		l4 = float(l644[i]) - float(l324[i])	
		l5 = float(l645[i]) - float(l325[i])
		####################### claculer le min/max et moyenne pourcentage erreur###########################
		if Mins > min(l1, l2, l3, l4, l5):
			Mins=min(l1, l2, l3, l4, l5)
		if Ming > min(l1, l2, l3, l4, l5):
			Ming=min(l1, l2, l3, l4, l5)
		if Maxs < max(l1, l2, l3, l4, l5):
			Maxs=max(l1, l2, l3, l4, l5)
		if Maxg < max(l1, l2, l3, l4, l5):
			Maxg=max(l1, l2, l3, l4, l5)
		if (l1!=0) or (l2!=0) or (l3!=0) or(l4!=0) or (l5!=0):
			pe= pe+1
			pes= pes +1
			moyg= l1 + l2 + l3 + l4 + l5 +moyg
			moys= l1 + l2 + l3 + l4 + l5 +moys
		Is = Is+1 		
		##########################################################################################
		f50.write(str(l1)+"        "+str(l2) + "    " +str(l3)+"        "+str(l4) + "    "+str(l5)+"\n") 
	i =i+1
moyg = moyg/889
pe = (pe*100)/889
f.write('           the total satatistic are : ' '\n')
f.write('average of error: ' + str(moyg)+ '\n' )
f.write('\n')
f.write('Error min: ' +str(Ming)+ '\n')
f.write('\n')
f.write('Error max: ' +str(Maxg)+'\n')
f.write('\n')

f.write('error percentage: '+ str(pe) +'%'+'\n')

f.close()
os.system('rm -Rf 641.txt 642.txt 643.txt 644.txt 645.txt  ../../32/fd1d_burgers_lax/322.txt  ../../32/fd1d_burgers_lax/323.txt  ../../32/fd1d_burgers_lax/324.txt  ../../32/fd1d_burgers_lax/325.txt  ../../32/fd1d_burgers_lax/321.txt  tab.txt ../../32/fd1d_burgers_lax/tab.txt')
