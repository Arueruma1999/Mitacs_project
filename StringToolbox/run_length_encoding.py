from error_message import numpyImportErrorMessage
from model import MethodModel
from itertools import groupby

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class RLE(MethodModel):
    '''
    This class is used to calculate the burrows and wheeler transform run length
    encoding distance between strings. This method measures distance between the strings
    as the normalized length of concatenated compressed string compared with
    the lengths of compressed original strings.

    https://en.wikipedia.org/wiki/Run-length_encoding
    '''
    def __init__(self):
        self.model_type = 'distance'

    def calculator(self, string1, string2):
       len_concat = np.minimum(len(self._compressor(string1+string2)),
                               len(self._compressor(string2+string1)))
       len1 = len(self._compressor(string1))
       len2 = len(self._compressor(string2))
       len_max = np.maximum(len1, len2)
       len_min = np.minimum(len1, len2)
       return (len_concat-len_min)/len_max

    def _compressor(self, string):
        string_compressed = []
        for char, l in groupby(string):
            num = len(list(l))
            if num>2:
                string_compressed.append(str(num)+char)
            else:
                string_compressed.append((num*char))
        return ''.join(string_compressed)

    def _compute_max_lengths(self):
        self.max_lengths = np.ones((len(self.group1), len(self.group2)))

