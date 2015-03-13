#!/usr/bin/env python
# -*- coding: utf8 -*-
import os,subprocess
os.system('./fd1d_burgers_lax.sh')
os.system('./a.out > t.txt')
