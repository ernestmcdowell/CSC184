# Homework for CSC184-40
#
# Author: Beau McDowell
# Date: 09FEB2020
#
# calculate amount you can barrow based off of 2850 a month downpayment of 75000 and PMI at 1.8


down_payment = 75000


def chose_max():
    monthly_max1 = 2850
    monthly_max2 = 1600
    print("1:) $2850 a month.")
    print("2:) $1600 a month.")
    monthly_inp = input(
        "Chose the amount you want to spend monthly on a house.")

    if monthly_inp == "1":
        monthly_max = monthly_max1
        print("Using $"+str(monthly_max1)+" as monthly payment.")
    elif monthly_inp == "2":
        monthly_max = monthly_max2
        print("Using $"+str(monthly_max2)+" as monthly payment.")
    else:
        print("You must select a monthly payments.")
    return monthly_max


monthly_max = chose_max()


def chose_loan():
    mortgage_rate1 = 0.04750  # loan option 1 apr
    mortgage_rate2 = 0.0525  # loan option 2 apr
    mortgage_rate3 = 0.0613  # loan option 3 apr
    print("Loan 1: "+str(mortgage_rate1*100)+'%')
    print("Loan 2: "+str(mortgage_rate2*100)+'%')
    print("Loan 3: "+str(mortgage_rate3*100)+'%')
    apr_inp = input("Chose Loan (1, 2, 3) : ")
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
        print("You must chose an option")
        return chose_loan()
    return mortgage_rate


mortgage_rate = chose_loan()


def calc_can_barrow():  # calculate the amount user can barrow based on monthly_max
    can_barrow = (monthly_max)*(1-(1+(mortgage_rate/12))
                                ** (-12*30))/(mortgage_rate/12)
    can_barrow = round(can_barrow, 2)
    return can_barrow


can_barrow = calc_can_barrow()


def calc_mortgage_payment():
    mortgage_payment = can_barrow / \
        ((1-(1+mortgage_rate/12)**(-12*30))/(mortgage_rate/12))
    mortgage_payment = round(mortgage_payment, 2)
    return mortgage_payment


mortgage_payment = calc_mortgage_payment()

# if down_payment < can_barrow*0.20:
#     pmi = True
#     print("Paying PMI")
# else:
#     pmi = False
#     print("Not Paying PMI")

# mortgage_payment = mortgage_payment + mortgage_payment*pmi*0.018
print(mortgage_payment)
total_monthly_payments = round(mortgage_payment, 2)
print("With a down payment of $"+str(down_payment)+" and a monthly max payment of $" +
      str(monthly_max)+" you can get a loan for $"+str(round(can_barrow - down_payment, 2)))
