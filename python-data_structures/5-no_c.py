#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    else:
        for i in range(len(my_string)):
            if my_string[i] == "c" or my_string[i] == "C":
                my_string = my_string[0:i] + my_string[i+1:]
                return no_c(my_string)
        return my_string
