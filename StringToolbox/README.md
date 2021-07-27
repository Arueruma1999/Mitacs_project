**READ ME**

StringToolbox

version: 2021.7.27

Contributor: 
Yannick Marchand (marchand@cs.dal.ca)
Jinyu Zang (Arueruma@foxmail.com)

---

## Introduction of the StringToolbox

The functions in the package mainly provide support for three parts:
1. distance(similarity) matrix for binary vectors
2. distance(similarity) matrix for strings
3. classification based on the distance matrix for strings.

## 1. Distance(Similarity) matrix for binary vectors

The package has Implemented 76 methods of distance(similarity) measurements for binary vectors as mensioned in
Choi S S ,  Cha S H ,  Tappert C C . A Survey of Binary Similarity and Distance Measures[J]. Journal of Systemics,
Cybernetics & Informatics, 2010, 8(1):43--48.

First, the method name should be given when MBD class is instantiated.

Second, the data in size (2, len(vector)), whose first row is the i binary vector and second row is the j binary vector,
could be used to train the model with the function: self.fit(data)

Third, function self.get_answer() could be applied to see the result value, together with self.get_method() to recheck
the method name and self.get_method_type() to check the method's type(similarity or distance).

Besides, self.get_menu() could be used to see all methods name available and 'JACCARD' would be the default method in
condition of none method input or input mismatch. If self.set_method() is applied to change method, please reuse
self.fit() to do the calculation again. To save memory, data would not be saved in the MBS class. Whenever uexpected
input is received, warnings or errors would be raised.

Here is one example:
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

Here is the result:
The i and j binary vector would be the row 1 and row 2 of data seperately: 
[[0 1 1 0 1 1 1 1 1 1 1 0 0 1 0 0 0 0 0 1 0 1 1 0 0 1 1 1 1 0 1 0 1 0 1 1
  0 1 1 0 0 1 0 1 1 1 1 1 0 1 0 1 1 1 1 0 1 0 0 1 1 0 1 0 1 0 0 0 0 0 1 1
  0 0 0 1 1 0 1 0 0 1 0 1 1 1 1 1 1 0 1 1 0 0 1 0 0 1 1 0]
 [1 0 0 1 0 0 0 1 1 0 1 0 0 0 0 0 1 0 1 0 1 1 1 1 1 0 1 1 1 1 0 1 1 0 0 1
  0 0 0 0 1 1 0 0 1 0 1 1 1 1 0 0 0 1 0 1 1 1 0 1 0 0 1 0 1 1 0 0 1 0 1 0
  1 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 1 0 0 0 1 0 0]]
Method:  JACCARD
Method type:  similarity
a:  25.0
b:  31.0
c:  20.0
d:  24.0
Result:  0.32894736842105265
All method available in MBD are: 
dict_keys(['JACCARD', 'DICE', 'CZEKANOWSKI', '3W_JACCARD', 'NEI_AND_LI', 'SOKAL_AND_SNEATH_I', 'SOKAL_AND_MICHENER', 'SOKAL_AND_SNEATH_II', 'ROGER_AND_TANIMOTO', 'FAITH', 'GOWER_AND_LEGENDRE', 'INTERSECTION', 'INNERPRODUCT', 'RUSSELL_AND_RAO', 'HAMMING', 'EUCLID', 'SQUARED_EUCLID', 'CANBERRA', 'MANHATTAN', 'MEAN_MANHATTAN', 'CITYBLOCK', 'MINKOWSKI', 'VARI', 'SIZEDIFFERENCE', 'SHAPEDIFFERENCE', 'PATTERNDIFFERENCE', 'LANCE_AND_WILLIAMS', 'BRAY_AND_CURTIS', 'HELLINGER', 'CHORD', 'COSINE', 'GILBERT_AND_WELLS', 'OCHIAI_I', 'FORBESI', 'FOSSUM', 'SORGENFREI', 'MOUNTFORD', 'OTSUKA', 'MCCONNAUGHEY', 'TARWID', 'KULCZYNSKI_II', 'DRIVER_AND_KROEBER', 'JOHNSON', 'DENNIS', 'SIMPSON', 'BRAUN_AND_BANQUET', 'FAGER_AND_MCGOWAN', 'FORBES_II', 'SOKAL_AND_SNEATH_IV', 'GOWER', 'PEARSON_I', 'PEARSON_II', 'PEARSON_III', 'PEARSON_AND_HERON_1', 'PEARSON_AND_HERON_II', 'SOKAL_AND_SNEATH_III', 'SOKAL_AND_SNEATH_V', 'COLE', 'STILES', 'OCHIAI_II', 'S_YULEQ', 'D_YULEQ', 'YULEW', 'KULCZYNSKI_I', 'TANIMOTO', 'DISPERSON', 'HAMANN', 'MICHAEL', 'GOODMAN_AND_KRUSKAL', 'ANDERBERG', 'BARONI_URBANI_AND_BUSER_I', 'BARONI_URBANI_AND_BUSER_II', 'PEIRCE', 'EYRAUD', 'TARANTULA', 'AMPLE'])

## 2. Distance(Similarity) matrix for strings

