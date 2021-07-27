from error_message import numpyImportErrorMessage
from model import MethodModel
from utils import get_n_grams, tuple_to_string
from levenshtein import Levenshtein

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class ME(MethodModel):
    '''
    This class is used to calculate the mongue elkan similarity between strings.
    It measures the similarity between strings based on the similarity of n grams of
    two strings derived from other string similarity methods.

    reference: [1] Gelbukh, and Alexander. "[Lecture Notes in Computer Science] Computational Linguistics and Intelligent Text Processing Volume 5449 || Generalized Mongue-Elkan Method for Approximate Text String Comparison." 10.1007/978-3-642-00382-0.Chapter 45(2009):559-570. DOI: 10.1007/978-3-642-00382-0_45
    '''
    def __init__(self, n = 1, weighted = False, symmetry = False):
        self.model_type = 'similarity'
        self.n = n
        self.weighted = weighted
        self.symmetry = symmetry
        self.algorithm = Levenshtein()

    def calculator(self, string1, string2):
        n_gram1 = list(map(tuple_to_string, get_n_grams(string1, self.n)))
        n_gram2 = list(map(tuple_to_string, get_n_grams(string2, self.n)))
        if self.symmetry:
            return 0.5*(self._calculator_help(n_gram1, n_gram2)+self._calculator_help(n_gram2, n_gram1))
        else:
            return self._calculator_help(n_gram1, n_gram2)


    def _calculator_help(self, n_gram1, n_gram2):
        matrix = self.algorithm.fit(n_gram1, n_gram2).get_similarity()
        matrix = np.max(matrix, axis=1)
        if not self.weighted:
            return np.sum(matrix)/len(n_gram1)
        else:
            return (np.sum(matrix ** self.weighted) / len(n_gram1))**(1/self.weighted)

    def _compute_max_lengths(self):
        self.max_lengths = self.n
