"""
a) Write an empty Python class named Trainee and display its type and namespace. Additionally, display only the keys of the Trainee's namespace.

b) Create an object of class Trainee, and display its type, namespace and its class name.

c) Write an empty Python class named Trainer and create an object of this class. Check whether this object and the object of class Trainee created in question 1b are instances of the said classes or not. Also, check whether the classes Trainee and Trainer are subclasses of the built-in object class or not.

d) Add two class attributes: academy and trainee_name to the class Trainee. Modify the attribute values of the class Trainee and print the original and modified values of the attributes.

e) Add a class method to print the values of the two class attributes: academy and trainee_name. Use this method to print the values of the two class attributes. Check that the two attributes and their values are included to the Trainee's class namespace.

f) Add an instance method to print the values of the two class attributes: academy and trainee_name from an object. Create an object of class Trainee and use the method to print the values of the two class attributes. Using the object's namespace check that the object has no instance attributes. Access each class attribute from the object to print its value.

g) Add another instance method to the Trainee class to print the values of its instance attributes (from an object, as instance attributes are not accessible from the class).

Create another object of class Trainee.

Print its class attributes:

- using the class method created in question 1e

- using the instance method created in question 1f

- using the class namespace

- directly from the object.

Assign new values to the attributes academy and trainee_name

directly from the object.

Print class attributes and their values

- using the class method created in question 1e

- using the instance method created in question 1f

- using the class namespace.

Then print the values of the object's instance attributes

- using the instance method created in this question

- using the object's namespace

- directly from the object.

Explain what has happened.

Tip: use the __dict__ attribute to display the namespaces.
"""

class Trainee():
    academy='FDM'
    trainee_name ='unknown'

    @classmethod
    def get_class_attributes(cls):
        print(f'Trainee {cls.trainee_name} is in the {cls.academy}')

    def print_class_attr_from_instance_method(self):
        print(f'Trainee {self.__class__.trainee_name} is in the {self.__class__.academy}')

    def print_instance_attr(self):
        print(f'Trainee {self.trainee_name} is in the {self.academy}')


class Trainer():
    pass

# a) Write an empty Python class named Trainee and display its type and namespace. Additionally, display only the keys of the Trainee's namespace.

print(f'a) Trainee type: {type(Trainee)}')
print(f' Trainee namespace: {Trainee.__dict__}')
print(f'keys of the Trainees namespace : {Trainee.__dict__.keys()}')
print('\n')

# b) Create an object of class Trainee, and display its type,
#    namespace and its class name.

ioana = Trainee()
print(f'b) ioana type: {type(ioana)}')
print(f'ioana namespace: {ioana.__dict__}')
print(f'keys of the ioana namespace : {ioana.__dict__.keys()}')
print('\n')


# c) Write an empty Python class named Trainer and create an object
#    of this class. Check whether this object and the object of
#    class Trainee created in question 1b are instances of the said
#    classes or not. Also, check whether the classes Trainee and
#    Trainer are subclasses of the built-in object class or not.

trainer = Trainer()
print(f'c) is ioana instance of Trainee? {isinstance(ioana, Trainee)}')
print(f'is trainer instance of Trainer? {isinstance(trainer, Trainer)}')
print('\n')

# d) Add two class attributes: academy and trainee_name to the class
#    Trainee. Modify the attribute values of the class Trainee
#    and print the original and modified values of the attributes.

print(f'd) initial class attribute: {ioana.trainee_name}')
ioana.trainee_name = 'Ioana'
print(f'new class attribute: {ioana.trainee_name}')
print('\n')

print(f'Initial academy value : {ioana.academy}')
ioana.academy = 'Developer Path'
print(f'New academy value : {ioana.academy}')
print('\n')

# e) Add a class method to print the values of the two class
#    attributes: academy and trainee_name. Use this method to
#    print the values of the two class attributes.
#    Check that the two attributes and their values are included
#    to the Trainee's class namespace.

Trainee.get_class_attributes()
print(f'e) Trainee namespace: {Trainee.__dict__}')
print('\n')

# f) Add an instance method to print the values of the two class
#    attributes: academy and trainee_name from an object. Create
#    an object of class Trainee and use the method to print the
#    values of the two class attributes.
#    Using the object's namespace check that the object has no
#    instance attributes.
ioana.print_class_attr_from_instance_method()
print(f'f) ioana namespace: {ioana.__dict__}')
print('\n')

# g) Add another instance method to the Trainee class to print the
#    values of its instance attributes (from an object, as instance
#    attributes are not accessible from the class).
#    Create another object of class Trainee.
#    Print its class attributes:
#    - using the class method created in question 1e
#    - using the instance method created in question 1f
#    - using the class namespace
#    - directly from the object.

another_trainee = Trainee()
another_trainee.trainee_name = 'Dan-Dan'
another_trainee.academy = ' nO nEED aCADEMY'
print(f'g) Class Attributes using the class method : {another_trainee.get_class_attributes()}')
print(f'Class attributes using instance method : {another_trainee.print_class_attr_from_instance_method()}')
print(f'Class attributes  : {another_trainee.print_instance_attr()}')
print(f'Class attributes using teh __dir__: {ioana.__dir__()}')
print('\n')