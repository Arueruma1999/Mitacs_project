from levenshtein import Levenshtein
from jaro import Jaro
from jaro_winkler import JaroWinkler
from needleman_wunsch import NeedlemanWunsch
from smith_waterman import SmithWaterman
from hamming import Hamming
from damerau_levenshtein import DamerauLevenshtein
import numpy as np
from k_nearest_neighbors import StringKNN
import textdistance as td

if __name__ == "__main__":

    X_train = ["helloworld", "helloworld2", "hellosworld", "hello34world", "hellowo7rld", "hellowoxrld", "hellow1rld", "2helloworld",
               "goodbye", "goodezbye", "goodby3e", "good5fbye", "goodby4e", "goodbyrge", "gooderbye","4goodbye"]
    X_test = ["hellowor3ld", "hello1world5", "hel3loworldv", "he1llowo3rld", "goodby5e", "goodvye", "g5sdbye", "goo45dbye"]
    y_train = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
    y_test = [0,0,0,0,1,1,1,1]
    lvs = DamerauLevenshtein()
    lvs.fit(X_train, X_test)
    answers2 = lvs.get_normalized_similarity()
    # print(td.levenshtein.normalized_distance(str1, str2))

    answers = np.empty((len(X_train), len(X_test)))
    for i, string1 in enumerate(X_train):
        for j, string2 in enumerate(X_test):
            answers[i][j] = td.damerau_levenshtein.normalized_similarity(string1, string2)
    print("-----------------------------------------")
    print(np.abs(answers-answers2)<0.0000001)
    print(answers2)
    print("-----------------------------------------")
    print(answers)