The package has Implemented 29 methods of distance(similarity) measurements for strings. All methods support the comparison between
one string and one string, the comparison between one string and a group of string, the comparison between a group
of string and a group of string, and the comparison within a group of string, by calling seperately:
instance.fit(one string, one string)
instance.fit(one string, one list of string)
instance.fit(one list of string, one list of string)
instance.fit(one list of string)

All methods also support to get the result of distance, similarity, normalized distance, normalized similarit by calling seperately
after the fit process:
instance.get_distance(mode)
instance.get_similarity(mode)
instance.get_normalized_distance(mode)
instance.get_normalized_similarity(mode)
where the mode could be selected as 'all'(default), 'max', 'min'. When the mode is selected as 'all', all distance results will be returned;
when the mode is selected as 'max', only the maximum value of the distance(normalized)/similarity(normalized) for each string as the
input of the first parameter will be returned; when the mode is selected as 'min', only the minimum value of the distance(normalized)
/similarity(normalized) for each string as the input of the first parameter will be returned.

Here is one example:
from levenshtein import Levenshtein
string_list1 = ["helloworld", "helloworld2", "hellosworld", "hello34world", "hellowo7rld", "hellowoxrld", "hellow1rld",
               "2helloworld",
               "goodbye", "goodezbye", "goodby3e", "good5fbye", "goodby4e", "goodbyrge", "gooderbye", "4goodbye"]
string_list2 = ["hellowor3ld", "hello1world5", "hel3loworldv", "he1llowo3rld", "goodby5e", "goodvye", "g5sdbye",
              "goo45dbye"]
lvs = Levenshtein()
lvs.fit(string_list1, string_list2)
print(lvs.get_normalized_distance('all'))

Here is the result:
[[0.09090909 0.16666667 0.16666667 0.16666667 0.9        0.9
  1.         1.        ]
 [0.18181818 0.16666667 0.16666667 0.25       0.90909091 0.81818182
  1.         0.90909091]
 [0.18181818 0.16666667 0.25       0.25       0.90909091 0.90909091
  0.90909091 0.90909091]
 [0.25       0.25       0.33333333 0.33333333 0.91666667 0.91666667
  1.         0.83333333]
 [0.18181818 0.25       0.25       0.16666667 0.90909091 0.81818182
  1.         0.90909091]
 [0.18181818 0.25       0.25       0.16666667 0.90909091 0.81818182
  1.         0.90909091]
 [0.18181818 0.25       0.25       0.25       0.9        0.9
  1.         1.        ]
 [0.18181818 0.25       0.25       0.25       0.90909091 0.90909091
  1.         1.        ]
 [0.81818182 0.83333333 0.83333333 0.83333333 0.125      0.14285714
  0.28571429 0.22222222]
 [0.90909091 0.91666667 0.91666667 0.91666667 0.33333333 0.33333333
  0.44444444 0.33333333]
 [0.81818182 0.91666667 0.91666667 0.91666667 0.125      0.25
  0.375      0.33333333]
 [0.90909091 0.91666667 0.91666667 0.91666667 0.33333333 0.33333333
  0.44444444 0.22222222]
 [0.90909091 0.91666667 0.91666667 0.91666667 0.125      0.25
  0.375      0.33333333]
 [0.90909091 0.83333333 0.91666667 0.83333333 0.22222222 0.33333333
  0.44444444 0.44444444]
 [0.81818182 0.83333333 0.83333333 0.91666667 0.33333333 0.33333333
  0.44444444 0.33333333]
 [0.81818182 0.83333333 0.83333333 0.83333333 0.25       0.25
  0.375      0.33333333]]

All methods available are:
[bag, burrows_wheeler_transform_run_length_encoding, bzip2_encoding, cooccurrence_over_distance, cosine_coefficient, damerau_levenshtein, dice_coefficient, entropy_encoding, hamming, jaccard_coefficient, jaro, jaro_winkler, levenshtein, longest_common_sequence, longest_common_string, maximal_consecutive_longest_common_sequence, mongue_elkan, mutual_information, needleman_wunsch, overlap_coefficient, ratcliff_obershelp, run_length_encoding, smith_waterman, sqrt_encoding, sum_of_occurrence, Tversky_index, weighted_mongue_elkan, 
weighted_sum_of_occurrence, zlib_encoding]


## 3. Classification Based on the Distance matrix for Strings.

The classification is mainly based on the principle of K nearest neighbors algorithm. The distance measurement method could be selected as the hyperparameter (under developing, however, only the levenshtein method is available now). 

Here is one example:
X_train = ["helloworld", "helloworld2", "hellosworld", "hello34world", "hellowo7rld", "hellowoxrld", "hellow1rld", "2helloworld",
               "goodbye", "goodezbye", "goodby3e", "good5fbye", "goodby4e", "goodbyrge", "gooderbye","4goodbye"]
X_test = ["hellowor3ld", "hello1world5", "hel3loworldv", "he1llowo3rld", "goodby5e", "goodvye", "g5sdbye", "goo45dbye"]
y_train = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
y_test = [0,0,0,0,1,1,1,1]

knn = StringKNN()
knn.fit(X_train, y_train)
prediction = knn.predict(X_test)
print(prediction)
print("accuracy = ", sum(prediction==y_test)/len(y_test))

Here is the reuslt:
[0 0 0 0 1 1 1 1]
accuracy =  1.0

---

## Third package requirement (up to now)

numpy

---