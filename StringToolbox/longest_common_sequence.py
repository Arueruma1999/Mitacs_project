'''
reference: https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
'''

from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class LCSequence(MethodModel):
    def __init__(self):
        self.model_type = 'similarity'

    def calculator(self, string1, string2):
        similarity_matrix = np.empty((len(string1)+1, len(string2)+1))
        for i in range(len(string1)+1):
            for j in range(len(string2)+1):
                if(i==0 or j == 0):
                    similarity_matrix[i][j] = 0
                else:
                    if(string1[i-1]==string2[j-1]):
                        similarity_matrix[i][j] = similarity_matrix[i-1][j-1] + 1
                    else:
                        similarity_matrix[i][j] = np.max([similarity_matrix[i-1][j], similarity_matrix[i][j-1]])
        return similarity_matrix[-1][-1]

    def get_common_sequence(self, string1, string2):
        similarity_matrix = np.empty((len(string1) + 1, len(string2) + 1))
        for i in range(len(string1) + 1):
            for j in range(len(string2) + 1):
                if (i == 0 or j == 0):
                    similarity_matrix[i][j] = 0
                else:
                    if (string1[i - 1] == string2[j - 1]):
                        similarity_matrix[i][j] = similarity_matrix[i - 1][j - 1] + 1
                    else:
                        similarity_matrix[i][j] = np.max([similarity_matrix[i - 1][j], similarity_matrix[i][j - 1]])
        i = len(string1)
        j = len(string2)
        common_sequence = []
        while(similarity_matrix[i][j] != 0):
            if similarity_matrix[i][j] == similarity_matrix[i-1][j]:
                i -= 1
                continue
            elif (similarity_matrix[i][j] == similarity_matrix[i][j-1]):
                j -= 1
                continue
            else:
                common_sequence.append(string1[i-1])
                i -= 1
                j -= 1
        return "".join(common_sequence[::-1])
