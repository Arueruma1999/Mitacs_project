import numpy as np
from collections import Counter
from mutual_information import MI
from dice_coefficient import DC
from cooccurrence_over_distance import COD
from weighted_sum_of_occurrence import WSO
from utils import get_n_grams
from mongue_elkan import ME
from ratcliff_obershelp import RO
from longest_common_string import LCString
import textdistance as td

if __name__ == '__main__':
    '''
    my_list = list(zip([1,1,2,4], [2,2,3,2]))
    b = {}.fromkeys(my_list).keys()
    myset = set(my_list)  # myset是另外一个列表，里面的内容是mylist里面的无重复 项
    for item in myset:
        print("the %s has found %d" % (str(item), my_list.count(item)))


    print(list(zip([1,1,2,4], [2,2,3,2])))
    '''
    '''
    lcs = LCString()



    lvs = RO()
    str1 = 'MATHEMATICS'
    str2 = 'MATEMATICA'
    print(lcs.get_common_string(str1, str2))
    print(len(""))


    lvs.fit(str1, str2)
    answers2 = lvs.get_similarity()
    print(answers2)
    print("package td result is: ", td.RatcliffObershelp().similarity(str1, str2))
    # print(get_n_grams('helloworld', 2))

    n_gram1 = get_n_grams(str1, 1)
    n_gram2 = get_n_grams(str2, 1)
    length_common = (Counter(set(n_gram1)) | Counter(n_gram2))
    '''

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



