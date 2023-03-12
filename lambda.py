"""
Use the lambda function from Question 1 as a lambda function:

a) passed as an argument to an ordinary higher order function

b) passed as an argument to a lambda higher order function

c) returned from an ordinary custom-built higher order function

d) returned from a lambda custom-built higher order function

to calculate the salary with the bonus for a given employee's salary.

Create two solutions for questions a) and b): the first where the lambda function accepts two changeable parameters: salary & bonus, and the second where the lambda function accepts two parameters: salary & bonus, one of which (bonus) is fixed (keyword argument) - making it effectively a lambda function that accepts one changeable parameter.

In questions c) and d) pass only the bonus value as argument to the higher order function. Example: for the salary of 25000 and the bonus of 5%, tall solutions should return 26250.0

"""

salary_with_bonus_a = lambda salary, bonus: salary + (salary*bonus)/100
print(salary_with_bonus_a(25000,5))

salary_with_bonus_b = lambda salary, bonus = 0.05: salary + salary * bonus
print(salary_with_bonus_b(25000))

salary_with_bonus_c = lambda salary : salary +salary*0.05
print(salary_with_bonus_c(25000))

def o_h_f(sal,bon,func):
    return func(sal,bon)
print (f' ofhf : {o_h_f ( 25000,0.05, lambda sal,bon: sal + sal * bon) }')

lambda_hiugher_order_function = lambda sal,bon , func: sal +func(sal,bon)
print ( f' lambda_hiugher_order_function: {lambda_hiugher_order_function(25000,0.05, lambda sal,bon: sal*bon )}')

def my_func(sal):
    return lambda bon: sal+sal*bon
salary = my_func(25000)
print(f'return from a regular custome biilt high order func : {salary(0.05)}')

my_salary = lambda sal: lambda bon: sal+ sal*bon

final_sal=my_salary(25000)
print(f'as a return from lambda function {final_sal(0.05)}')
