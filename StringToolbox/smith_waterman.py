from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class SmithWaterman(MethodModel):
    '''
    This class is used to calculate the smith waterman similarity between strings.
    This method measures the similarity between strings by finding the common
    substring with the highest similarity instead of measuring the whole string.

    https://github.com/ekg/smithwaterman
    '''
    def __init__(self):
        self.model_type = 'similarity'
        self.match_point = 1.0
        self.gap_lost = -1.0

    def calculator(self, string1, string2):
        similarity_matrix = np.empty((len(string1)+1, len(string2)+1))
        for i in range(len(string1)+1):
            for j in range(len(string2)+1):
                if(i == 0 or j == 0):
                    similarity_matrix[i][j] = 0
                else:
                    if(string1[i-1]==string2[j-1]):
                        temp = self.match_point
                    else:
                        temp = 0
                    similarity_matrix[i][j] = np.max([similarity_matrix[i-1][j]+self.gap_lost, similarity_matrix[i][j-1]+self.gap_lost, similarity_matrix[i-1][j-1]+temp])
        return similarity_matrix[-1][-1]



    def _compute_max_lengths(self):
        lengths1 = np.array(list((map(len, self.group1)))).reshape(-1, 1)
        lengths2 = np.array(list((map(len, self.group2)))).reshape(1, -1)
        self.max_lengths = np.minimum(lengths1, lengths2)


