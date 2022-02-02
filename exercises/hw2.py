# Title: Setup a function to calculate compound interest
#
# Description: Homework 2.1
#
# Author: Ernest B McDowell
# Date: 26JAN2022
#
# define starting price, ending price and the length of investment for AAPL NTDOY SPY and TSLA stocks
#AAPL
aapl_start = 34.25 
aapl_end = 159.22 
aapl_length = 5 
#NTDOY
ntdoy_start = 26.11
ntdoy_end = 61.19
ntdoy_length = 5
#SPY
spy_start = 236.47
spy_end = 431.24
spy_length = 5
#TSLA
tsla_start = 50.00
tsla_end = 821.10
tsla_length = 5
#User input stock
new_start = float(input('Stock starting price: ')) # get starting price of user input stock
new_end = float(input('Stock ending price: ')) # get ending price of user input stock
new_length = float(input('Enter length of investment: ')) # get user input length of investment

principal = 100 # the prinicpal investment in dollars
compounds = 12 # the compound frequency in months 

def calc_apr(start, end, time):
    rate = compounds*((end/start)**(1/(compounds*time))-1) # compound interest formula
    rate = round(rate*100,2) # multiplies the rate by 100 for correct decimal placement and rounds 2 places after decimal
    return rate

def calc_annuity(principal, rate, time, compounds):
    amount = principal*((1+(rate/100)/compounds)**(compounds*time)-1)/(rate/compounds)
    amount = round(amount*100,2) # multiplies the ammount by 100 for correct decimal placement and rounds 2 places after decimal
    return amount

def stocks_final():
    user_apr = (calc_apr(new_start, new_end, new_length))
    user_annuity = calc_annuity(principal, user_apr, new_length, compounds)
    print('The APR for your stock was: '+str(user_apr)+'%')
    print('if you had invested $100 a month in the stock over 5 years you would have: $'+str(user_annuity))
    
    aapl_apr = calc_apr(aapl_start, aapl_end, aapl_length)
    aapl_annuity = calc_annuity(principal, aapl_apr, aapl_length, compounds)
    print('The APR for AAPL was: '+str(aapl_apr)+'%')
    print('if you had invested $100 a month in AAPL over 5 years you would: $'+str(aapl_annuity))
    
    ntdoy_apr = calc_apr(ntdoy_start, ntdoy_end, ntdoy_length)
    ntdoy_annuity = calc_annuity(principal, ntdoy_apr, ntdoy_length, compounds)
    print('The APR for NTDOY was: '+str(ntdoy_apr)+'%')
    print('if you had invested $100 a month in NTDOY over 5 years you would have: $'+str(ntdoy_annuity))
    
    spy_apr = calc_apr(spy_start, spy_end, spy_length)
    spy_annuity = calc_annuity(principal, spy_apr, spy_length, compounds)
    print('The APR for SPY was: '+str(spy_apr)+'%')
    print('if you had invested $100 a month in SPY over 5 years you would have: $'+str(spy_annuity))
    
    tsla_apr = calc_apr(tsla_start, tsla_end, tsla_length)
    tsla_annuity = calc_annuity(principal, tsla_apr, tsla_length, compounds)
    print('The APR for TSLA was: '+str(tsla_apr)+'%')
    print('if you had invested $100 a month in TSLA over 5 years you would have: $'+str(tsla_annuity))
    
stocks_final()