from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class Levenshtein(MethodModel):
    '''
    This class is used to calculate the levenshtein distance between strings.
    The levenshtein distance is the minimum number of operations for one string
    to convert to another string. The operations includes: substitutions,
    insertions and deletions.

    reference: https://github.com/agnivade/levenshtein
    '''

    def __init__(self):
        self.model_type = 'distance'

    def calculator(self, string1, string2):
        distance_matrix = np.empty((len(string1)+1, len(string2)+1))
        for i in range(len(string1)+1):
            for j in range(len(string2)+1):
                if(i==0):
                    distance_matrix[i][j] = j
                elif(j == 0):
                    distance_matrix[i][j] = i
                else:
                    if(string1[i-1]==string2[j-1]):
                        temp = 0
                    else:
                        temp = 1
                    distance_matrix[i][j] = np.min([distance_matrix[i-1][j]+1, distance_matrix[i][j-1]+1, distance_matrix[i-1][j-1]+temp])
        return distance_matrix[-1][-1]




















