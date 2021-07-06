'''
reference: Rodrigues, E. O., et al. "Proposal and study of statistical features for string similarity computation and classification." International Journal of Data Mining, Modelling and Management 12(2020).DOI: 10.1504/IJDMMM.2020.108731
'''

from error_message import numpyImportErrorMessage, inputTypeErrorMessage
from model import MethodModel
from utils import get_n_grams
from collections import Counter

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class SO(MethodModel):
    def __init__(self, weighted = False):
        self.model_type = 'similarity'
        self.weighted = weighted

    def calculator(self, string1, string2):
        so = 0
        for l in range(1, len(string1)+1):
            n_gram1 = get_n_grams(string1, l)
            n_gram2 = get_n_grams(string2, l)
            for k,v in Counter(n_gram2).items():
                if k in n_gram1:
                    if self.weighted:
                        so += l*v
                    else:
                        so += v
        return so

    def _compute_max_lengths(self):
        lengths1 = np.array(list((map(len, self.group1))), dtype=int).reshape(-1, 1)
        lengths2 = np.array(list((map(len, self.group2))), dtype=int).reshape(1, -1)
        max_len = np.maximum(lengths1, lengths2)
        if self.weighted:
            self.max_lengths = (max_len+1)*max_len*(max_len+2)/6
        else:
            self.max_lengths = max_len*(max_len+1)/2

