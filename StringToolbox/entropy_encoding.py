from error_message import numpyImportErrorMessage
from model import MethodModel
from collections import Counter

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class EE(MethodModel):
    '''
    This class is used to calculate the entropy encoding distance
    between strings. This method measures distance between the strings
    by compressing the strings according to information entropy

    https://en.wikipedia.org/wiki/Entropy_encoding
    '''
    def __init__(self):
        self.model_type = 'distance'

    def calculator(self, string1, string2):
       len_concat = np.minimum(self._compressor(string1+string2),
                               self._compressor(string2+string1))
       len1 = self._compressor(string1)
       len2 = self._compressor(string2)
       len_max = np.maximum(len1, len2)
       len_min = np.minimum(len1, len2)
       return (len_concat-len_min)/len_max

    def _compressor(self, string):
        entropy = 1
        num_all = len(string)
        for num in Counter(string).values():
            entropy -= num/num_all*np.log2(num/num_all)
        return entropy

    def _compute_max_lengths(self):
        self.max_lengths = np.ones((len(self.group1), len(self.group2)))

