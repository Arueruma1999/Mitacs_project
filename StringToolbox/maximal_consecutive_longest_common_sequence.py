'''
reference: Islam, A., and D. Z. Inkpen. "Semantic similarity of short texts." Recent Advances in Natural Language Processing (2007):227--236.DOI: 10.1075/cilt.309.18isl
'''

from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class MCLCS(MethodModel):
    def __init__(self):
        self.model_type = 'similarity'

    def calculator(self, string1, string2):
        if len(string1) <= len(string2):
            string_short = string1
            string_long = string2
        else:
            string_short = string2
            string_long = string1
        while (string_short not in string_long):
            string_short = string_short[:-1]
        return len(string_short)
