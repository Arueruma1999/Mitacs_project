from error_message import numpyImportErrorMessage, inputTypeErrorMessage
from mongue_elkan import ME
from levenshtein import Levenshtein


try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class WME(ME):
    '''
        This class is used to calculate the mongue elkan similarity between strings.
        It measures the similarity between strings based on the similarity of n grams of
        two strings derived from other string similarity methods. The weighted version
        is for the improvement.

        reference: [1] Gelbukh, and Alexander. "[Lecture Notes in Computer Science] Computational Linguistics and Intelligent Text Processing Volume 5449 || Generalized Mongue-Elkan Method for Approximate Text String Comparison." 10.1007/978-3-642-00382-0.Chapter 45(2009):559-570. DOI: 10.1007/978-3-642-00382-0_45
    '''

    def __init__(self, n=1, weighted=2, symmetry=False):
        self.model_type = 'similarity'
        self.n = n
        self.weighted = weighted
        self.symmetry = symmetry
        self.algorithm = Levenshtein()