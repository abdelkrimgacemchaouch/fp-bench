#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
os.system('./analemma.sh')
os.system('./a.out')
os.system('gnuplot < analemma_commands.txt')

