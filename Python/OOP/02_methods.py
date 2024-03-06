class Employee:

    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def tax(self):
        return self.salary * 0.2

    def salaryPerDay(self):
        return self.salary / 30


# initializing an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())

# Class Methods


class MyClass:
    classVariable = "educative"

    @classmethod
    def demo(cls):
        return cls.classVariable


class Player:

    teamName = "Liverpool"

    def __init__(self, name):
        self.name = name

    @classmethod
    def getTeamName(cls):
        return cls.teamName


print(Player.getTeamName())

# Static Methods


class Player:
    teamName = "Liverpool"  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables

    @staticmethod
    def demo():
        print("I am a static method.")


p1 = Player("lol")
p1.demo()
Player.demo()

"""
Static methods do not know anything about the state of the class, i.e., they cannot modify class attributes. 
The purpose of a static method is to use its parameters and produce a useful result.

Suppose that there is a class, BodyInfo, containing information about the physical attributes of a person.
We can make a static method for calculating the BMI of any given weight and height:
"""


class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)


weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))
