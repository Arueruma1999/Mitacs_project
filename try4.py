import numpy as np
from collections import Counter
if __name__ == "__main__":
    def find_ngrams(input_list, n):
        return list(zip(*[input_list[i:] for i in range(n)]))

    def display(*data):
        return data

    '''
    a = ("helloworld", "helloworld")
    print(isinstance(a, str))
    print(all((True, True, False)))
    print(len(display(["hello","world","Hi"])[0]))
    print(len("hello"[0]))
    print(["hello"])

    b = np.array([[1,2,3]])
    c = np.array([[2,1,4]]).T
    print(c)
    print(np.maximum(b, c))

    print(np.array(list((map(len, a)))).reshape(-1,1))

    data1 = np.array(list((map(lambda x: x[np.argpartition(x, 2)[:2]], np.array([[1,2,3], [4,5,6], [7,8,9]])))))
    print(data1)
    '''
    data = np.array([[1,2,1,1], [2,2,2,3]]).tolist()[0]
    print(data)
    print(max(set(data), key=data.count))


