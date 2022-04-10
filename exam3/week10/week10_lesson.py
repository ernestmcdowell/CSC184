# Classes and Objects
#
#
# Date: 06APR2022
# Author: Ernest McDowell
#
#

class Dog:
    breed = ""
    age = 0
    color = "black"
    owner = ""

rover = Dog
rover.owner = "beau"
print(rover.breed, rover.age, rover.color, rover.owner)

class Employee:
    employee_index = 0
    name = ""
    phone = "8167243304"
    salary = 0

    def telephone(self):
        return "Phone number is: "+str(self.phone)

bob = Employee()
print(bob.name,bob.salary,bob.employee_index,bob.phone)


class Employee2:
    employee_index = 0
    def __init__(self,name="Blank",phone=0,salary=0):
        self.name = name
        self.phone = phone
        self.salary = salary 
        Employee2.employee_index +=1
        self.employee_indx = Employee2.employee_index


    def telephone(self):
        return "Phone number is: "+str(self.phone)
beau = Employee2("Beau McDowell","816-724-3304",59000)
print(beau.name,beau.salary,beau.phone)
john = Employee2("Belh","Bleh",23000)
print(john)
