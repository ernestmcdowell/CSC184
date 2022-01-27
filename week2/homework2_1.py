# Title: Homework2_1 for CSC184
#
# Description: Take user input of stocks and calculate APR over a 5 year period
#
# Author: Ernest B McDowell
# Date: 26JAN2022
#
# Annuity formula is annuity = contribution*(1+rate/compound_frequency)**(compound_frequency*length_of_investment)-1)/(rate/compound_frequency)
#



def calc_annuity():
    rate = float(input('Enter the APR: '))
    compound_frequency = float(input('Enter the frequency interest will compound: '))
    length_of_investment = 5
    contribution = float(input('Enter the dollar amount of your contribution: '))
    annuity = contribution*((1+rate/100/compound_frequency)**(compound_frequency*length_of_investment)-1)/(rate/compound_frequency) # annuity formula 
    print(round(annuity,2) + contribution)




def calc_stock_apr():
    start_price = float(input('Enter stock starting price: '))
    end_price = float(input('Enter the stock ending price: '))
    length_of_investment = 5
    compound_frequency = float(input('Enter the frequency interest will compound: '))
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*length_of_investment))-1)
    return float(round(rate,2))


print(calc_annuity())
print(calc_stock_apr())




