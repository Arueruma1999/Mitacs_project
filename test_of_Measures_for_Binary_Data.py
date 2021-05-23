from Measures_for_Binary_Data import MBD
import numpy as np

if __name__ == "__main__":
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
