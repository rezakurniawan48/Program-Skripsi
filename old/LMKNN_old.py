import math
import baca_csv as baca

def dist(uji, dataset):
    z = 0.0
    #dataset.pop(0)
    for n in range(len(uji)) :
        z = z + ((float(uji[n]) - float(dataset[n])) ** 2)
    z = z / len(uji)
    return z


def hitung_tepat(uji):
    hasil = []
    n = baca.banyak_tepat()
    for i in range(n) :
        data = baca.get_tepat(i)
        id = data[0]
        data.pop(0)
        jarak = dist(uji, data)
        x = [id,jarak]

        if not hasil :
            hasil.insert(0,x)
        else :
            j = 0
            while (j < len(hasil)) :
                if (jarak > float(hasil[j][1])) :
                    j += 1
                else: break
            hasil.insert(j,x)
        
    return hasil

def hitung_lambat(uji):
    hasil = []
    n = baca.banyak_lambat()
    for i in range(n):
        data = baca.get_lambat(i)
        id = data[0]
        data.pop(0)
        jarak = dist(uji, data)
        x = [id,jarak]

        if not hasil :
            hasil.insert(0,x)
        else :
            j = 0
            while (j < len(hasil)) :
                if (jarak > float(hasil[j][1])) :
                    j += 1
                else: break
            hasil.insert(j,x)        
    
    return hasil

def get_hasil(uji, k):
    per_tepat = hitung_tepat(uji)
    per_lambat = hitung_lambat(uji)
    
    a = 0
    b = 0
    for i in range(k) :
        a = a + per_tepat[i][1]
        b = b + per_lambat[i][1]
    
    a = a/k
    b = b/k

    if (a < b):
        return "Tepat Waktu"
    else : return "Tidak Tepat Waktu"



#uji = [2.90,3.24,3.19,3.40,3.39,3.35]
#uji2 = ['A1',3.76,3.26,3.67,3.59,3.83,3.74]
#print(len(hitung_tepat(uji)))
#x = baca.banyak_tepat()
#print(x)
    


