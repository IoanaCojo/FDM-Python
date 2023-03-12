"""Write a Python function that finds the maximum of all the numbers in a given list using lambda."""

from functools import reduce

list_no = [4, 3, 2, 2, -1, 18]
max_no = reduce(lambda x, y: max(x,y), list_no)
print(max_no)

"""Write a Python function that finds the minimum of all the numbers in a given list using lambda."""

min_no = reduce(lambda x,y: min(x,y), list_no)
print(min_no)

average_no = reduce(lambda x,y: x+y, list_no)
print( average_no/len(list_no))