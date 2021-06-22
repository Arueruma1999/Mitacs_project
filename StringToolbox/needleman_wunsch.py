'''
https://github.com/timreid/needlemanWunsch/blob/master/needleman_wunsch.py
'''
from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class NeedlemanWunsch(MethodModel):
    def __init__(self):
        self.model_type = 'similarity'
        self.match_point = 1.0
        self.gap_lost = -1.0

    def calculator(self, string1, string2):
        similarity_matrix = np.empty((len(string1)+1, len(string2)+1))
        for i in range(len(string1)+1):
            for j in range(len(string2)+1):
                if(i == 0 or j == 0):
                    similarity_matrix[i][j] = 0+self.gap_lost*(i+j)
                else:
                    if(string1[i-1]==string2[j-1]):
                        temp = self.match_point
                    else:
                        temp = 0
                    similarity_matrix[i][j] = np.max([similarity_matrix[i-1][j]+self.gap_lost, similarity_matrix[i][j-1]+self.gap_lost, similarity_matrix[i-1][j-1]+temp])
        return similarity_matrix[-1][-1]

    def fit(self, *strings):
        self._input_type_check(strings)
        self._compute_max_and_min()
        self._fit()
        return self

    def _compute_max_and_min(self):
        lengths1 = np.array(list((map(len, self.group1)))).reshape(-1, 1)
        lengths2 = np.array(list((map(len, self.group2)))).reshape(1, -1)
        self.max = np.maximum(lengths1, lengths2)
        self.min = np.maximum(lengths1, lengths2)*self.gap_lost

    def get_distance(self):
        return -self.answers

    def get_similarity(self):
        return self.answers

    def get_normalized_similarity(self):
        return (self.answers-self.min)/(self.max*2)

    def get_normalized_distance(self):
        return 1 - self.get_normalized_similarity()

