# Title: Homework2_1 for CSC-184-40
#
# Description: Take user input of stocks and calculate APR over a 5 year period
#
# Author: Ernest B McDowell
# Date: 26JAN2022
#
# Annuity formula is annuity = contribution*(1+rate/compound_frequency)**(compound_frequency*length_of_investment)-1)/(rate/compound_frequency)
#

def calc_stock_apr():
    print('Stock APR Calculator') #Title to show what is being calculated 
    start_price = float(input('Enter stock starting price: ')) #starting price of the stock 
    end_price = float(input('Enter the stock ending price: ')) #ending price of the stock 
    length_of_investment = 9 # length of the investment in years
    compound_frequency = int(input('Enter the frequency at which interest will compound: ')) # frequency at which interest will compound ie. monthly(12), weekly(52) etc..
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*length_of_investment))-1) # compound interest formula
    return float(round(rate*100,2)) # multiplies the result of rate by 100 to get percentage and rounds to 2 decimal places

def calc_annuity():
    print('Annuity Calculator') #Title to show what is being calculated
    rate = float(input('Enter the APR: ')) # enter the APR given from the previous calculation
    length_of_investment = 5 # investment length in years
    compound_frequency = 12 # frequency interest will be compounded
    contribution = 100
    annuity = contribution*((1+(rate/100)/compound_frequency)**(compound_frequency*length_of_investment)-1)/(rate/compound_frequency) # annuity formula 
    return round(annuity*100,2) # rounds the result from annuity to 2 decimal places

def test_annuity(rate, frequency, payment):
    annuity = payment*((1+rate)**(frequency)-1/rate)
    return annuity*100


stock_apr = calc_stock_apr() # assign function to new variable
print('The APR for the stock is: ' + str(stock_apr)+'%'' over 5 years')

annuity_calc = calc_annuity() # assing function to new variable 
print('If you had invested $100 per month you would have earned: $'+str(annuity_calc))



