'''
reference: Rodrigues, E. O., et al. "Proposal and study of statistical features for string similarity computation and classification." International Journal of Data Mining, Modelling and Management 12(2020).DOI: 10.1504/IJDMMM.2020.108731
'''

from error_message import numpyImportErrorMessage, inputTypeErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class COD(MethodModel):
    def __init__(self):
        self.model_type = 'similarity'

    def calculator(self, string1, string2):
        self.com = np.zeros((len(string1), (len(string2)//2)*2))
        for p in range(len(string1)):
            for d in range((len(string2)//2)*2):
                for k in range(min(len(string1), len(string2)-d)):
                    if (string1[p]==string1[k]==string2[k+d]):
                        self.com[p][d] += 1
        cod = np.sum(np.sum(self.com[:, 0:len(string2)//2] - self.com[:, len(string2)//2:]))
        return cod

    def _compute_max_lengths(self):
        lengths1 = np.array(list((map(len, self.group1)))).reshape(-1, 1)
        lengths2 = np.array(list((map(len, self.group2)))).reshape(1, -1)
        self.max_lengths = (np.maximum(lengths1, lengths2)//2)**2*np.maximum(lengths1, lengths2)

    def get_distance(self):
        return - self.answers

    def get_normalized_distance(self):
        return 1-self.get_normalized_similarity()

    def get_normalized_similarity(self):
        return self.get_similarity()/2/self.max_lengths + 0.5