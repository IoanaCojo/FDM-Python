"""
Write a Python program to sort a list of tuples using lambda function. Sort the courses by their achievement in descending order. Example: Original list of tuples: [('SQL', 88), ('Excel', 90), ('Python', 97), ('Unix', 82), ('Web Apps', 78), ('Java', 75)]

Sorted list of tuples: [('Python', 97), ('Excel', 90), ('SQL', 88), ('Unix', 82), ('Web Apps', 78), ('Java', 75)] Tip: pass the lambda function as the value to the key parameter of sorted() function or sort() method.
"""
marks = [('SQL', 88), ('Excel', 90), ('Python', 97), ('Unix', 82), ('Web Apps', 78), ('Java', 75)]
course_marks = sorted(marks, key = lambda x:x[1],reverse=True)
print(course_marks)