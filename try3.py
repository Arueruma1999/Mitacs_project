from sklearn.neighbors import KNeighborsClassifier
import textdistance as td
import numpy as np

if __name__ == "__main__":
    X_train = np.array(["hello", "hella", "helle", "hello", "goodbye", "goadbye", "goodbye", "gaadbye"]).reshape(-1,1)
    X_test = np.array(["hello", "goodbye"])
    print(X_train.dtype)
    # X_train = X_train.astype(np.float64)
    # X_test = X_test.astype(np.float64)
    y_train = np.array([0,0,0,0,1,1,1,1])
    y_test = np.array([0,1])

    knn = KNeighborsClassifier(n_neighbors=3, metric=td.levenshtein.normalized_distance)
    print(knn.metric_params)
    knn.fit(X_train, y_train)
