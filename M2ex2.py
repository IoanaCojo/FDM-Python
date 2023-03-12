"""Rewrite the class Trainee so that it has 2 class attributes:
company - initialised as 'FDM Group', and count - initialised
to 0, to count the number of trainees.
Also add two instance attributes: academy and trainee_name.
Keep the three methods created in your solution for question 1
and add two more methods: the constructor to set up the values
for the two instance attributes when creating a new object and
to increase the trainee counter, as well as the destructor to
decrease the counter every time a trainee is removed.
Once the class has been created, write the client code to do
the following:
- print the values of class attributes as soon as the class has
  been created
- print the Trainee class namespace (using the __dict__ attribute)
- create three trainees and for each one print its class and
  instance attributes, and its namespace (using the __dict__ attribute)
- remove the first trainee
- print the values of Trainee class attributes using the class
  (not an object)"""

class Trainee():
    company = 'FDM GROUP'
    count = 0

    def __init__(self, academy, trainee_name):
        self.academy = academy
        self.trainee_name = trainee_name
        self.__class__.count += 1


    @classmethod
    def get_class_attributes(cls):
        print(f' In {cls.company} are {cls.count} trainees')

    def print_class_attr_from_instance_method(self):
        print(f' In {self.__class__.company} are {self.__class__.count} trainees')

    def print_instance_attr(self):
        print(f' In {self.company} are {self.count} trainees')

    def __del__(self):
        print(f'Delete {self.trainee_name} from {self.__class__.company}')
        self.__class__.count -= 1


trainee = Trainee('Software Dev', 'Ioana')
trainee.print_instance_attr()
print(f'Trainee__dict__ : {Trainee.__dict__}')

trainee2 = Trainee('DevOps', 'Clara')
trainee3 = Trainee('DevOps', 'Mihai')
trainee2.get_class_attributes()
trainee2.print_class_attr_from_instance_method()
trainee2.print_instance_attr()

del trainee3
trainee2.print_instance_attr()

