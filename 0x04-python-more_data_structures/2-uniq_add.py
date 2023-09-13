#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set(my_list)
    result = 0
    for num in unique_set:
        result += num
    return result

