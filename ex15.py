"""
Write a Python program to find palindromes in a given list of strings using lambda function. Example: Original list of strings: ['!', 'php', 'w3r', 'Python', 'ada', 'Java', 'abcd', 'aaa', 'aoxomoxoa', 'BaroccoraB'] List of palindromes: ['!', 'php', 'ada', 'aaa', 'aoxomoxoa', 'BaroccoraB']
"""
strings= ['!', 'php', 'w3r', 'Python', 'ada', 'Java', 'abcd', 'aaa', 'aoxomoxoa', 'BaroccoraB']
palindro = list(filter(lambda str: str == ''.join(reversed(str)), strings))
print(palindro)




