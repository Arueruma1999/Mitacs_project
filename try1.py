import numpy as np

class MBD:
    def __init__(self, method='JACCARD'):
        self.method = method
        self.method_dictionary={
            'JACCARD': self.call_JACCARD,
            'DICE': '',
            'CZEKANOWSKI': '',
        }
        self.answer = self.method_dictionary.get(self.method)()
    def call_JACCARD(self):
        return 1


mbd = MBD('JACCARD')
print(mbd.answer)
