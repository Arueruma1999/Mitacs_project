'''
------------------------------------------------------------------------------------------------------------------------
Guidance:

MBS is the class to calculate the similarity or the distance for two binary vector of the same size.
First, the method name should be given when MBS class is established.

Second, the data in size (2, len(vector)), whose first row is the i binary vector and second row is the j binary vector,
could be used to train the model with the function: self.fit(data)

Third, function self.get_answer() could be applied to see the result value, together with self.get_method() to recheck
the method name and self.get_method_type() to check the method's type(similarity or distance).

Besides, self.get_menu() could be used to see all methods name available and 'JACCARD' would be the default method in
condition of none method input or input mismatch. If self.set_method() is applied to change method, please reuse
self.fit() to do the calculation again. To save memory, data would not be saved in the MBS class. Whenever uexpected
input is received, warnings or errors would be raised.

Here is one example:

######################################################################################################################
from Measures_for_Binary_Data import MBD
import numpy as np

np.random.seed(0)
data = np.random.randint(0, 2, size=(2, 100))
print('The i and j binary vector would be the row 1 and row 2 of data seperately: ')
print(data)

method = 'JACCARD'
mbd = MBD(method)
mbd.fit(data)
print('Method: ', mbd.get_method())
print('Method type: ', mbd.get_method_type())
print('a: ', mbd.a)
print('b: ', mbd.b)
print('c: ', mbd.c)
print('d: ', mbd.d)
print('Result: ', mbd.get_answer())

print('All method available in MBD are: ')
print(mbd.get_menu())
########################################################################################################################

Reference:
[1] Choi S S ,  Cha S H ,  Tappert C C . A Survey of Binary Similarity and Distance Measures[J]. Journal of Systemics,
 Cybernetics & Informatics, 2010, 8(1):43--48.

Coded by:
Jinyu Zang∣B.Eng. Biomedical Engineering
School of Material Science and Engineering
South China University of Technology
Email: arueruma@foxmail.com

------------------------------------------------------------------------------------------------------------------------
'''


import numpy as np
import warnings

