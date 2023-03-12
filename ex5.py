"""
Create a function salaries_with_bonus that returns the list of salaries with the bonus for a list of employees' salaries passed to it as parameter using:

a) lambda function passed as an argument to an ordinary higher order function featuring

i. list function
ii. list comprehension
iii. generator comprehension

b) lambda function passed as argument to a lambda higher order function featuring

i. list function
ii. list comprehension
iii. generator comprehension

c) lambda function returned from an ordinary higher order function featuring

i. list function
ii. list comprehension
iii. generator comprehension

d) lambda function returned from a lambda higher order function featuring

i. list function
ii. list comprehension
iii. generator comprehension

Assume bonus is 5%. Example: for the list of salaries [29000, 48000, 31213, 15875, 17450, 50245, 75801] the function should return the list [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]

"""
salaries = [30450.0, 50400.0, 32773.65, 16668.75, 18322.5, 52757.25, 79591.05]

def ordinary_higher_order_func(salary, func):
    return func(salary)

def salaries_with_bonus(bonus, salaries):
    return list(ordinary_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries)

salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801])


def salaries_with_bonus(bonus, salaries):
    return [ordinary_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries]

salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801])


def salaries_with_bonus(bonus, salaries):
    return list((ordinary_higher_order_func(salary, lambda salary : salary + salary * bonus) for salary in salaries))

salaries_with_bonus(0.05,  [29000, 48000, 31213, 15875, 17450, 50245, 75801])