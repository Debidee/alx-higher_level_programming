#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_newlist = my_list[:]
    if idx < 0:
        return my_newlist
    elif idx >= len(my_list):
        return my_newlist
    else:
        my_newlist[idx] = element
        return my_newlist
