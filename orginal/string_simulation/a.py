#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
os.system('./string_simulation.sh')
os.system('./a.out')
os.system('gnuplot < string_commands.txt')

