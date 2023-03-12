""" 1. Create a lambda function named salary_with_bonus that calculates employee’s salary with the bonus,

a) where both employee's salary and bonus are passed in as parameters

b) where both employee's salary and bonus are passed in as parameters but bonus is fixed as keyword argument (“kwarg”)

c) where only employee's salary is passed in as a parameter and bonus is fixed (hard-coded)

Assume bonus is 5%. Example: for the salary of 25000 the lambda function should return 26250.0
"""

salary_with_bonus_a = lambda salary, bonus: salary + (salary*bonus)/100
print(salary_with_bonus_a(25000,5))

salary_with_bonus_b = lambda salary, bonus = 0.05: salary + salary * bonus
print(salary_with_bonus_b(25000))

salary_with_bonus_c = lambda salary : salary +salary*0.05
print(salary_with_bonus_c(25000))

"""
a) Write an ordinary function to create the biggest number by rearranging the digits of a given number. Example: for the input 213 the function should return 321

b) Use method chaining to create a one-line version of the above function.

c) Create a lambda function from the one-line version of the above function
"""

def rearranging_no(no):
    lst = []
    while(no):
        lst.append(int(no%10))
        no = int(no/10)
    lst.sort(reverse=True)
    result = 0
    for i in lst:
        result = result * 10 + i
    return result

print(rearranging_no(231))

class rearrange():
    def no_separate(self, no):
        lst = []
        while (no):
            lst.append(int(no % 10))
            no = int(no / 10)
        lst.sort(reverse=True)
        return(lst)

    def return_no(self,lst):
        result = 0
        for i in lst:
            result = result * 10 + i
        return result

test = rearrange()
print(test.return_no(test.no_separate(231)))

def rearrange_nikola(no):
    lst=list(str(no))
    numbers_desc = sorted(lst, reverse=True)
    biggest_num =''.join(numbers_desc)
    return(biggest_num)

def rearrange_nikola2(no):
    print(int(''.join(sorted(list(str(no)),reverse = True))))

rearrange_nikola3 = lambda no: ''.join(sorted(list(str(no)),reverse = True))
print(f'rearrange nikola 3:  {rearrange_nikola3(4567)}')


"""
Write a lambda function named cap_string that capitalises the first letter of a string.
"""
cap_str = lambda str : str[:1].upper() +str[1:]
print(cap_str('asta e stringul meu '))

