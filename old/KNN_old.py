import baca_csv as baca


def dist(uji, dataset):
    z = 0.0
    for n in range(len(uji)) :
        z = z + ((float(uji[n]) - float(dataset[n])) ** 2)
    z = z / len(uji)
    return z

def rumus (uji):
    hasil = []

    a = baca.banyak_tepat()
    for i in range(a) :
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
            
    
    b = baca.banyak_lambat()
    for i in range(b) :
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
    perhitungan = rumus(uji)
    
    a = 0
    b = 0
    for i in range(k) :
        if (perhitungan[i][0][0] == 'A'):
            a += 1
        else : b +=1
    
    if (a > b):
        return "Tepat Waktu"
    elif (a < b) : 
        return "Tidak Tepat Waktu"
    else :
        if (perhitungan[0][0][0] == 'A'):
            return "Tepat Waktu"
        else :
            return "Tidak Tepat Waktu"

    


#uji = [3.62,3.09,3.52,3.87,3.11,3.64]
#uji2 = ['A1',3.76,3.26,3.67,3.59,3.83,3.74]
#print(get_hasil(uji,3))

