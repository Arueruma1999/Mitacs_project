

def stringCheck(string):
    return isinstance(string, str)

def find_most_label(label_list):
    return max(set(label_list), key=label_list.count)

def get_n_grams(string, n):
    return list(zip(*[string[i:] for i in range(n)]))

def tuple_to_string(tuple_data):
    return "".join(tuple_data)