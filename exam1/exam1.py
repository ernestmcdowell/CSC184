# Program that will allow user to convert between celsius and fahrenheit and kilometers and miles vice versa.
#
# Exam 1 for CSC184-40
#
# Author: Beau McDowell
# Date: 18FEB2022
#

kilo_conversion = 1.609344  # number of kilometer in a mile found on google
mile_conversion = 1/kilo_conversion  # number of miles in a kilometer


def fahrenheit():  # take user input of a temperature in celsius and converts it to fahrenheit
    celsius_temp = float(input("Please enter a temperature in celsius: "))
    fahrenheit = (celsius_temp*1.8)+32 # fahrenheit conversion formula
    print(str(celsius_temp)+" celsius is " +
          str(round(fahrenheit, 2))+" fahrenheit")


def celsius():  # takes user input of a temperature in fahrenheit and converts it to celsius
    fahrenheit_temp = float(
        input("Please enter the temperature in Fahrenheit to convert: "))
    celsius = ((fahrenheit_temp-32)/1.8) #celsius conversion formula
    print(str(fahrenheit_temp)+" fahrenheit is " +
          str(round(celsius, 2))+" celsius")


def kilometers():  # take user input of a number of miles and converts it to kilometers
    num_miles = float(
        input("Please enter the number of miles to convert to kilometers: "))
    kilometers = num_miles * kilo_conversion # kilometer conversion formula
    print("The conversion of "+str(num_miles)+" mile(s) is " +
          str(round(kilometers, 2))+" kilometer(s)")


def miles():  # take user input of a number of kilometers and converts it to miles
    num_kilometers = float(
        input("Please enter the number of kilometers to convert to miles: "))
    miles = num_kilometers/kilo_conversion # mile conversion formula
    print("The conversion of "+str(num_kilometers) +
          " kilometer(s) is "+str(round(miles, 2))+" mile(s)")


def user_selection():  # allow user to select between performing Temperature conversion or Distance conversion
    print("1:) Temperature")
    print("2:) Distance")
    user_inp = input(
        "Please select the conversion you would like to perform: ")
    if user_inp == "1":  # if user is equal to 1 then prompt user for temp conversion selection
        print("1:) To Fahrenheit")
        print("2:) To Celsius")
        temp_selection = input("Please select what you want to convert to: ")
        if temp_selection == "1":
            fahrenheit()  # if user input is equal to 1 then call the fahrenheit function
        elif temp_selection == "2":
            celsius()  # if user input is equal to 2 then call the celsius function
        else:
            print("You must select a valid option!")
            return user_selection()  # if no valid option is selected rerun this function
    elif user_inp == "2":  # else if user input is equal 2 prompt user for distance conversion selection
        print("1:) To Kilometers")
        print("2:) To Miles")
        distance_selection = input(
            "Please select what you want to convert to: ")
        if distance_selection == "1":
            kilometers()  # if user input is equal to 1 then call the kilometers function
        elif distance_selection == "2":
            miles()  # if user input is equal to 2 then call the miles function
        else:
            print("You must select a valid option!")
            return user_selection()  # if no valid option is selected rerun this function
    else:
        print("You must select a valid option!")
        return user_selection()  # if no valid option is selected rerun this function

user_selection()