class MBD:
    def __init__(self, method='JACCARD'):

        self.method_dictionary={
            'JACCARD': self.call_JACCARD,
            'DICE': self.call_DICE,
            'CZEKANOWSKI': self.call_CZEKANOWSKI,
            '3W_JACCARD': self.call_3W_JACCARD,
            'NEI_AND_LI': self.call_NEI_AND_LI,
            'SOKAL_AND_SNEATH_I': self.call_SOKAL_AND_SNEATH_I,
            'SOKAL_AND_MICHENER': self.call_SOKAL_AND_MICHENER,
            'SOKAL_AND_SNEATH_II': self.call_SOKAL_AND_SNEATH_II,
            'ROGER_AND_TANIMOTO': self.call_ROGER_AND_TANIMOTO,
            'FAITH': self.call_FAITH,
            'GOWER_AND_LEGENDRE': self.call_GOWER_AND_LEGENDRE,
            'INTERSECTION': self.call_INTERSECTION,
            'INNERPRODUCT': self.call_INNERPRODUCT,
            'RUSSELL_AND_RAO': self.call_RUSSELL_AND_RAO,
            'HAMMING': self.call_HAMMING,
            'EUCLID': self.call_EUCLID,
            'SQUARED_EUCLID': self.call_SQUARED_EUCLID,
            'CANBERRA': self.call_CANBERRA,
            'MANHATTAN': self.call_MANHATTAN,
            'MEAN_MANHATTAN': self.call_MEAN_MANHATTAN,
            'CITYBLOCK': self.call_CITYBLOCK,
            'MINKOWSKI': self.call_MINKOWSKI,
            'VARI': self.call_VARI,
            'SIZEDIFFERENCE': self.call_SIZEDIFFERENCE,
            'SHAPEDIFFERENCE': self.call_SHAPEDIFFERENCE,
            'PATTERNDIFFERENCE': self.call_PATTERNDIFFERENCE,
            'LANCE_AND_WILLIAMS': self.call_LANCE_AND_WILLIAMS,
            'BRAY_AND_CURTIS': self.call_BRAY_AND_CURTIS,
            'HELLINGER': self.call_HELLINGER,
            'CHORD': self.call_CHORD,
            'COSINE': self.call_COSINE,
            'GILBERT_AND_WELLS': self.call_GILBERT_AND_WELLS,
            'OCHIAI_I': self.call_OCHIAI_I,
            'FORBESI': self.call_FORBESI,
            'FOSSUM': self.call_FOSSUM,
            'SORGENFREI': self.call_SORGENFREI,
            'MOUNTFORD': self.call_MOUNTFORD,
            'OTSUKA': self.call_OTSUKA,
            'MCCONNAUGHEY': self.call_MCCONNAUGHEY,
            'TARWID': self.call_TARWID,
            'KULCZYNSKI_II': self.call_KULCZYNSKI_II,
            'DRIVER_AND_KROEBER': self.call_DRIVER_AND_KROEBER,
            'JOHNSON': self.call_JOHNSON,
            'DENNIS': self.call_DENNIS,
            'SIMPSON': self.call_SIMPSON,
            'BRAUN_AND_BANQUET': self.call_BRAUN_AND_BANQUET,
            'FAGER_AND_MCGOWAN': self.call_FAGER_AND_MCGOWAN,
            'FORBES_II': self.call_FORBES_II,
            'SOKAL_AND_SNEATH_IV': self.call_SOKAL_AND_SNEATH_IV,
            'GOWER': self.call_GOWER,
            'PEARSON_I': self.call_PEARSON_I,
            'PEARSON_II': self.call_PEARSON_II,
            'PEARSON_III': self.call_PEARSON_III,
            'PEARSON_AND_HERON_1': self.call_PEARSON_AND_HERON_1,
            'PEARSON_AND_HERON_II': self.call_PEARSON_AND_HERON_II,
            'SOKAL_AND_SNEATH_III': self.call_SOKAL_AND_SNEATH_III,
            'SOKAL_AND_SNEATH_V': self.call_SOKAL_AND_SNEATH_V,
            'COLE': self.call_COLE,
            'STILES': self.call_STILES,
            'OCHIAI_II': self.call_OCHIAI_II,
            'S_YULEQ': self.call_S_YULEQ,
            'D_YULEQ': self.call_D_YULEQ,
            'YULEW': self.call_YULEW,
            'KULCZYNSKI_I': self.call_KULCZYNSKI_I,
            'TANIMOTO': self.call_TANIMOTO,
            'DISPERSON': self.call_DISPERSON,
            'HAMANN': self.call_HAMANN,
            'MICHAEL': self.call_MICHAEL,
            'GOODMAN_AND_KRUSKAL': self.call_GOODMAN_AND_KRUSKAL,
            'ANDERBERG': self.call_ANDERBERG,
            'BARONI_URBANI_AND_BUSER_I': self.call_BARONI_URBANI_AND_BUSER_I,
            'BARONI_URBANI_AND_BUSER_II': self.call_BARONI_URBANI_AND_BUSER_II,
            'PEIRCE': self.call_PEIRCE,
            'EYRAUD': self.call_EYRAUD,
            'TARANTULA': self.call_TARANTULA,
            'AMPLE': self.call_AMPLE,
        }
        self.method_type_dictionary = {
            'JACCARD': 'similarity',
            'DICE': 'similarity',
            'CZEKANOWSKI': 'similarity',
            '3W_JACCARD': 'similarity',
            'NEI&LI': 'similarity',
            'SOKAL&SNEATH_I': 'similarity',
            'SOKAL&MICHENER': 'similarity',
            'SOKAL&SNEATH_II': 'similarity',
            'ROGER&TANIMOTO': 'similarity',
            'FAITH': 'similarity',
            'GOWER&LEGENDRE': 'similarity',
            'INTERSECTION': 'similarity',
            'INNERPRODUCT': 'similarity',
            'RUSSELL&RAO': 'similarity',
            'HAMMING': 'distance',
            'EUCLID': 'distance',
            'SQUARED_EUCLID': 'distance',
            'CANBERRA': 'distance',
            'MANHATTAN': 'distance',
            'MEAN_MANHATTAN': 'distance',
            'CITYBLOCK': 'distance',
            'MINKOWSKI': 'distance',
            'VARI': 'distance',
            'SIZEDIFFERENCE': 'distance',
            'SHAPEDIFFERENCE': 'distance',
            'PATTERNDIFFERENCE': 'distance',
            'LANCE&WILLIAMS': 'distance',
            'BRAY&CURTIS': 'distance',
            'HELLINGER': 'distance',
            'CHORD': 'distance',
            'COSINE': 'similarity',
            'GILBERT&WELLS': 'similarity',
            'OCHIAI_I': 'similarity',
            'FORBESI': 'similarity',
            'FOSSUM': 'similarity',
            'SORGENFREI': 'similarity',
            'MOUNTFORD': 'similarity',
            'OTSUKA': 'similarity',
            'MCCONNAUGHEY': 'similarity',
            'TARWID': 'similarity',
            'KULCZYNSKI_II': 'similarity',
            'DRIVER&KROEBER': 'similarity',
            'JOHNSON': 'similarity',
            'DENNIS': 'similarity',
            'SIMPSON': 'similarity',
            'BRAUN&BANQUET': 'similarity',
            'FAGER&MCGOWAN': 'similarity',
            'FORBES_II': 'similarity',
            'SOKAL&SNEATH_IV': 'similarity',
            'GOWER': 'similarity',
            'PEARSON_I': 'similarity',
            'PEARSON_II': 'similarity',
            'PEARSON_III': 'similarity',
            'PEARSON&HERON_1': 'similarity',
            'PEARSON&HERON_II': 'similarity',
            'SOKAL&SNEATH_III': 'similarity',
            'SOKAL&SNEATH_V': 'similarity',
            'COLE': 'similarity',
            'STILES': 'similarity',
            'OCHIAI_II': 'similarity',
            'S_YULEQ': 'similarity',
            'D_YULEQ': 'distance',
            'YULEW': 'similarity',
            'KULCZYNSKI_I': 'similarity',
            'TANIMOTO': 'similarity',
            'DISPERSON': 'similarity',
            'HAMANN': 'similarity',
            'MICHAEL': 'similarity',
            'GOODMAN&KRUSKAL': 'similarity',
            'ANDERBERG': 'similarity',
            'BARONI_URBANI&BUSER_I': 'similarity',
            'BARONI_URBANI&BUSER_II': 'similarity',
            'PEIRCE': 'similarity',
            'EYRAUD': 'similarity',
            'TARANTULA': 'similarity',
            'AMPLE': 'similarity',

        }
        self.set_method(method)
        self.a = None
        self.b = None
        self.c = None
        self.d = None
        self.answer = None

    def fit(self, data):
        data = np.array(data)
        [m, n] = data.shape
        assert m == 2, 'Could only used for comparison for two binary vector with same length.'

        from sklearn.metrics import confusion_matrix
        [[self.d, self.c],[self.b, self.a]] = np.double(confusion_matrix(data[0], data[1]))

        call_method = self.method_dictionary.get(self.method)
        self.answer = call_method()
        return self

    def get_answer(self):
        return self.answer

    def get_menu(self):
        return self.method_dictionary.keys()

    def get_method_type(self):
        return self.method_type

    def set_method(self, method='JACCARD'):
        if method not in self.method_dictionary.keys():
            self.method = 'JACCARD'
            warnings.warn('Method not found, use JACCARD for default.')
        else:
            self.method = method
        self.method_type = self.method_type_dictionary.get(self.method)

    def get_method(self):
        return self.method

    def call_JACCARD(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c!=0, 'Divided by zero.'
        answer = a/(a+b+c)
        return answer

    def call_DICE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert 2*a+b+c!=0, 'Divided by zero.'
        answer = 2*a/(2*a+b+c)
        return answer

    def call_CZEKANOWSKI(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert 2*a+b+c!=0, 'Divided by zero.'
        answer = 2*a/(2*a+b+c)
        return answer

    def call_3W_JACCARD(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (3*a+b+c)!=0, 'Divided by zero.'
        answer = 3*a/(3*a+b+c)
        return answer

    def call_NEI_AND_LI(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert 2*a+b+c!=0, 'Divided by zero.'
        answer = 2*a/(2*a+b+c)
        return answer

    def call_SOKAL_AND_SNEATH_I(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert +2*b+2*c!=0, 'Divided by zero.'
        answer = a/(a+2*b+2*c)
        return answer

    def call_SOKAL_AND_MICHENER(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = (a+d)/(a+b+c+d)
        return answer

    def call_SOKAL_AND_SNEATH_II(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert 2*a+b+c+2*d != 0, 'Divided by zero.'
        answer = 2*(a+d)/(2*a+b+c+2*d)
        return answer

    def call_ROGER_AND_TANIMOTO(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+2*b+2*c+d != 0, 'Divided by zero.'
        answer =(a+d)/(a+2*b+2*c+d)
        return answer

    def call_FAITH(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d !=0, 'Divided by zero.'
        answer = (a+0.5*d)/(a+b+c+d)
        return answer

    def call_GOWER_AND_LEGENDRE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+0.5*(b+c)+d !=0, 'Divided by zero.'
        answer = (a+d)/(a+0.5*(b+c)+d)
        return answer

    def call_INTERSECTION(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = a
        return answer

    def call_INNERPRODUCT(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = a+d
        return answer

    def call_RUSSELL_AND_RAO(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = a/(a+b+c+d)
        return answer

    def call_HAMMING(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = b+c
        return answer

    def call_EUCLID(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = np.sqrt(b+c)
        return answer

    def call_SQUARED_EUCLID(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = np.sqrt((b+c)**2)
        return answer

    def call_CANBERRA(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = b+c
        return answer

    def call_MANHATTAN(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = b+c
        return answer

    def call_MEAN_MANHATTAN(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d !=0, 'Divided by zero.'
        answer = (b+c)/(a+b+c+d)
        return answer

    def call_CITYBLOCK(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = b+c
        return answer

    def call_MINKOWSKI(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        answer = b+c
        return answer

    def call_VARI(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = (b+c)/4/(a+b+c+d)
        return answer

    def call_SIZEDIFFERENCE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = (b+c)**2/(a+b+c+d)**2
        return answer

    def call_SHAPEDIFFERENCE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = ((a+b+c+d)*(b+c) - (b-c)**2)/(a+b+c+d)**2
        return answer

    def call_PATTERNDIFFERENCE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer  = 4*b*c/(a+b+c+d)**2
        return answer

    def call_LANCE_AND_WILLIAMS(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert 2*a+b+c != 0, 'Divided by zero.'
        answer = (b+c)/(2*a+b+c)
        return answer

    def call_BRAY_AND_CURTIS(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert 2 * a + b + c != 0, 'Divided by zero.'
        answer = (b + c) / (2 * a + b + c)
        return answer

    def call_HELLINGER(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b)*(a+c) != 0, 'Divided by zero.'
        answer = 2*np.sqrt(1-a/np.sqrt((a+b)*(a+c)))
        return answer

    def call_CHORD(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = np.sqrt(2 * (1 - a / np.sqrt((a + b) * (a + c))))
        return answer

    def call_COSINE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer =  a / ((a + b) * (a + c))
        return answer

    def call_GILBERT_AND_WELLS(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = np.log(a) - np.log(a+b+c+d) - np.log((a+b)/(a+b+c+d)) - np.log((a+c)/(a+b+c+d))
        return answer

    def call_OCHIAI_I(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = a / np.sqrt((a + b) * (a + c))
        return answer

    def call_FORBESI(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = (a+b+c+d)*a / ((a + b) * (a + c))
        return answer

    def call_FOSSUM(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = (a + b + c + d) * (a-0.5)**2 / ((a + b) * (a + c))
        return answer

    def call_SORGENFREI(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = a**2 / ((a + b) * (a + c))
        return answer

    def call_MOUNTFORD(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert 0.5*(a*b + a*c) + b*c != 0, 'Divided by zero.'
        answer = a/(0.5*(a*b + a*c) + b*c)
        return answer

    def call_OTSUKA(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = a / np.sqrt((a + b) * (a + c))
        return answer

    def call_MCCONNAUGHEY(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = (a**2 - b*c)/((a + b) * (a + c))
        return answer

    def call_TARWID(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b+c+d)*a + (a+b)*(a+c) != 0, 'Divided by zero.'
        answer = ((a+b+c+d)*a - (a+b)*(a+c))/((a+b+c+d)*a + (a+b)*(a+c))
        return answer

    def call_KULCZYNSKI_II(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = (a/2)*(2*a+b+c)/((a + b) * (a + c))
        return answer

    def call_DRIVER_AND_KROEBER(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = (a / 2) * (2 * a + b + c) / ((a + b) * (a + c))
        return answer

    def call_JOHNSON(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = a * (2 * a + b + c) / ((a + b) * (a + c))
        return answer

    def call_DENNIS(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b+c+d)*(a + b) * (a + c) != 0, 'Divided by zero.'
        answer =((a*d)-(b*c))/np.sqrt((a+b+c+d)*(a + b) * (a + c))
        return answer

    def call_SIMPSON(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert np.min([(a + b), (a + c)]) != 0, 'Divided by zero.'
        answer = a/np.min([(a + b), (a + c)])
        return answer

    def call_BRAUN_AND_BANQUET(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert np.max([(a + b), (a + c)]) != 0, 'Divided by zero.'
        answer = a / np.max([(a + b), (a + c)])
        return answer

    def call_FAGER_AND_MCGOWAN(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) != 0, 'Divided by zero.'
        answer = a/np.sqrt((a + b) * (a + c)) -  np.max([(a + b), (a + c)])/2
        return answer

    def call_FORBES_II(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b+c+d)* np.min([(a + b), (a + c)])-(a+b)*(a+c) != 0, 'Divided by zero.'
        answer = ((a+b+c+d)*a -(a+b)*(a+c))/((a+b+c+d)* np.min([(a + b), (a + c)])-(a+b)*(a+c))
        return answer

    def call_SOKAL_AND_SNEATH_IV(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b)*(a+c)*(b+d)*(c+d) != 0, 'Divided by zero.'
        answer = (a/(a+b) + a/(a+c) + d/(b+d) + d/(b+d))/4
        return answer

    def call_GOWER(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b)*(a+c)*(b+d)*(c+d) != 0, 'Divided by zero.'
        answer = (a+d)/np.sqrt((a+b)*(a+c)*(b+d)*(c+d))
        return answer

    def call_PEARSON_I(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b)*(a+c)*(b+d)*(c+d) != 0, 'Divided by zero.'
        x2 = (a+b+c+d)*(a*d - b*c)**2/((a+b)*(a+c)*(b+d)*(c+d))
        answer = x2
        return answer

    def call_PEARSON_II(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b)*(a+c)*(b+d)*(c+d) != 0, 'Divided by zero.'
        x2 = (a + b + c + d) * (a * d - b * c) ** 2 / ((a + b) * (a + c) * (b + d) * (c + d))
        answer = np.sqrt(x2/((a+b+c+d)+x2))
        return answer

    def call_PEARSON_III(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) * (b + d) * (c + d) != 0, 'Divided by zero.'
        rou = (a * d - b * c)  / np.sqrt((a + b) * (a + c) * (b + d) * (c + d))
        answer = np.sqrt(rou / ((a + b + c + d) + rou))
        return answer

    def call_PEARSON_AND_HERON_1(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) * (b + d) * (c + d) != 0, 'Divided by zero.'
        rou = (a * d - b * c) / np.sqrt((a + b) * (a + c) * (b + d) * (c + d))
        answer = rou
        return answer

    def call_PEARSON_AND_HERON_II(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (np.sqrt(a*d) + np.sqrt(b*c)) != 0, 'Divided by zero.'
        answer = np.cos(np.pi*np.sqrt(b*c)/(np.sqrt(a*d) + np.sqrt(b*c)))
        return answer

    def call_SOKAL_AND_SNEATH_III(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert b+c != 0, 'Divided by zero.'
        answer = (a+d)/(b+c)
        return answer

    def call_SOKAL_AND_SNEATH_V(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) * (b + d) * (c + d) != 0, 'Divided by zero.'
        answer = a*d/np.sqrt((a + b) * (a + c) * (b + d) * (c + d))
        return answer

    def call_COLE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a*d-b*c)**2-(a + b) * (a + c) * (b + d) * (c + d) != 0, 'Divided by zero.'
        answer = np.sqrt(2)*(a*d - b*c)/np.sqrt((a*d-b*c)**2-(a + b) * (a + c) * (b + d) * (c + d))
        return answer

    def call_STILES(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) * (b + d) * (c + d) != 0, 'Divided by zero.'
        answer = np.log10((a+b+c+d)*(np.abs(a*d - b*c) - (a+b+c+d)/2)**2/(a + b) * (a + c) * (b + d) * (c + d))
        return answer

    def call_OCHIAI_II(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a + b) * (a + c) * (b + d) * (c + d) != 0, 'Divided by zero.'
        answer = a*d/np.sqrt((a + b) * (a + c) * (b + d) * (c + d))
        return answer

    def call_S_YULEQ(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a*d+b*c != 0, 'Divided by zero.'
        answer = (a*d-b*c)/(a*d+b*c)
        return answer

    def call_D_YULEQ(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a*d+b*c != 0, 'Divided by zero.'
        answer = 2*b*c/(a*d+b*c)
        return answer

    def call_YULEW(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert np.sqrt(a*d)+np.sqrt(b*c) != 0, 'Divided by zero.'
        answer =(np.sqrt(a*d)-np.sqrt(b*c))/(np.sqrt(a*d)+np.sqrt(b*c))
        return answer

    def call_KULCZYNSKI_I(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert b+c != 0, 'Divided by zero.'
        answer = a/(b+c)
        return answer

    def call_TANIMOTO(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c != 0, 'Divided by zero.'
        answer = a/(a+b+c)
        return answer

    def call_DISPERSON(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = (a*d - b*c)/ (a+b+c+d)**2
        return answer

    def call_HAMANN(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = (a+d-b-c)/(a+b+c+d)
        return answer

    def call_MICHAEL(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+d)**2 + (b+c)**2 != 0, 'Divided by zero.'
        answer = 4*(a*d-b*c)/((a+d)**2 + (b+c)**2)
        return answer

    def call_GOODMAN_AND_KRUSKAL(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        theta = np.max([a,b])+np.max([c,d])+np.max([a,c])+np.max([b,d])
        theta_ = np.max([a+c, b+d]) + np.max([a+b, c+d])
        assert 2*(a+b+c+d)-theta_ != 0, 'Divided by zero.'
        answer = (theta-theta_)/(2*(a+b+c+d)-theta_)
        return answer

    def call_ANDERBERG(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        theta = np.max([a, b]) + np.max([c, d]) + np.max([a, c]) + np.max([b, d])
        theta_ = np.max([a + c, b + d]) + np.max([a + b, c + d])
        assert a+b+c+d != 0, 'Divided by zero.'
        answer = (theta-theta_)/2/(a+b+c+d)
        return answer

    def call_BARONI_URBANI_AND_BUSER_I(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert np.sqrt(a*d) + a+ b+c != 0, 'Divided by zero.'
        answer = (np.sqrt(a*d) + a)/(np.sqrt(a*d) + a+ b+c)
        return answer

    def call_BARONI_URBANI_AND_BUSER_II(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert np.sqrt(a * d) + a + b + c != 0, 'Divided by zero.'
        answer = (np.sqrt(a * d) + a-b-c) / (np.sqrt(a * d) + a + b + c)
        return answer

    def call_PEIRCE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert a*b + 2*b*c + c*d != 0, 'Divided by zero.'
        answer = (a*b + b*c)/ (a*b + 2*b*c + c*d)
        return answer

    def call_EYRAUD(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert (a+b)*(a+c)*(b+d)*(c+d) != 0, 'Divided by zero.'
        answer = (a+b+c+d)**2*((a+b+c+d)*a-(a+b)*(a+c))/((a+b)*(a+c)*(b+d)*(c+d))
        return answer

    def call_TARANTULA(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert c*(a+b), 'Divided by zero.'
        answer = a*(c+d)/(c*(a+b))
        return answer

    def call_AMPLE(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        assert c * (a + b), 'Divided by zero.'
        answer = np.abs(a * (c + d) / (c * (a + b)))
        return answer
