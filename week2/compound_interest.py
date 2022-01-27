# Homework 2_1 for CSC184
# Author: Ernest B McDowell
# Date: 26JAN2022
#
# Description: Find the amount of money for compound interest investment
#
# Compound interest formula is Amount = Principal*(1+r/n)**(n*t)

principal = float(input('How much money are you planing to invest: '))
rate = float(input('Input the expected annual percentage rate(APR): '))
compound_frequency = float(input('Please enter the frequency at which interested will be accrued: '))
length_of_investment = float(input('Please eneter the length of time you plan to invest for in years: '))

# A = P*(1+r/n)**(n*t)
total = principal*(1+(rate/100)/compound_frequency)**(compound_frequency*length_of_investment)

total = round(total,2)

print('The total amount after ' + str(length_of_investment) + ' years is : $'+str(total))



