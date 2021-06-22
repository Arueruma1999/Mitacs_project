

def stringCheck(string):
    return isinstance(string, str)

def find_most_label(label_list):
    return max(set(label_list), key=label_list.count)