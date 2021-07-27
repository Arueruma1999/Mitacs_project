from error_message import numpyImportErrorMessage, inputTypeErrorMessage
from sum_of_occurrence import SO
from utils import get_n_grams
from collections import Counter

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class WSO(SO):
    '''
        This class is used to calculate the sum of occurrence between strings.
        Basically, this method measures the similarity between two distance. It calculate
        the frequency of coocurence of the n gram components between the two strings.
        The weighted version is for the improvement.

        reference: Rodrigues, E. O., et al. "Proposal and study of statistical features for string similarity computation and classification." International Journal of Data Mining, Modelling and Management 12(2020).DOI: 10.1504/IJDMMM.2020.108731
    '''

    def __init__(self, weighted = True):
        self.model_type = 'similarity'
        self.weighted = weighted