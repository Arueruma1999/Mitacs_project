'''
https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
'''
from jaro import Jaro

class JaroWinkler(Jaro):
    def __init__(self):
        self.model_type = 'similarity'
        self.Winkler = True