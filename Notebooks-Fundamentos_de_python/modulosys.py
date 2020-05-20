# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 10:48:04 2018

@author: bfu0
"""
import sys
print("Numero de parametros: %d \n" % len(sys.argv))
for i, p in enumerate(sys.argv):
    print("Parametro %d = %s" % (i,p))