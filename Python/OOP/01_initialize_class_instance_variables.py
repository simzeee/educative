class Employee:

    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


Bob = Employee(3789, 2500, "Human Resources")

print(Bob.id)


class Player:
    teamName = "Liverpool"  # class variables
    teamMembers = []

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = []
        self.teamMembers.append(self.name)


p1 = Player("Mark")
p2 = Player("Steve")
p3 = Player("John")
print("Name:", p1.name)
print("Team Members:")
print(p1.teamMembers)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.teamMembers)
