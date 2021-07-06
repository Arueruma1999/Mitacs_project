'''
reference: Rodrigues, E. O., et al. "Proposal and study of statistical features for string similarity computation and classification." International Journal of Data Mining, Modelling and Management 12(2020).DOI: 10.1504/IJDMMM.2020.108731
           http://en.wikipedia.org/wiki/Mutual_information
'''

from error_message import numpyImportErrorMessage, inputTypeErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class MI(MethodModel):
    def __init__(self):
        self.model_type = 'similarity'

    def calculator(self, string1, string2):
        length = np.min([len(string1), len(string2)])
        string1 = string1[:length+1]
        string2 = string2[:length+1]
        common_list = list(zip(string1, string2))
        MI = 0
        for common in set(common_list):
            p_common = common_list.count(common)/length
            p_1 = string1.count(common[0])/length
            p_2 = string2.count(common[1])/length
            MI += p_common*np.log(p_common/p_1/p_2)
        return MI

    def _compute_max_lengths(self):
        if (self.input_type == "between"):
            self.max_lengths = np.empty((len(self.group1), len(self.group2)))
            for i, string1 in enumerate(self.group1):
                for j, string2 in enumerate(self.group2):
                    self.max_lengths[i][j] = self.length_calculator(string1, string2)
        elif (self.input_type == "within"):
            self.answers = np.empty((len(self.group1), len(self.group2)))
            for i in range(len(self.group1)):
                for j in range(i + 1):
                    self.max_lengths[i][j] = self.max_lengths[j][i] = self.length_calculator(self.group1[i], self.group2[j])
        else:
            raise Exception(inputTypeErrorMessage)

    def length_calculator(self, string1, string2):
        length = np.min([len(string1), len(string2)])
        string1 = string1[:length + 1]
        string2 = string2[:length + 1]
        H_string1 = 0
        H_string2 = 0
        for char in set(string1):
            p = string1.count(char)/length
            H_string1 -= p*np.log(p)
        for char in set(string2):
            p = string2.count(char) / length
            H_string2 -= p * np.log(p)
        return 0.5*(H_string1+H_string2)



