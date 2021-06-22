'''
reference:https://gitee.com/yukio233/Machine-Learning-Algorithms-from-Scratch/blob/master/K%20Nearest%20Neighbours.py
'''
from utils import stringCheck, find_most_label

from levenshtein import Levenshtein
from error_message import numpyImportErrorMessage

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class StringKNN:
    def __init__(self, k=3, method = "Levenshtein"):
        self.k = k
        self.method = method
        self.X = None
        self.y = None
        self.normalized_distance = None
        self.method_dic = {
            "Levenshtein":Levenshtein()
        }
        if method in self.method_dic.keys():
            self.model = self.method_dic[self.method]
        else:
            print("The methods available is listed below: ")
            print(self.method_dic.keys())
            raise Exception("Please recheck the method.")

    def fit(self, X, y):
        self._input_data_check(X, y)

    def _input_data_check(self, X, y):
        if (not all(map(stringCheck, X))):
            raise Exception("Wrong input. The X input should be a list of strings.")
        elif(len(X) != len(y)):
            raise Exception("Wrong input. The dimension of X should equals to the dimension of y.")
        else:
            self.X = np.array(X)
            self.y = np.array(y)

    def predict(self, X):
        self.model.fit(X, self.X)
        self.normalized_distance = self.model.get_normalized_distance()
        nearest_labels = np.array(list(map(lambda x: self.y[np.argpartition(x, self.k)[:self.k]], self.normalized_distance)))
        prediction = np.array(list(map(find_most_label, nearest_labels.tolist())))
        return prediction

