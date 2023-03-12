"""
Write a Python function to find the list with maximum length in a list of lists using lambda function. The function should return a tuple consisting of two elements:
1) the max length
2) the list having the max length Example: Original list: [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]] Returned value: (3, [13, 15, 17])
"""


def max_len_list(ll):
    max_len = max(len(x) for x in ll)
    max_list = max(ll, key=lambda x: len(x) == max_len)
    return (max_len, max_list)


ll = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print(max_len_list(ll))

"""
Write a Python function to find the list with minimum length in a list of lists using lambda function. The function should return a tuple consisting of two elements: 1) the min length 2) the list having the min length Example: Original list: [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]] List with minimum length of lists: (1, [0])
"""

def min_len_list(ll):
    min_len = min(len(x) for x in ll)
    min_list = min(ll,key = lambda  x :len(x) == min_len)
    return (min_len, min_list)

print(min_len_list(ll))