import numpy as np

class KNN:
    
    def __init__(self, k):
        self.k = k

    def set_dataset(self, data, target):
        self.data = data
        self.target = target

    def pengurutan(self, hasil):
        n = len(hasil)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if (hasil[j][1] >  hasil[j+1][1]):
                    hasil[j], hasil[j + 1] = hasil[j + 1], hasil[j]
        return hasil

    def distance(self, x1, x2):
        z = 0.0
        for n in range(len(x1)) :
            z = z + ((float(x1[n]) - float(x2[n])) ** 2)
        z = z / len(x1)
        return z

    def rumus (self, uji):
        hasil = []

        for i in range(len(self.target)) :
            x_id = self.data[i][0]
            x_data = np.delete(self.data[i], 0)
            jarak = self.distance(uji, x_data)
            x_target = self.target[i]
            
            temp = [x_id, jarak, x_target]
            hasil.append(temp)
        hasil = self.pengurutan(hasil)
                    
        return hasil

    def get_hasil_klasifikasi(self, uji):
        perhitungan = self.rumus(uji)
        a = 0
        b = 0
        for i in range(self.k) :
            if (perhitungan[i][2] == '1'):
                a += 1
            elif (perhitungan[i][2] == '0') :
                b +=1
            
        if (a > b):
            return "1"
        elif (a < b) : 
            return "0"
        else :
            if (perhitungan[0][2] == '1'):
                return "1"
            else :
                return "0"

    def get_hasil_array(self, x_test):
        hasil = []
        for i in range(len(x_test)):
            uji = np.delete(x_test[i], 0)
            hasil.append(self.get_hasil_klasifikasi(uji))
        return hasil