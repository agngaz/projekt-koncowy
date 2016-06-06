#!/usr/bin/env python
from similaritymeasures import Similarity
from czebyszew import czebyszew
from czebyszew import braycurtis
import pandas as pd
import random
import numpy
import scipy.stats as stats
import scipy.spatial as spatial
df = pd.read_csv('dane.csv')
nofcol=(len(df.values[0]))
nofrow=(len(df['Col 1']))-1
petla = 0
print ("Wpisz 1, aby otworzyc pierwsza wersje. Wpisz inna liczbe, aby otworzyc druga wersje.")
wersja = input()
print ("Wpisz ilosc wykonywania petli.")
ilosc = int(input())
while petla < ilosc:
    row1=random.randint(0,nofrow)
    row2=random.randint(0,nofrow)
    while row1==row2:
        row2=random.randint(0,nofrow)
    ncol=random.randint(3,nofcol)
    zakres=range(0,nofcol)
    col=random.sample(zakres,ncol)
    x = []
    y = []
    i=0
    while i<ncol:
        x.insert(i,df.iat[row1,col[i]])
        y.insert(i,df.iat[row2,col[i]])
        i += 1
    measures = Similarity()
    lista = []
    lista.insert(0,measures.euclidean_distance(x,y))
    lista.insert(1,measures.jaccard_similarity(x,y))
    lista.insert(2,measures.cosine_similarity(x,y))
    lista.insert(3,measures.manhattan_distance(x,y))
    lista.insert(4,spatial.distance.minkowski(x,y,3))
    lista.insert(5,numpy.corrcoef(x, y)[0, 1])
    lista.insert(6,stats.kendalltau(x, y)[0])
    lista.insert(7,czebyszew(x,y))
    lista.insert(8,stats.spearmanr(x, y)[0])
    lista.insert(9,braycurtis(x,y))
    lista.insert(10,numpy.correlate(x,y)[0])
    lista.insert(11,spatial.distance.canberra(x, y))
    lista.insert(12,spatial.distance.dice(x, y))
    lista.insert(13,spatial.distance.hamming(x, y))
    lista.insert(14,spatial.distance.matching(x, y))
    lista.insert(15,spatial.distance.russellrao(x, y))
    lista.insert(16,spatial.distance.sokalmichener(x, y))
    lista.insert(17,spatial.distance.sokalsneath(x, y))
    if wersja == '1':
        x=row1 
        y=row2 
    if petla == 0:
        euclideanmax=[lista[0],x,y]
        euclideanmin=[lista[0],x,y]
        jaccardmax=[lista[1],x,y]
        jaccardmin=[lista[1],x,y]
        cosinemax=[lista[2],x,y]
        cosinemin=[lista[2],x,y]
        manhattanmax=[lista[3],x,y]
        manhattanmin=[lista[3],x,y]
        minkowskimax=[lista[4],x,y]
        minkowskimin=[lista[4],x,y]
        correlpearsonmax=[lista[5],x,y]
        correlpearsonmin=[lista[5],x,y]
        kendalltaumax=[lista[6],x,y]
        kendalltaumin=[lista[6],x,y]
        czebyszewmax=[lista[7],x,y]
        czebyszewmin=[lista[7],x,y]
        spearmanmax=[lista[8],x,y]
        spearmanmin=[lista[8],x,y]
        braycurtismax=[lista[9],x,y]
        braycurtismin=[lista[9],x,y]
        correlationmax=[lista[10],x,y]
        correlationmin=[lista[10],x,y]
        canberramax=[lista[11],x,y]
        canberramin=[lista[11],x,y]
        dicemax=[lista[12],x,y]
        dicemin=[lista[12],x,y]
        hammingmax=[lista[13],x,y]
        hammingmin=[lista[13],x,y]
        matchingmax=[lista[14],x,y]
        matchingmin=[lista[14],x,y]
        russellraomax=[lista[15],x,y]
        russellraomin=[lista[15],x,y]
        sokalmichenermax=[lista[16],x,y]
        sokalmichenermin=[lista[16],x,y]
        sokalsneathmax=[lista[17],x,y]
        sokalsneathmin=[lista[17],x,y]
    else:
        if lista[0] > euclideanmax[0]:
            euclideanmax=[lista[0],x,y]
        if lista[0] < euclideanmin[0]:
            euclideanmin=[lista[0],x,y]
        if lista[1] > jaccardmax[0]:
            jaccardmax=[lista[1],x,y]
        if lista[1] < jaccardmin[0]:
            jaccardmin=[lista[1],x,y]
        if lista[2] > cosinemax[0]:
            cosinemax=[lista[2],x,y]
        if lista[2] < cosinemin[0]:
            cosinemin=[lista[2],x,y]
        if lista[3] > manhattanmax[0]:
            manhattanmax=[lista[3],x,y]
        if lista[3] < manhattanmin[0]:
            manhattanmin=[lista[3],x,y]
        if lista[4] > minkowskimax[0]:
            minkowskimax=[lista[4],x,y]
        if lista[4] < minkowskimin[0]:
            minkowskimin=[lista[4],x,y]
        if lista[5] > correlpearsonmax[0]:
            correlpearsonmax=[lista[5],x,y]
        if lista[5] < correlpearsonmin[0]:
            correlpearsonmin=[lista[5],x,y]
        if lista[6] > kendalltaumax[0]:
            kendalltaumax=[lista[6],x,y]
        if lista[6] < kendalltaumin[0]:
            kendalltaumin=[lista[6],x,y]
        if lista[7] > czebyszewmax[0]:
            czebyszewmax=[lista[7],x,y]
        if lista[7] < czebyszewmin[0]:
            czebyszewmin=[lista[7],x,y]
        if lista[8] > spearmanmax[0]:
            spearmanmax=[lista[8],x,y]
        if lista[8] < spearmanmin[0]:
            spearmanmin=[lista[8],x,y]
        if lista[9] > braycurtismax[0]:
            braycurtismax=[lista[9],x,y]
        if lista[9] < braycurtismin[0]:
            braycurtismin=[lista[9],x,y]
        if lista[10] > correlationmax[0]:
            correlationmax=[lista[10],x,y]
        if lista[10] < correlationmin[0]:
            correlationmin=[lista[10],x,y]
        if lista[11] > canberramax[0]:
            canberramax=[lista[11],x,y]
        if lista[11] < canberramin[0]:
            canberramin=[lista[11],x,y]
        if lista[12] > dicemax[0]:
            dicemax=[lista[12],x,y]
        if lista[12] < dicemin[0]:
            dicemin=[lista[12],x,y]
        if lista[13] > hammingmax[0]:
            hammingmax=[lista[13],x,y]
        if lista[13] < hammingmin[0]:
            hammingmin=[lista[13],x,y]
        if lista[14] > matchingmax[0]:
            matchingmax=[lista[14],x,y]
        if lista[14] < matchingmin[0]:
            matchingmin=[lista[14],x,y]
        if lista[15] > russellraomax[0]:
            russellraomax=[lista[15],x,y]
        if lista[15] < russellraomin[0]:
            russellraomin=[lista[15],x,y]
        if lista[16] > sokalmichenermax[0]:
            sokalmichenermax=[lista[16],x,y]
        if lista[16] < sokalmichenermin[0]:
            sokalmichenermin=[lista[16],x,y]
        if lista[17] >  sokalsneathmax[0]:
             sokalsneathmax=[lista[17],x,y]
        if lista[17] <  sokalsneathmin[0]:
             sokalsneathmin=[lista[17],x,y]
    petla += 1
