# Title: Setup a function to calculate compound interest
#
# Description: Using functions 
#
# Author: Ernest B McDowell
# Date: 26JAN2022
#
#

def new_func(num):
    print('Do stuff')
    print(num)
    return num+num


def compound_interest(principal, rate, length_of_investment, compound_frequency):
    # A = P*(1+r/n)**(n*t)
    amount = principal*(1+(rate/100)/compound_frequency)**(compound_frequency*length_of_investment) 
    amount = round(amount,2)
    return amount


def calc_stock_apr(start_price, end_price, length_of_investment):
    compound_frequency = 12
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*length_of_investment))-1)
    return rate

print(calc_stock_apr(33.4,104.65,9))
print(compound_interest(100,7,8.5,12))