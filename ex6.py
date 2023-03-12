"""
6. The input list contains integer values that should represent employee's salaries; however some of its values may be erroneous: some values may be 0, while others may be negative. Assuming that bonus is 5%, write a function valid_salaries_with_bonus that returns the list of salaries with the bonus for a list of employees' salaries passed to it as parameter, while ignoring any erroneous values using:

a. map() and filter() built-in functions

b. list comprehension

c. generator comprehension

Example: for the list of salaries: [29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000] the function should return the list [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05], as negative numbers and 0 should be ignored.
"""

def valid_salaries_with_bonus(salaries):
    return (list(map(lambda sal: sal + sal * 0.05, filter(lambda salary: salary >0, salaries))))

print(f'map, filter salaries: {valid_salaries_with_bonus([29000, 48000, 0, 31213, 15875, -21500, 17450, 50245, 75801, -100000])}')