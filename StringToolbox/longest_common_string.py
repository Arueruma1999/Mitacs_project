from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class LCString(MethodModel):
    '''
    This class is used to calculate the longest common substring between strings.
    Basically, it measures the similarity between strings.

    reference: https://www.programcreek.com/2015/04/longest-common-substring-java/
    '''
    def __init__(self):
        self.model_type = 'similarity'

    def calculator(self, string1, string2):
        similarity_matrix = np.empty((len(string1)+1, len(string2)+1))
        index1 = 0
        index2 = 0
        for i in range(len(string1)+1):
            for j in range(len(string2)+1):
                if(i==0 or j == 0):
                    similarity_matrix[i][j] = 0
                else:
                    if(string1[i-1]==string2[j-1]):
                        similarity_matrix[i][j] = similarity_matrix[i-1][j-1] + 1
                        if similarity_matrix[index1][index2] < similarity_matrix[i][j]:
                            index1 = i
                            index2 = j
                    else:
                        similarity_matrix[i][j] = 0
        return similarity_matrix[index1][index2]

    def get_common_string(self, string1, string2):
        similarity_matrix = np.empty((len(string1) + 1, len(string2) + 1))
        index1 = 0
        index2 = 0
        for i in range(len(string1) + 1):
            for j in range(len(string2) + 1):
                if (i == 0 or j == 0):
                    similarity_matrix[i][j] = 0
                else:
                    if (string1[i - 1] == string2[j - 1]):
                        similarity_matrix[i][j] = similarity_matrix[i - 1][j - 1] + 1
                        if similarity_matrix[index1][index2] < similarity_matrix[i][j]:
                            index1 = i
                            index2 = j
                    else:
                        similarity_matrix[i][j] = 0
        i = index1
        j = index2
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