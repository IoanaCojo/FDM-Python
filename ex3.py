"""
3. Write the function filter_valid_salaries that removes any non-positive salary from the list of salaries (leaving only positive salaries) using:

a) the filter() built-in function

b) list comprehension

c) generator comprehension

[29000, 48000, 31213, -15875, 17450, 50245, 75801, -564, 0 , -34]

"""

def filter_valid_salaries(salaries):
    return (list(filter(lambda sal: sal>0,salaries)))
print (filter_valid_salaries([138, -3,8,-46,98,-4, 0,224]))


salaries = [29000, 48000, 31213, -15875, 17450, 50245, 75801, -564, 0 , -34]
comprehension_list = [sal for sal in salaries if sal >0]
print(comprehension_list)
