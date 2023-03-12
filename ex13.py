"""
Write a Python program to find the values of length 5 in a given list using lambda function. Example: for the following list: months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] the program should return just two values: March April
"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

five_letters = list(filter(lambda str: str if len(str)==5 else '',months))
print(five_letters)

"""
Change the lambda function from previous question to find values of any given length in a given list.
"""
any_letters = list(filter(lambda str,no = 8 : len(str) == no, months))

print(any_letters)