print ("euclidean:\n", euclideanmax[0], euclideanmax[1], euclideanmax [2],"\n")
print (euclideanmin[0], euclideanmin[1], euclideanmin [2],"\n")
print ("jaccard:\n", jaccardmax[0], jaccardmax[1], jaccardmax [2],"\n")
print (jaccardmin[0], jaccardmin[1], jaccardmin [2],"\n")
print ("cosine:\n", cosinemax[0], cosinemax[1], cosinemax[2],"\n")
print (cosinemin[0], cosinemin[1], cosinemin [2],"\n")
print ("manhattan:\n", manhattanmax[0], manhattanmax[1], manhattanmax[2],"\n")
print (manhattanmin[0], manhattanmin[1], manhattanmin [2],"\n")     
print ("minkowski:\n", minkowskimax[0], minkowskimax[1], minkowskimax[2],"\n")
print (minkowskimin[0], minkowskimin[1], minkowskimin [2],"\n")    
print ("correlpearson:\n", correlpearsonmax[0], correlpearsonmax[1], correlpearsonmax[2],"\n")
print (correlpearsonmin[0], correlpearsonmin[1], correlpearsonmin [2],"\n")  
print ("kendalltau:\n", kendalltaumax[0], kendalltaumax[1], kendalltaumax[2],"\n")
print (kendalltaumin[0], kendalltaumin[1], kendalltaumin [2],"\n")
print ("czebyszew:\n", czebyszewmax[0], czebyszewmax[1], czebyszewmax[2],"\n")
print (czebyszewmin[0], czebyszewmin[1], czebyszewmin [2],"\n") 
print ("spearman:\n", spearmanmax[0], spearmanmax[1], spearmanmax[2],"\n")
print (spearmanmin[0], spearmanmin[1], spearmanmin [2],"\n")  
print ("braycurtis:\n", braycurtismax[0], braycurtismax[1], braycurtismax[2],"\n")
print (braycurtismin[0], braycurtismin[1], braycurtismin [2],"\n") 
print ("correlation:\n", correlationmax[0], correlationmax[1], correlationmax[2],"\n")
print (correlationmin[0], correlationmin[1], correlationmin [2],"\n")    
print ("canberra:\n", canberramax[0], canberramax[1], canberramax[2],"\n")
print (canberramin[0], canberramin[1], canberramin [2],"\n") 
print ("dice:\n", dicemax[0], dicemax[1], dicemax[2],"\n")
print (dicemin[0], dicemin[1], dicemin [2],"\n")     
print ("hamming:\n", hammingmax[0], hammingmax[1], hammingmax[2],"\n")
print (hammingmin[0], hammingmin[1], hammingmin [2],"\n")     
print ("matching:\n", matchingmax[0], matchingmax[1], matchingmax[2],"\n")
print (matchingmin[0], matchingmin[1], matchingmin [2],"\n")     
print ("russellrao:\n", russellraomax[0], russellraomax[1], russellraomax[2],"\n")
print (russellraomin[0], russellraomin[1], russellraomin [2],"\n") 
print ("sokalmichener:\n", sokalmichenermax[0], sokalmichenermax[1], sokalmichenermax[2],"\n")
print (sokalmichenermin[0], sokalmichenermin[1], sokalmichenermin [2],"\n")     
print (" sokalsneath:\n",  sokalsneathmax[0],  sokalsneathmax[1],  sokalsneathmax[2],"\n")
print ( sokalsneathmin[0],  sokalsneathmin[1],  sokalsneathmin [2],"\n")
