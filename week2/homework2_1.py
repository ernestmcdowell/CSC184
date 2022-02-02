# Title: Homework2_1 for CSC-184-40
# Description: Take user input of stock prices and calculate APR over a period period of time and return potential annuity based on stock apr
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
stock_name = str(input('Enter the stock name: '))
new_start = float(input('Enter stock starting price: $')) # get starting price of user input stock
new_end = float(input('Enter stock ending price: $')) # get ending price of user input stock
new_length = float(input('Enter the length of investment in years: ')) # get user input length of investment
user_contrib = float(input('Enter your custom contribution ammount: $') + '\n') # get user input contribution dollar ammount

contribution = float(100) # the contribution amount in dollars for TSLA SPY NTDOY and AAPL
compound_frequency = 12 # the compound frequency in months 

def calc_apr(start, end, time): # calculate the apr based on start price, end price, and length of investment in years
    rate = compound_frequency*((end/start)**(1/(compound_frequency*time))-1) # compound interest formula
    rate = round(rate*100,2) # multiplies the rate by 100 for correct decimal placement and rounds 2 places after decimal
    return rate

def calc_annuity(contribution, rate, time, compound_frequency):
    amount = contribution*((1+(rate/100)/compound_frequency)**(compound_frequency*time)-1)/(rate/compound_frequency) # annuity formula
    amount = round(amount*100,2) # multiplies the ammount by 100 for correct decimal placement and rounds 2 places after decimal
    return amount

def stocks_final(): 
    """
    This function calls the calc_apr and calc_annuity function. Using user defined input and
    the defined variables it calculate the stocks APR and, using that APR, calculates the projected annuity ammount. 
    Finally it prints the results for each stocks APR and annuity amount.
    """
        
    user_apr = (calc_apr(new_start, new_end, new_length)) 
    user_annuity = calc_annuity(user_contrib, user_apr, new_length, compound_frequency) 
    print('The APR for '+str(stock_name)+' was: '+str(user_apr)+'%') 
    print('If you had invested $'+str(user_contrib)+' every month in '+str(stock_name)+' over 5 years you would have: $'+str(user_annuity)+'\n') 
    
    aapl_apr = calc_apr(aapl_start, aapl_end, aapl_length)
    aapl_annuity = calc_annuity(contribution, aapl_apr, aapl_length, compound_frequency)
    print('The APR for AAPL was: '+str(aapl_apr)+'%')
    print('If you had invested $'+str(contribution) +' every month in AAPL over 5 years you would have: $'+str(aapl_annuity)+'\n')
    
    ntdoy_apr = calc_apr(ntdoy_start, ntdoy_end, ntdoy_length)
    ntdoy_annuity = calc_annuity(contribution, ntdoy_apr, ntdoy_length, compound_frequency)
    print('The APR for NTDOY was: '+str(ntdoy_apr)+'%')
    print('If you had invested $'+str(contribution) +' every month in NTDOY over 5 years you would have: $'+str(ntdoy_annuity)+'\n')
    
    spy_apr = calc_apr(spy_start, spy_end, spy_length)
    spy_annuity = calc_annuity(contribution, spy_apr, spy_length, compound_frequency)
    print('The APR for SPY was: '+str(spy_apr)+'%')
    print('If you had invested $'+str(contribution) +' every month in SPY over 5 years you would have: $'+str(spy_annuity)+'\n')
    
    tsla_apr = calc_apr(tsla_start, tsla_end, tsla_length)
    tsla_annuity = calc_annuity(contribution, tsla_apr, tsla_length, compound_frequency)
    print('The APR for TSLA was: '+str(tsla_apr)+'%')
    print('If you had invested $'+str(contribution) +' every month in TSLA over 5 years you would have: $'+str(tsla_annuity))
    
stocks_final()