'''
reference: https://www.sciencedirect.com/topics/engineering/hamming-distance
'''
from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class Hamming(MethodModel):
    def __init__(self):
        self.model_type = 'distance'

    def calculator(self, string1, string2):
        distance = 0
        for i in range(np.minimum(len(string1), len(string2))):
            if string1[i] != string2[i]:
                distance+=1
        distance += np.abs(len(string1)-len(string2))
        return distance