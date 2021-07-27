from utils import stringCheck
from error_message import valueErrorMessage, inputTypeErrorMessage, \
    numpyImportErrorMessage, unfitErrorMessage, modeErrorMessage

try:
    import numpy as np
except ImportError:
    raise Exception(numpyImportErrorMessage)


class MethodModel:
    def __init__(self):
        self.input_type = None
        self.group1 = None
        self.group2 = None
        self.model_type = None
        self.answers = None
        self.max_lengths = None

    def fit(self, *strings):
        self._input_type_check(strings)
        self._compute_max_lengths()
        self._fit()
        return self

    def _input_type_check(self, strings):
        if (len(strings) == 1 and len(strings[0]) > 1 and all(map(stringCheck, strings[0]))):
            self.group1 = strings[0]
            self.group2 = strings[0]
            self.input_type = "within"
        elif(len(strings) == 2):
            if(isinstance(strings[0], str)):
                temp_group1 = [strings[0]]
            elif(all(map(stringCheck, strings[0]))):
                temp_group1 = strings[0]
            else:
                raise ValueError(valueErrorMessage)
            if (isinstance(strings[1], str)):
                temp_group2 = [strings[1]]
            elif (all(map(stringCheck, strings[1]))):
                temp_group2 = strings[1]
            else:
                raise ValueError(valueErrorMessage)
            self.group1 = np.array(temp_group1)
            self.group2 = np.array(temp_group2)
            self.input_type = "between"
        else:
            raise ValueError(valueErrorMessage)


    def _compute_max_lengths(self):
        lengths1 = np.array(list((map(len, self.group1)))).reshape(-1, 1)
        lengths2 = np.array(list((map(len, self.group2)))).reshape(1, -1)
        self.max_lengths = np.maximum(lengths1, lengths2)

    def _fit(self):
        if(self.input_type == "between"):
            self.answers = np.empty((len(self.group1), len(self.group2)))
            for i, string1 in enumerate(self.group1):
                for j, string2 in enumerate(self.group2):
                    self.answers[i][j] = self.calculator(string1, string2)
        elif(self.input_type == "within"):
            self.answers = np.empty((len(self.group1), len(self.group2)))
            for i in range(len(self.group1)):
                for j in range(i+1):
                    self.answers[i][j] = self.answers[j][i] = self.calculator(self.group1[i], self.group2[j])
        else:
            raise Exception(inputTypeErrorMessage)

    def get_distance(self, mode = 'all'):
        if mode == 'all':
            if(self.model_type == "distance"):
                return self.answers
            elif(self.model_type == "similarity"):
                return self.max_lengths - self.answers
            else:
                raise Exception(unfitErrorMessage)
        elif mode == 'max':
            if (self.model_type == "distance"):
                return np.max(self.answers, axis=1)
            elif (self.model_type == "similarity"):
                return np.max(self.max_lengths - self.answers, axis=1)
            else:
                raise Exception(unfitErrorMessage)
        elif mode == 'min':
            if (self.model_type == "distance"):
                return np.min(self.answers, axis=1)
            elif (self.model_type == "similarity"):
                return np.min(self.max_lengths - self.answers, axis=1)
            else:
                raise Exception(unfitErrorMessage)
        else:
            raise(modeErrorMessage)

    def get_similarity(self, mode = 'all'):
        if mode == 'all':
            if (self.model_type == "distance"):
                return self.max_lengths - self.answers
            elif (self.model_type == "similarity"):
                return self.answers
            else:
                raise Exception(unfitErrorMessage)
        elif mode == 'max':
            if (self.model_type == "distance"):
                return np.max(self.max_lengths - self.answers, axis=1)
            elif (self.model_type == "similarity"):
                return np.max(self.answers, axis=1)
            else:
                raise Exception(unfitErrorMessage)
        elif mode == 'min':
            if (self.model_type == "distance"):
                return np.min(self.max_lengths - self.answers, axis=1)
            elif (self.model_type == "similarity"):
                return np.min(self.answers, axis=1)
            else:
                raise Exception(unfitErrorMessage)
        else:
            raise (modeErrorMessage)

    def get_normalized_distance(self, mode = 'all'):
        if mode == 'all':
            return self.get_distance()/self.max_lengths
        elif mode == 'max':
            return np.max(self.get_distance() / self.max_lengths, axis=1)
        elif mode == 'min':
            return np.min(self.get_distance() / self.max_lengths, axis=1)
        else:
            raise(modeErrorMessage)

    def get_normalized_similarity(self, mode = 'all'):
        if mode == 'all':
            return self.get_similarity() / self.max_lengths
        elif mode == 'max':
            return np.max(self.get_distance() / self.max_lengths, axis=1)
        elif mode == 'min':
            return np.min(self.get_distance() / self.max_lengths, axis=1)
        else:
            raise (modeErrorMessage)

    def get_closest_index(self, k=1):
        return np.array(list(map(lambda x: np.argpartition(x, k)[:k], self.get_normalized_distance())))



