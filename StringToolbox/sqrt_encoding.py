from error_message import numpyImportErrorMessage
from model import MethodModel
from collections import Counter

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class SE(MethodModel):
    '''
    This class is used to calculate the sqrt encoding distance
    between strings. This method measures distance between the strings
    as the normalized sum of square roots of the numbers of every character
    in the string.

    https://pypi.org/project/textdistance/
    '''
    def __init__(self):
        self.model_type = 'distance'

    def calculator(self, string1, string2):
       len_concat = np.minimum(sum(self._compressor(string1+string2).values()),
                               sum(self._compressor(string2+string1).values()))
       len1 = sum(self._compressor(string1).values())
       len2 = sum(self._compressor(string2).values())
       len_max = np.maximum(len1, len2)
       len_min = np.minimum(len1, len2)
       return (len_concat-len_min)/len_max

    def _compressor(self, string):
        return {char:np.sqrt(num) for char, num in Counter(string).items()}

    def _compute_max_lengths(self):
        self.max_lengths = np.ones((len(self.group1), len(self.group2)))

