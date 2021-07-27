from error_message import numpyImportErrorMessage
from model import MethodModel
from utils import get_n_grams
from collections import Counter

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class JC(MethodModel):
    '''
    This class is used to calculate the jaccard coefficient between strings.
    The jaccard coefficient measures the similarity of the substrings components
    of the two strings.

    reference: [1] Thada, V. , and  D. V. Jaglan . "Comparison of Jaccard, Dice, Cosine Similarity Coefficient To Find Best Fitness Value for Web Retrieved Documents Using Genetic Algorithm." International Journal of Innovations in Engineering and Technology 2.4(2013):202-205.
    '''

    def __init__(self, n = 1):
        self.model_type = 'similarity'
        self.n = n

    def calculator(self, string1, string2):
        n_gram1 = get_n_grams(string1, self.n)
        n_gram2 = get_n_grams(string2, self.n)
        length_common = sum((Counter(n_gram1) & Counter(n_gram2)).values())
        length1 = len(n_gram1)
        length2 = len(n_gram2)
        return length_common/(length1+length2-length_common)

    def _compute_max_lengths(self):
        self.max_lengths = np.ones((len(self.group1), len(self.group2)))

