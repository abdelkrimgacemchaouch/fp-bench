#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
os.system('./fd_predator_prey.sh')
os.system('./a.out %d' % (100))
os.system('./a.out %d' % (1000))
os.system('./a.out %d' % (10000))
