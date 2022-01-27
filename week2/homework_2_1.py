# Homework 2_1 for CSC184
# Author: Ernest B McDowell
# Date: 26JAN2022
#
# Description: Find the amount of money for compound interest investment
#
# Compound interest formula is Amount = Principal*(1+r/n)**(n*t)

principal = float(input('How much money are you planing to invest: '))
rate = float(input('Input the expected annual percentage rate(APR): '))
compoundFrequency = float(input(' Please enter the frequency at which interested will be accrued: '))
lengthOfInvestment = float(input('Please eneter the length of time you plan to invest for in years: '))

# A = P*(1+r/n)**(n*t)
annuity = principal*(1+(rate/100)/compoundFrequency)**(compoundFrequency*lengthOfInvestment)

annuity = round(annuity,2)

print('The total amount after ' + str(lengthOfInvestment) + ' years is : $'+str(annuity))



