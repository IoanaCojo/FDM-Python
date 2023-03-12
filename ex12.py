"""
Write a Python program to find the elements of a given list of strings that contain specific substring using lambda function. Example: for the following two inputs: list_strings = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] substring = 'emb' the program should return the list ['September', 'November', 'December'] Tip: pass the lambda function as argument to the filter() function
"""

list_strings = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
substring = 'emb'

filtered_list = list(filter(lambda str: substring in str ,list_strings))
print(filtered_list)