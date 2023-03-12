"""
Write a Python function to multiply all the numbers in a given list using lambda. Example: Original list: [4, 3, 2, 2, -1, 18] Result: -864 as 4 * 3 * 2 * 2 * -1 * 18 = -864 Tip: import the functools module and find help on the function reduce()

"""
from functools import reduce

print(reduce(lambda x,y: x*y, [4, 3, 2, 2, -1, 18]))
