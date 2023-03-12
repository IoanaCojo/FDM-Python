"""
Write a Python program that multiplies each number of a given list with a given number using lambda function. Print the result as a string of numbers. Example: Original list: [2, 4, 6, 9, 11] Given number: 2 Result: 4 8 12 18 22
"""
initial_list = [2, 4, 6, 9, 11]
double_list = list(map(lambda el: el*2, initial_list))

print(double_list)


