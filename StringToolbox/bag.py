from error_message import numpyImportErrorMessage
from model import MethodModel
from utils import get_n_grams
from collections import Counter

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class Bag(MethodModel):
    '''
    This class is used to calculate the bag coefficient between strings.
    The jaccard coefficient measures the similarity of the substrings components
    of the two strings.

    https://github.com/Yomguithereal/talisman/blob/master/src/metrics/distance/bag.js
    '''
    def __init__(self, n = 1):
        self.model_type = 'distance'
        self.n = n

    def calculator(self, string1, string2):
        n_gram1 = get_n_grams(string1, self.n)
        n_gram2 = get_n_grams(string2, self.n)
        length_common = sum((Counter(n_gram1) & Counter(n_gram2)).values())
        length1 = len(n_gram1)
        length2 = len(n_gram2)
        return max(length1, length2)-length_common

