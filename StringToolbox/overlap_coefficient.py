'''
reference: https://en.wikipedia.org/wiki/Overlap_coefficient
'''

from error_message import numpyImportErrorMessage
from model import MethodModel
from utils import get_n_grams
from collections import Counter

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class OC(MethodModel):
    def __init__(self, n = 1):
        self.model_type = 'similarity'
        self.n = n

    def calculator(self, string1, string2):
        n_gram1 = get_n_grams(string1, self.n)
        n_gram2 = get_n_grams(string2, self.n)
        length_common = sum((Counter(n_gram1) & Counter(n_gram2)).values())
        length1 = len(n_gram1)
        length2 = len(n_gram2)
        return length_common/min(length1, length2)

    def _compute_max_lengths(self):
        self.max_lengths = np.ones((len(self.group1), len(self.group2)))

