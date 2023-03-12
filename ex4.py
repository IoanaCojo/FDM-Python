"""
Create a function salaries_with_bonus that returns the list of salaries with the bonus for a list of employees' salaries passed to it as parameter using:

a) the map() built-in function

b) list comprehension

c) generator comprehension
"""

def salaries_with_bonus(salaries, bonus=0.05):
    return list(map(lambda sal: sal + sal*bonus, salaries))
print(salaries_with_bonus([29000, 48000, 31213, 15875, 17450, 50245, 75801]))

salaries = [29000, 48000, 31213, -15875, 17450, 50245, 75801, -564, 0 , -34]

comprehension_salary = [sal + sal * 0.05 for sal in salaries if sal>0 ]
print(comprehension_salary)