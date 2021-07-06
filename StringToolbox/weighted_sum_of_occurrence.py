'''
reference: Rodrigues, E. O., et al. "Proposal and study of statistical features for string similarity computation and classification." International Journal of Data Mining, Modelling and Management 12(2020).DOI: 10.1504/IJDMMM.2020.108731
'''

from error_message import numpyImportErrorMessage, inputTypeErrorMessage
from sum_of_occurrence import SO
from utils import get_n_grams
from collections import Counter

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class WSO(SO):
    def __init__(self, weighted = True):
        self.model_type = 'similarity'
        self.weighted = weighted