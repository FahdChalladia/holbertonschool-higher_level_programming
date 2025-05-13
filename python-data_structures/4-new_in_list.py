#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    test = my_list.copy()
    if idx < 0 or idx >= len(test):
        return test
    else:
        test[idx] = element
        return test
