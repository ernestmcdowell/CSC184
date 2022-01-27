# Find APR for stocks over a period of time
#
# Description: 
#
# Author: Ernest McDowell
# Date: 26JAN2022
#
# Compound Formula is rate = compound_frequency*((amount/principal)**(1/(compound_frequency*time_of_investment))-1)

stock_start = float(input('Enter the starting price of the stock: '))
compound_frequency = float(input(' Please enter the frequency at which interest will be accrued: '))
length_of_investment = float(input('Please eneter the length of time that you owned the stock: '))
stock_end = float(input('Enter the stock ending price: '))
rate = compound_frequency*((stock_end/stock_start)**(1/(compound_frequency*length_of_investment))-1)
rate = round(rate*100,2)

print('The average APR over '+str(length_of_investment)+' years is : '+str(rate)+' %')