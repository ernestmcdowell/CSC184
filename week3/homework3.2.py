# Homework for CSC184-40
#
# Create a program that will figure out mortgage payment. taxes and PMI insurance.
#
# Author: Beau McDowell
# Date: 04FEB2022
#
#
# Variables
monthly_max = float(2850)
down_payment = float(75000.00)
pmi = float(.0180)
prop_tax = monthly_max*(0.027*12)
mortgage_term = float(30.00)

def chose_loan():
    mortgage_rate1 = 0.04750
    mortgage_rate2 = 0.0525
    mortgage_rate3 = 0.0613
    print("Loan 1: "+str(mortgage_rate1*100)+'%')
    print("Loan 2: "+str(mortgage_rate2*100)+'%')
    print("Loan 3: "+str(mortgage_rate3*100)+'%')
    inp = input("Chose Loan (1, 2, 3) : ")
    if inp == "1":
        mortgage_rate = mortgage_rate1
        print("Calculating loan amount using Loan 1: " +
              str(mortgage_rate1*100)+'% '+'interest')
    elif inp == "2":
        mortgage_rate = mortgage_rate2
        print("Calculating loan amount using Loan 2: " +
              str(mortgage_rate2*100)+'% '+'interest')
    elif inp == "3":
        mortgage_rate = mortgage_rate3
        print("Calculating loan amount using Loan 3: " +
              str(mortgage_rate3*100)+'% '+'interest')
    else:
        print("You must chose an option")
        return chose_loan()
    return mortgage_rate
mortgage_rate = chose_loan()

def calc_can_barrow():
    # assume that is is a monthly payments
    can_barrow = (monthly_max)*(1-(1+(mortgage_rate/12))**(-12*30))/(mortgage_rate/12)*(prop_tax/100)
    can_barrow = round(can_barrow,2)
    return float(can_barrow)

barrowable = calc_can_barrow()

def calc_mortgage_payment():
    # assume that is is a monthly payments
    mortgage_payment = barrowable/((1-(1+mortgage_rate/12)**(-12*mortgage_term))/(mortgage_rate/12))
    mortgage_payment = round(mortgage_payment)
    return mortgage_payment
monthly_payment = calc_mortgage_payment()


# if down_payment > house_value*0.2:
#     pmi = True
# else:
#     pmi = False

print('Property Taxes: $'+str(prop_tax))
calc_can_barrow()
print('Monthly Payment: $'+str(monthly_payment))
print('With a downpayment of $'+str(down_payment)+' and max monthly payment of $'+str(monthly_max)+' you can get a loan for $'+str(barrowable))

# calc_mortgage_payment()
