"""
In Python, we can impose access restrictions on different data members and member functions. 
The restrictions are specified through access modifiers. 
Access modifiers are tags we can associate with each member to define which parts of the program can access it directly.

There are two types of access modifiers in Python. Let’s take a look at them one by one.
"""

# Public attributes are those that can be accessed inside the class and outside the class.


class Employee:
    def __init__(self, ID, salary):
        # all properties are public
        self.ID = ID
        self.salary = salary

    def displayID(self):
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
print(Steve.salary)

# Private attributes cannot be accessed directly from outside the class but can be accessed from inside the class.


class Employee2:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee2(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error


class Employee3:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee3(3789, 2500)
print(Steve._Employee__salary)  # accessing a private property
