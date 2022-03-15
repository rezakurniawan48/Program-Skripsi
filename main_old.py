import baca_csv as baca

x = baca.get_tepat(0)

y = [['a','1.2'],['b','2.2']]

#print(float(y[0][1])+1)
a = 0
b = [1,2,3,4,5,6,7]
x = 0
while a > b[x]:
    x = x+1

b.insert(x,a)

#print(b)

print(float(baca.baca('Data/dataset2.csv')[0][1])+ float(baca.baca('Data/dataset2.csv')[0][0]))