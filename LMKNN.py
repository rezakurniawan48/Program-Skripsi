import numpy as np
import math

class LMKNN:

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
    
    def pembagian(self, hasil):
        hasil_tepat = []
        hasil_lambat = []
        for i in hasil:
            if(i[2]=='1'):
                hasil_tepat.append(i)
            elif(i[2] == '0'):
                hasil_lambat.append(i) 
        return hasil_tepat, hasil_lambat

    def distance(self, x1, x2):
        z = 0.0
        for n in range(len(x1)) :
            z = z + ((float(x1[n]) - float(x2[n])) ** 2)
        z = math.sqrt(z)
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

        hasil_tepat, hasil_lambat = self.pembagian(hasil)
        hasil_tepat = self.pengurutan(hasil_tepat)
        hasil_lambat = self.pengurutan(hasil_lambat)        
        return hasil_tepat, hasil_lambat


    def get_hasil_klasifikasi(self, uji):
        hasil_tepat, hasil_lambat = self.rumus(uji) 
        
        a = 0.0
        b = 0.0
        for i in range(self.k) :
            a = a + float(hasil_tepat[i][1])
            b = b + float(hasil_lambat[i][1])
        
        a = a/self.k
        b = b/self.k
        
        if (a < b):
            return "1"
        elif (a > b) :
            return "0"


    def get_hasil_array(self, x_test):
        hasil = []
        for i in range(len(x_test)):
            uji = np.delete(x_test[i], 0)
            hasil.append(self.get_hasil_klasifikasi(uji))
        return hasil    


