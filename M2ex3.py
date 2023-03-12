"""
Create the two classes as depicted by the UML diagram below
a. Create a constructor for each class. Ensure that it only initialises the
attributes shown in the UML.
b. Except for the constructor, all methods that don’t return or change
values should simply print out a message containing the name of the
method and the value of its argument(s).
For example, the read_data method returns a String. The String should
contain a simple message like: “read_data: reading data from “ + file.
c. Ensure that attributes shown in upper case are read-only instance
attributes.
d. Use the Python property decorators to get, set and delete all attributes

Client code to test the HardDrive class:
• create a HardDrive object
• display the namespace of both the class and the object
• display the model and capacity directly from the object (ensure the
getter gets invoked in both cases)
• set the value of model for the object to ‘WD’ and the value of capacity
to 3072GB (ensure the setter gets invoked in both cases displaying the
appropriate message)
• display the values of model and capacity directly from the object
(ensure the getter gets invoked in both cases and that the values of
both attributes have not been changed)
• use the set_used_space method to change the used space to 0GB and
check that it was changed by displaying the used_space attribute
directly from the object
• execute the read_data() and write_data() instance methods to check
that the appropriate messages are displayed
• set the docstring for the model to 'name of the hard disk model' and
for the capacity to 'hard disk capacity', and then display them both
• delete the model, capacity and used space attributes and check their
removal by displaying the object’s namespace after each attribute is
deleted

Client code to test the Memory class:
• create a Memory object
• display the namespace of both the class and the object
• display the model, capacity and speed directly from the object (ensure
the getter gets invoked in both cases)
• set the value of model for the object to ‘Corsair’ and the value of
capacity and speed to 8GB and 1333Hz respectively (ensure the setter
gets invoked in both cases displaying the appropriate message)
• display the values of model, capacity and speed directly from the
object (ensure the getter gets invoked in both cases and that the
values of none of the attributes have been changed)
• use the set_used_space method to change the used space to 0.5GB and
check that it was changed by displaying the used_space attribute
directly from the object
• execute the store_data()instance method to check that the appropriate
message is displayed
• set the docstring for the model to 'name of the hard disk model', for
the capacity to 'hard disk capacity' and for the speed to “memory
speed”, and then display them all
• delete the model, capacity, speed and used space attributes and check
their removal by displaying the object’s namespace after each
attribute is deleted
"""


class HardDrive():
    def __init__(self, model, capacity):
        self.model = model
        self.capacity = capacity

    @property
    def model(self):
        print('Getting model : ')
        return self._model

    @model.setter
    def model(self, value):
        print('Setting Model to ', value)
        self._model = value

    @model.deleter
    def model(self):
        print('Deleting capacity :', self._model)
        del self._model

    @property
    def capacity(self):
        print('getting capacity: ')
        return self._capacity

    @capacity.setter
    def capacity(self,value):
        print(f'Set capacity to {value}')
        self._capacity = value

    @capacity.deleter
    def capacity(self):
        print('Deleting capacity:', self._capacity)
        del self._capacity


    def set_used_space(self, used_space):
        self.used_space = used_space


    def read_data(self, file):
        print('read_data: reading data from', file)

    def write_data(self, file):
        print('write_data: writing data to', file)


class Memory():
    def __init__(self,model, capacity, speed):
        self.model = model
        self.capacity = capacity
        self.speed = speed

    @property
    def capacity(self):
        print('Getting capacity :')
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        print(f'Set capacity to {value}')
        self._capacity = value

    @capacity.deleter
    def capacity(self):
        print(f'Delete :{self._capacity}')
        del self._capacity

    @property
    def speed(self):
        print('Getting speed :')
        return self._speed

    @speed.setter
    def speed(self, value):
        print(f'Set speed to {value}')
        self._speed = value

    @speed.deleter
    def speed(self):
        print(f'Delete :{self._speed}')
        del self._speed

    @property
    def model(self):
        if hasattr(self, '_Memory_model'):
            print("Attempting to alter read-only attribute: model")
        else:
            print('Getting model :')
            return self._model

    @model.setter
    def model(self, value):
        print(f'Set model to {value}')
        self._model = value

    @model.deleter
    def model(self):
        print(f'delete {self._model}')
        del self._model

    def set_used_space(self, used_space):
        self.used_space = used_space



def hd_manipulation():
    hd = HardDrive("11-A", 8)
    print(HardDrive.__dir__)
    print(hd.__dir__)
    #print(hd.model)
    hd.model = 'WD'
    hd.capacity = 3072
    print(hd.model)
    print(hd.capacity)

    hd.set_used_space(0)
    print(f'Used space : {hd.used_space}')

    hd.read_data('readable_file.txt')
    hd.write_data('writable_file.txt')

    # set the docstring
    HardDrive.model.__doc__ = 'name of the hard disk model'
    HardDrive.capacity.__doc__ = 'hard disk capacity'
    # display the docstring
    print('Docstring:', HardDrive.model.__doc__)    # prints Docstring: name of the hard disk model
    print('Docstring:', HardDrive.capacity.__doc__) # prints Docstring: hard disk capacity
    print('\n')

    del hd.model
    print(hd.__dir__)
    del hd.capacity

    print(hd.__dir__)
# hd_manipulation()

def memory_manipulation():
    memory = Memory('Corsair',8, 1333)
    print(f'Namespace for memory instance: {memory.__dir__}')
    print(f'Namespace for Memory class: {Memory.__dir__}')

    print(memory.capacity)
    print(memory.model)
    print(memory.speed)



memory_manipulation()