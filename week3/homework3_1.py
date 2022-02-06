# Create a python program that figures out how much house you can afford with the following restrictions.
# You have only $2850 per month spare for mortgages payments, taxes and PMI insurance.
# You have $75,000 for a down payment.
# If you pay PMI the rate is 1.8% of the mortgage payments
# Taxes are 2.7% of the value of the home to be paid monthly.
# You have 3 different mortgage companies offering 4.75%, 5.25% and 6.13% APR on 30 year mortgages.
# How much house can you afford for each of the different rates.

# Title: Calculating more realistic Mortgage Payments
#
# Description: input credit rating, 30 year fixed, PMI, property taxes and give back mortgage payments
#
# Author: Gavin Waters
# Date: 02/02/2022
#
# 

def calc_mortgage_payment(mortgage_principal, mortgage_rate,mortgage_term):
    # assume that is is a monthly payments
    mortgage_rate = mortgage_rate/100
    mortgage_payment = mortgage_principal/((1-(1+mortgage_rate/12)**(-12*mortgage_term))/(mortgage_rate/12))
    mortgage_payment = round(mortgage_payment,2)
    return mortgage_payment

house_value = float(input('Please input the value of the property: '))
mortgage_rate = float(input('Please input the mortgage rate: '))
mortgage_term = int(input('Please input the mortage length in years: '))
credit_rating = int(input('Please input your credit rating(600-800) :'))
down_payment = float(input('Please input down payment: '))
vary_rate_credit_rating= mortgage_rate*0.18/2
vary_of_credit_rating = credit_rating-700
mortgage_rate = mortgage_rate - vary_rate_credit_rating*vary_of_credit_rating/100
property_taxes = round(house_value*0.027/12,2)

if down_payment>house_value*0.2:
    PMI= True
else:
    PMI=False

mortgage_principal = house_value - down_payment
mortgage_payment = calc_mortgage_payment(mortgage_principal,mortgage_rate,mortgage_term)
mortgage_payment = mortgage_payment + mortgage_payment*PMI*0.013
total_monthly_payments = round(mortgage_payment + property_taxes,2)

print()
print('The total monthly payments for a house value of $'+str(house_value)+ ' with a down payment of $'+ str(down_payment)+' will be $'+str(total_monthly_payments))