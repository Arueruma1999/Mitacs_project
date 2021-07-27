from levenshtein import Levenshtein
from jaro import Jaro
from jaro_winkler import JaroWinkler
from needleman_wunsch import NeedlemanWunsch
from smith_waterman import SmithWaterman
from hamming import Hamming
from damerau_levenshtein import DamerauLevenshtein
from maximal_consecutive_longest_common_sequence import MCLCS
from mutual_information import MI
from dice_coefficient import DC
from cosine_coefficient import CC
from jaccard_coefficient import JC
from overlap_coefficient import OC
from bag import Bag
from mongue_elkan import ME
from weighted_mongue_elkan import WME
from ratcliff_obershelp import RO
from cooccurrence_over_distance import COD
import numpy as np
from k_nearest_neighbors import StringKNN
import textdistance as td
from k_nearest_neighbors import StringKNN

if __name__ == "__main__":

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