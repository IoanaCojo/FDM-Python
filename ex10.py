"""
Change the lambda function from previous question to find if a given string starts with a given character passed to it as a parameter.
"""

starts_with = lambda str, char: True if str.startswith(char)else False
print(starts_with('prune', 'l'))