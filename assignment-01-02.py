"""
2. Write a program to sort a given list by increasing order of the last element in each tuple.
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""

list_1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def get_last_element(tuple):
    return tuple[-1]

sorted_list = sorted(list_1, key=get_last_element)

print(sorted_list)

