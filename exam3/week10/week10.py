# Homework 10.1 CSC-184-40
#
# Date: 09APR2022
# Author: Beau McDowell
#
class Students():
    student_indx = 0 # set student index to 0
    student_roster = [] # crate empty list for students
    def __init__(self,first_name="N/A",last_name="N/A",sex="N/A",major="N/A",graduation=0): # initialize the class with the following variables
        self.student_roster.append(self)
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.major = major
        self.graduation = graduation
        Students.student_indx +=1 #increment the student index by 1 for every student object
        self.student_indx = Students.student_indx # sets selft.student_indx to the current value of Students.student_indx

    def __str__(self) -> str:
        return f"{self.student_indx}: {self.first_name} {self.last_name} {self.sex} {self.major} {self.graduation} " #returns student objects containing all attributes in a string

# 3 pre defined student objects each containing the students special index #, first name, last name, sex, major, and graduation date.
print("CURRENT STUDENT ROSTER")
beau = Students("Beau","McDowell","M","Computer Science",2026)
print(str(beau.student_indx)+str(": "),beau.first_name,beau.last_name,beau.sex,beau.major,beau.graduation)
Bob = Students("Billy","Bob","M","Drama",1974)
print(str(Bob.student_indx)+str(": "),Bob.first_name,Bob.last_name,Bob.sex,Bob.major,Bob.graduation)
Tommy = Students("Tommy","Callahan","M","Business",1995)
print(str(Tommy.student_indx)+str(": "),Tommy.first_name,Tommy.last_name,Tommy.sex,Tommy.major,Tommy.graduation)


# Allow for adding new students to the roster
def new_student():
    enter_more = True
    wrong_inp = False
    user_inp = input("Would you like to add another student? y/n: ")
    if user_inp == "y":
        enter_more = True
        while enter_more == True:
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            sex = input("Sex: ")
            major = input("Major: ")
            graduation = input("Graduation Year: ")
            student = Students(first_name,last_name,sex,major,graduation)
            user_inp = input("Would you like to add another student? y/n: ")
            if user_inp == "y":
                enter_more = True
            else: 
                enter_more = False
    if enter_more == False:
        print("UPDATED STUDENT ROSTER")
        for students in Students.student_roster: # for any student object in the student roster
            print(students) # print student objects

new_student()
