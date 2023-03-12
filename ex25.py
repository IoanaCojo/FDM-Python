"""
Write a Python program to count the occurrences of the items in a given list using lambda. Tip: return the dictionary where the keys are the different (unique) items and the values are their corresponding frequency. Use the count() list method to count the occurrences of different list items. Example: Original list: [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2] Count the occurrences of the items in the said list:
"""

def unique(lst):
    dict={}
    for i in lst:
        if i not in dict.keys():
            dict[i] = lst.count(i)
    #return dict

    dict2 = {el: lst.count(el) for el in lst}
    return dict2

print(unique([3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]))