from error_message import numpyImportErrorMessage
from model import MethodModel

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)

class Jaro(MethodModel):
    '''
    This class is used to calculate the jaro similarity between strings.
    It measures the similarity between strings using the number of the
    matched characters over matching window and the number of transpositions.

    referene:
    https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance
    https://pypi.org/project/textdistance/
    '''

    def __init__(self):
        self.model_type = 'similarity'
        self.Winkler = False

    def _compute_max_lengths(self):
        self.max_lengths = np.ones((len(self.group1), len(self.group2)))

    def calculator(self, string1, string2):
        len1 = len(string1)
        len2 = len(string2)
        halfwin = (np.max([len1, len2]))//2 - 1
        string1flag = [False]*len1
        string2flag = [False]*len2
        for i in range(len1):
            left = np.max([0, i-halfwin])
            right = np.min([len2-1, i+halfwin])
            for j in range(left, right+1):
                if (string1[i] == string2[j] and not string2flag[j]):
                    string1flag[i] = string2flag[j] = True
                    break
        commonstring1 = np.array(list(string1))[np.array(string1flag)]
        commonstring2 = np.array(list(string2))[np.array(string2flag)]

        assert len(commonstring1) == len(commonstring2), "Error occured."
        m = len(commonstring1)
        if m == 0:
            return 0.0
        t = np.sum(commonstring1 != commonstring2)//2
        answer = (m/len1+m/len2+(m-t)/m)/3
        if self.Winkler:
            answer = self._Winker_process(answer, string1, string2)
        return answer

    def _Winker_process(self, answer, string1, string2):
        if (answer <= 0.7 or len(string1) < 4 or len(string2) < 4):
            return answer
        pre = 0
        for i in range(4):
            if string1[i] == string2[i]:
                pre += 1
            else:
                break
        if (pre > 0):
            return answer + pre*0.1*(1-answer)
        else:
            return answer


