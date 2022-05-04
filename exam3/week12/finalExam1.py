# Final Exam for CSC184-40
#
# Author: Beau McDowell
# Date: 25APR2022
#
# Create a basic human resource program that can have the following functionality:
# It can search for any employee and print their address, phone number, employee number, department, title, salary and immediate supervisor
# It must pull the data from the following two data sets, you are not allowed to "save" a new data set since both sets are from independent parts of the company. There is sensitive filermation in each data set hence why the separation. 

import csv
salary_file = open('Employee_salary_info.csv', 'r')
salary_read = csv.reader(salary_file, delimiter=',')
employee_file = open('Employees_personal_info.csv', 'r')
employee_read = csv.reader(employee_file, delimiter=',')


class SalaryInfo:
    def __init__(self):
        self.employee_rank = salary_file[3]
        self.employee_sup = salary_file[4]
        self.employee_salary = salary_file[5]
        self.employee_title = salary_file[6]


class PersonalInfo:
    def __init__(self):
        self.employee_number = employee_file[0]
        self.last_name = employee_file[1]
        self.first_name = employee_file[2]
        self.phone_num = employee_file[3]
        self.address = employee_file[4:5]


def searcher():
    count = 0
    is_searching = True
    print("Search for employee information.")
    search = str(input("Enter first and last name of employee: ")).capitalize()
    print("Search Result...")
    print()
    while is_searching:
        for row in employee_read:
            if search == row[1]:
                count += 1
                print(count)
                if count == 2:
                    first_name = input("Please enter employee first name to narrow search : ")
                    if first_name == row[2]:
                        print("Employee Number: " + row[0])
                        print("Full Name: " + row[1], row[2])
                        print("Phone Number: " + row[3])
                        print("Address: " + row[4], row[5])
                elif count == 1:
                    if search == row[1]:
                        print("Employee Number: " + row[0])
                        print("Full Name: " + row[1], row[2])
                        print("Phone Number: " + row[3])
                        print("Address: " + row[4], row[5])

        for row in salary_read:
            if search == row[1]:
                print("Immediate Supervisor: " + row[4])
                print("Salary: $" + row[5])
                print("Title: " + row[6])
                print()

        continue_search = input("Do you want to search for another employee? y/n ").capitalize()
        if continue_search == "Y":
            is_searching = True
            employee_file.seek(0)
            salary_file.seek(0)
            searcher()
        else:
            is_searching = False


searcher()


