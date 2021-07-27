from error_message import numpyImportErrorMessage
from model import MethodModel
import codecs

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class BZ2E(MethodModel):
    '''
    This class is used to calculate the burrows and wheeler transform run length
    encoding distance between strings. This method measures distance between the strings
    as the normalized length of concatenated compressed string compared with
    the lengths of compressed original strings. The compression method used here is
    BZip2

    https://en.wikipedia.org/wiki/Bzip2
    '''
    def __init__(self):
        self.model_type = 'distance'

    def calculator(self, string1, string2):
       string1 = string1.encode('utf-8')
       string2 = string2.encode('utf-8')
       len_concat = np.minimum(len(self._compressor(string1+string2)),
                               len(self._compressor(string2+string1)))
       len1 = len(self._compressor(string1))
       len2 = len(self._compressor(string2))
       len_max = np.maximum(len1, len2)
       len_min = np.minimum(len1, len2)
       return (len_concat-len_min)/len_max

    def _compressor(self, string):
        return codecs.encode(string, 'bz2_codec')[15:]

    def _compute_max_lengths(self):
        self.max_lengths = np.ones((len(self.group1), len(self.group2)))

