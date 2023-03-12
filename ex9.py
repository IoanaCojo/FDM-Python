"""
Write a lambda function named starts_with that finds if a given string starts with a character 'P' (returns True if it does; False if it doesn't). Tip: use the dir command to list all string methods and try to find one that could help with this task.
"""

starts_with = lambda str: True if str.startswith('P') or str.startswith('p') else False
print(starts_with('prune'))