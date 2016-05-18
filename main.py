#!/usr/bin/env python

from similaritymeasures import Similarity
import pandas as pd
import random
nofrow=10-1
nofcol=10
df = pd.read_csv('dane.csv')
row1=random.randint(0,nofrow)
row2=random.randint(0,nofrow)
while row1==row2:
    row2=random.randint(0,nofrow)
ncol=random.randint(1,nofcol)
zakres=range(0,nofcol)
col=random.sample(zakres,ncol)
x = []
y = []
i=0
while i<ncol:
    x.insert(i,df.iat[row1,col[i]])
    y.insert(i,df.iat[row2,col[i]])
    i += 1
print(x)
print(y)
measures = Similarity()
print (measures.euclidean_distance(x,y))
print (measures.jaccard_similarity(x,y))
print (measures.cosine_similarity(x,y))
print (measures.manhattan_distance(x,y))
#print (measures.minkowski_distance(x,y,3))
