"""
26. a) Write an ordinary function that accepts two parameters: a string and a boolean key variable upper_rest. If upper_rest=True is passed as 2nd argument, lambda function capitalises the first letter and capitalises the rest of the string. If upper_rest=False is passed as 2nd argument, lambda function capitalises the first letter and leaves the rest of the string as the original string. Tip: use the expression from the lambda function created in Question 25 as starting point to produce a one-line solution by including the if statement to it.

b) Write a lambda function that performs the task given in Question 26a.

When testing the ordinary function and the lambda function, call them with upper_rest=True, upper_rest=False and by omitting the parameter upper_rest altogether.

"""

lambda_version = lambda str,bol: str[:1].upper() + str[1:] if bol ==True else str[:1].lower() + str[1:].upper()

print(lambda_version('asta e stringul meu',False ))