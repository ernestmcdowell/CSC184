# Title: Homework2_1 for CSC-184-40
#
# Description: Take user input of stocks and calculate APR over a 5 year period
#
# Author: Ernest B McDowell
# Date: 26JAN2022
#
#

def tsla(): #calculate apr and annuity for TSLA over 5 years
    start_price = 50.00 
    end_price = 821.10
    time_length = 5
    compound_frequency = 12
    contribution = 100
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*time_length))-1)
    calced_rate = (float(round(rate*100,2)))
    print('The APR for TSLA over the last 5 years was: '+str(calced_rate)+'%')
    annuity = contribution*((1+(calced_rate/100)/compound_frequency)**(compound_frequency*time_length)-1)/(calced_rate/compound_frequency)
    print('If you had invested 100 dollars a month in TSLA for 5 years you would have: $'+str(round(annuity*100,2)))

def spy(): #calculate apr and annuity for SPY over 5 years
    start_price = 236.47
    end_price = 431.24
    time_length = 5
    compound_frequency = 12
    contribution = 100
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*time_length))-1)
    calced_rate = (float(round(rate*100,2)))
    print('The APR for SPY over the last 5 years was: '+str(calced_rate)+'%')
    annuity = contribution*((1+(calced_rate/100)/compound_frequency)**(compound_frequency*time_length)-1)/(calced_rate/compound_frequency)
    print('If you had invested 100 dollars a month in SPY for 5 years you would have: $'+str(round(annuity*100,2)))

def aapl(): #calculate apr and annuity for AAPL over 5 years
    start_price = 34.25
    end_price = 159.22
    time_length = 5
    compound_frequency = 12
    contribution = 100
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*time_length))-1)
    calced_rate = (float(round(rate*100,2)))
    print('The APR for AAPL over the last 5 years was: '+str(calced_rate)+'%')
    annuity = contribution*((1+(calced_rate/100)/compound_frequency)**(compound_frequency*time_length)-1)/(calced_rate/compound_frequency)
    print('If you had invested 100 dollars a month in AAPL for 5 years you would have: $'+str(round(annuity*100,2)))

def ntdoy(): #calculate apr and annuity for NTDOY over 5 years
    start_price = 26.11
    end_price = 61.19
    time_length = 5
    compound_frequency = 12
    contribution = 100
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*time_length))-1)
    calced_rate = (float(round(rate*100,2)))
    print('The APR for NTDOY over the last 5 years was: '+str(calced_rate)+'%')
    annuity = contribution*((1+(calced_rate/100)/compound_frequency)**(compound_frequency*time_length)-1)/(calced_rate/compound_frequency)
    print('If you had invested 100 dollars a month in NTDOY for 5 years you would have: $'+str(round(annuity*100,2)) +'\n')

def calc_stock_apr():
    print('Calculate the APR of another stock.') #Title to show what is being calculated 
    start_price = float(input('Enter stock starting price: ')) #starting price of the stock 
    end_price = float(input('Enter the stock ending price: ')) #ending price of the stock 
    length_of_investment = 5 # length of the investment in years
    compound_frequency = int(input('Enter the frequency at which interest will compound: ')) # frequency at which interest will compound ie. monthly(12), weekly(52) etc..
    rate = compound_frequency*((end_price/start_price)**(1/(compound_frequency*length_of_investment))-1) # compound interest formula
    return float(round(rate*100,2)) # multiplies the result of rate by 100 to get percentage and rounds to 2 decimal places

def calc_annuity():
    print('Calculate annuity from stock.') #Title to show what is being calculated
    rate = float(input('Enter the APR: ')) # enter the APR given from the previous calculation
    length_of_investment = 5 # investment length in years
    compound_frequency = 12 # frequency interest will be compounded
    contribution = 100 # dollar amount of monthly contribution
    annuity = contribution*((1+(rate/100)/compound_frequency)**(compound_frequency*length_of_investment)-1)/(rate/compound_frequency) # annuity formula 
    return round(annuity*100,2) # multiply annuity result by 100 for proper decimal placement and rounds the result from annuity to 2 decimal places

tsla()
spy()
aapl()
ntdoy()


print(calc_stock_apr())
print(calc_annuity())