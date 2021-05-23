from sklearn.metrics import confusion_matrix
import numpy as np

X = np.array([[0,0,1,1, 0], [0,1,0,1, 0]])
np.double(print(confusion_matrix(X[0], X[1])))