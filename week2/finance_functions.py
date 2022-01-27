# Definitions for finance related functions
#
# Author: Ernest B McDowell
# Date: 26JAN2022
#

def compound_interest(principal, rate, length_of_investment, compound_frequency):
    # A = P*(1+r/n)**(n*t)
    amount = principal*(1+(rate/100)/compound_frequency)**(compound_frequency*length_of_investment) 
    amount = round(amount,2)
    return amount


def calc_stock_apr(start_price, end_price, length_of_investment):
    compound_frequency = float(input('Enter the frequency interest will compound: '))
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*length_of_investment))-1)
    return float(round(rate,2))

