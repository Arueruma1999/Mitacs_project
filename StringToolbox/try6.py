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
from Tversky_index import TI
from needleman_wunsch import NeedlemanWunsch
from run_length_encoding import RLE
from burrows_wheeler_transform_run_length_encoding import BWTRLE
from sqrt_encoding import SE
from entropy_encoding import EE
from bzip2_encoding import BZ2E
from zlib_encoding import ZLE
from levenshtein import Levenshtein
from itertools import groupby
import codecs

if __name__ == '__main__':

    # help(Levenshtein)
    X_train = ["helloworld", "helloworld2", "hellosworld", "hello34world", "hellowo7rld", "hellowoxrld", "hellow1rld",
               "2helloworld",
               "goodbye", "goodezbye", "goodby3e", "good5fbye", "goodby4e", "goodbyrge", "gooderbye", "4goodbye"]
    X_test = ["hellowor3ld", "hello1world5", "hel3loworldv", "he1llowo3rld", "goodby5e", "goodvye", "g5sdbye",
              "goo45dbye"]
    y_train = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    y_test = [0, 0, 0, 0, 1, 1, 1, 1]

    lvs = ZLE()
    str1 = 'aaaabbbbccccc'
    str2 = 'ccccbbbaaaa'
    lvs.fit(str1, str2)
    print(lvs.get_normalized_distance())
    print(td.ZLIBNCD().normalized_distance(str1, str2))

    # print(lvs.get_normalized_similarity('max'))

    '''
    print(list(groupby('aaaabbbbaaaaa')))

    for i, j in groupby('aaaabbbbaaaaa'):
        print(i, list(j))
    print(1*'a')
    '''

    from levenshtein import Levenshtein

    string_list1 = ["helloworld", "helloworld2", "hellosworld", "hello34world", "hellowo7rld", "hellowoxrld",
                    "hellow1rld",
                    "2helloworld",
                    "goodbye", "goodezbye", "goodby3e", "good5fbye", "goodby4e", "goodbyrge", "gooderbye", "4goodbye"]
    string_list2 = ["hellowor3ld", "hello1world5", "hel3loworldv", "he1llowo3rld", "goodby5e", "goodvye", "g5sdbye",
                    "goo45dbye"]
    lvs = Levenshtein()
    lvs.fit(string_list1, string_list2)
    print(lvs.get_normalized_distance('all'))