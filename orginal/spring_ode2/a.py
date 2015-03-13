#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
os.system('./spring_ode2.sh')
os.system('./a.out')
os.system('gnuplot < spring_ode2_commands.txt')

