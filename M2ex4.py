"""
Write a Python class which has two methods get_string() and print_string().
get_string() accepts a string from the user and print_string() prints the string in
'proper' case (the first character of each word of the string is upper case and
the rest of the characters are lower case).
Example:
'tHiS iS My UNTIDY string' -> This Is My Untidy String
"""

class Text():
    def __init__(self):
        self.string = ''

    def get_string(self):
        self.string = input('Please input your string here :')

    def print_string(self):
        words = self.string.split()
        proper_string = ''
        for word in words:
            proper_string += word.capitalize() + ' '

        print(proper_string)

text =Text()
text.get_string()
text.print_string()