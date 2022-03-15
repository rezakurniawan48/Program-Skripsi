import csv
import numpy as np

class baca:
    def __init__(self, lokasi):
        self.lokasi = lokasi

    def buka(self):
        data=[]
        with open(self.lokasi) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                data.append(row)
            data.pop(0)
        return data
        
    def get_data(self):
        data = self.buka()
        target= []
        for i in range(len(data)):
            target.append(data[i][7])   
            data[i].pop(7)

        target = np.array(target)
        data = np.array(data)

        return data, target



