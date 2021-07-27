from error_message import numpyImportErrorMessage
from model import MethodModel
from longest_common_string import LCString

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class RO(MethodModel):
    '''
    This class is used to calculate the ratcliff obershelp similarity between strings.
    This method measures the similarity between strings by iteratively finding the
    longest common string in the remaining substring besides the longest common strings
    which have been already found.

    reference: https://ilyankou.files.wordpress.com/2015/06/ib-extended-essay.pdf
    '''
    def __init__(self):
        self.model_type = 'similarity'
        self.lcs = LCString()

    def _iteration(self, string1, string2):
        if (len(string1) != 0 and len(string2) != 0):
            common_string = self.lcs.get_common_string(string1, string2)
            if len(common_string) != 0:
                return len(common_string) \
                       + self._iteration(string1[:string1.find(common_string)],
                                         string2[:string2.find(common_string)]) \
                       + self._iteration(string1[string1.find(common_string)+len(common_string):],
                                         string2[string2.find(common_string)+len(common_string):])
            else:
                return 0
        else:
            return 0


    def calculator(self, string1, string2):
        return 2*self._iteration(string1, string2)/(len(string1) + len(string2))

    def _compute_max_lengths(self):
        self.max_lengths = np.ones((len(self.group1), len(self.group2)))





