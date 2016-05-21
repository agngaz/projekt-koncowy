#!/usr/bin/env python
"""
Created on Sat May 21 08:32:02 2016

@author: Wojtek
"""
import numpy as np
import math
from math import log

def czebyszew(x,y):
    max=0
    i=0
    while i<len(x):
        if abs(x[i]-y[i]) > max:
            max=abs(x[i]-y[i])
        i += 1 
    return max
    
def braycurtis(x,y):
    i=0
    sum1=0
    sum2=0
    while i<len(x):
        sum1=sum1+abs(x[i]-y[i])
        sum2=sum2+abs(x[i]+y[i])
        i = i+1
    return sum1/sum2
    
def kullbackleibler(p, q):
    i=0
    while i<len(p):
        if p[i] < 0 or q[i] < 0:
            return
        i=i+1
    p = np.asarray(p, dtype=np.float)
    q = np.asarray(q, dtype=np.float)
    return np.sum(np.where(p != 0,(p-q) * np.log10(p / q), 0))