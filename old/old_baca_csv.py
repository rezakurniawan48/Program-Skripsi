import csv
from itertools import count
import pandas as pd
import numpy as np

data_tepat = 'Data/Tepat_waktu.csv'
data_lambat = 'Data/Terlambat.csv'

def baca(loc):
    x=[]
    with open(loc) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            x.append(row)
        x.pop(0)
    return x

def get_tepat(n):
    tepat = baca(data_tepat)
    x = tepat[n]
    return x

def get_lambat(n):
    lambat = baca(data_lambat)
    x = lambat[n]
    return x

def banyak_tepat():
    f = baca(data_tepat)
    i = 0
    for j in f:
        i = i + 1
    return i

def banyak_lambat():
    f = baca(data_lambat)
    i = 0
    for j in f:
        i = i + 1
    return i



#print(baca(data_tepat))
#print(x[0][1][2])