from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class Hamming(MethodModel):
    '''
    This class is used to calculate the hamming distance between strings.
    For two ordered sequence, the value of hamming distance is the number of the
    characters they differ.

    reference: https://www.sciencedirect.com/topics/engineering/hamming-distance
    '''
    def __init__(self):
        self.model_type = 'distance'

    def calculator(self, string1, string2):
        distance = 0
        for i in range(np.minimum(len(string1), len(string2))):
            if string1[i] != string2[i]:
                distance+=1
        distance += np.abs(len(string1)-len(string2))
        return distance