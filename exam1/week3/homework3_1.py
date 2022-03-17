# Homework for CSC184-40
#
# Author: Beau McDowell
# Date: 09FEB2020
#
# calculate amount you can barrow based off of $2850 or $1600 a month downpayment of 75000 and PMI at 1.8
down_payment = 75000 # $75,000 down payment

# lets user choose between 2850 or 1600 a month to calculate loan. assign chosen input to monthly_max variable.
def chose_max():
    monthly_max1 = 2850 # monthly max in dollars
    monthly_max2 = 1600 # monthly max in dollars
    print("1:) $2850 a month.")
    print("2:) $1600 a month.")
    monthly_inp = input(
        "Choose the amount you want to spend monthly on a house : ")
    if monthly_inp == "1":
        monthly_max = monthly_max1
        print("Using $"+str(monthly_max1)+" as monthly payment.")
    elif monthly_inp == "2":
        monthly_max = monthly_max2
        print("Using $"+str(monthly_max2)+" as monthly payment.")
    else:
        print("You must select a monthly payment.")
        return chose_max() # if user doesn't select valid option or doesn't input anything, rerun function until valid input is received.
    return monthly_max
monthly_max = chose_max()

# let use choose between 3 different interest rates and assign the chosen rate to the mortgage_rate variable.
def chose_loan():
    mortgage_rate1 = 0.04750  # loan option 1 apr 4.75%
    mortgage_rate2 = 0.0525  # loan option 2 apr 5.25%
    mortgage_rate3 = 0.0613  # loan option 3 apr 6.13%
    #print mortgage rate options times 100 to show percentage
    print("Loan 1: "+str(mortgage_rate1*100)+'%')
    print("Loan 2: "+str(mortgage_rate2*100)+'%')
    print("Loan 3: "+str(mortgage_rate3*100)+'%')
    apr_inp = input("Choose Loan (1, 2, 3) : ")
    if apr_inp == "1":
        mortgage_rate = mortgage_rate1
        print("Calculating loan amount using 1:) " +
              str(mortgage_rate1*100)+'% '+'interest')
    elif apr_inp == "2":
        mortgage_rate = mortgage_rate2
        print("Calculating loan amount using 2:) " +
              str(mortgage_rate2*100)+'% '+'interest')
    elif apr_inp == "3":
        mortgage_rate = mortgage_rate3
        print("Calculating loan amount using 3:) " +
              str(mortgage_rate3*100)+'% '+'interest')
    else:
        print("You must chose an an interest rate!")
        return chose_loan() # if user doesn't select valid option or doesn't input anything, rerun the function until valid input is received.
    return mortgage_rate
mortgage_rate = chose_loan()

def calc_can_barrow():  # calculate the amount user can barrow based on chosen monthly_max
    can_barrow = (monthly_max)*(1-(1+(mortgage_rate/12))**(-12*30))/(mortgage_rate/12)
    can_barrow = round(can_barrow, 2) # round can_barrow amount to 2 decimals places
    return can_barrow
can_barrow = calc_can_barrow()

# determine whether PMI will be payed. if down payment is less than 20% of what you can barrow then you must pay PMI at 1.8%
def pay_pmi():
    if down_payment > can_barrow*0.20:
        pmi = True
        print("You will have to pay PMI")
    else:
        pmi = False
        print("You will not have to pay PMI")
    return pmi
    
def calc_adjusted_barrow():
    pmi = pay_pmi()
    pmi_payment = can_barrow*pmi*0.018 # determine total PMI payment at 1.8%
    print("Total PMI payment is : $"+str(round(pmi_payment,2))) # round pmi payment 2 decimal places
    adjusted_barrow = can_barrow - pmi_payment # if paying PMI subtract the total PMI payments from the loan principal(can_barrow) else subtract 0(False)
    print("After calculating for PMI and your downpayment you can barrow $"+str(round(adjusted_barrow,2)))
    return adjusted_barrow
adjusted_barrow = calc_adjusted_barrow()

def calc_mortgage_payment(): # calculate total mortgage payment factoring in PMI and down payment
    mortgage_payment = adjusted_barrow/((1-(1+mortgage_rate/12)**(-12*30))/(mortgage_rate/12))
    mortgage_payment = round(mortgage_payment, 2)# round mortgage payment result to 2 decimal places
    return print("Your monthly mortgage payment will be $"+str(mortgage_payment))
mortgage_payment = calc_mortgage_payment()

def calc_house_value(): # calc the total house value you can afford with downpayment
    house_value = down_payment + can_barrow
    return house_value
house_value = calc_house_value()

print("With a down payment of $"+str(down_payment)+" and a monthly max payment of $" +
      str(monthly_max)+",\n"+"you can get a mortgage for $"+str(adjusted_barrow)
      +" for a total house value of $"+str(house_value))

