import time
import KNN, LMKNN
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import KFold

class uji:

    def __init__(self, metode, k, dataset, target):
        self.dataset = dataset
        self.target = target
        if(metode == '1'):
            self.model = LMKNN.LMKNN(k)
        elif(metode == '0'):
            self.model = KNN.KNN(k)
        
    def start_tes(self):

        fold = KFold(n_splits = 10, random_state=0, shuffle=True)

        hasil = []
        #score.append(['Uji ke', 'akurasi', 'precision', 'recall', 'f1 score'])
        index = 1


        for train_index, test_index in fold.split(self.dataset):
            start_time = time.time()

            x_train, x_test, y_train, y_test = self.dataset[train_index], self.dataset[test_index], self.target[train_index], self.target[test_index]
            
            self.model.set_dataset(x_train, y_train)
            
            y_pred = self.model.get_hasil_array(x_test)
        
            acc = round(accuracy_score(y_test, y_pred), 3)
            pre = round(precision_score(y_test, y_pred, pos_label= '1'), 3)
            rec = round(recall_score(y_test, y_pred, pos_label= '1'), 3)
            f1 = round(f1_score(y_test, y_pred, pos_label='1'), 3)
            compute_time = round((time.time() - start_time), 3)
            [tn, fp], [fn, tp] = confusion_matrix(y_test, y_pred)
            hasil.append([index, acc, pre, rec, f1, compute_time,tp,tn,fp,fn])
            index +=1

        mean = ['Rata-Rata', 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for i in range(index-1):
            for j in range(1, 10) :
                mean[j] += hasil[i][j]
            

        for i in range(1, 10):
            mean[i] = round((mean[i]/index), 3)

        hasil.append(mean)

        return hasil
