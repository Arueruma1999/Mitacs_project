
from jaro import Jaro

class JaroWinkler(Jaro):
    '''
    This class is used to calculate the jaro-winkler similarity between strings.
    It measures the similarity between strings using the number of the
    matched characters over matching window and the number of transpositions.
    jaro-winkler similarity is the improvement of the jaro similarity, as
    it gives more importance to the suffix of the strings.

    https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
    '''

    def __init__(self):
        self.model_type = 'similarity'
        self.Winkler = True