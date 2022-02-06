monthly_max = 2850
down_payment = 75000
prop_tax_rate = 0.0270

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

def calc_can_barrow(): # calculate the amount user can barrow based on monthly_max 
    can_barrow = (monthly_max)*(1-(1+(mortgage_rate/12))**(-12*30))/(mortgage_rate/12)
    can_barrow = round(can_barrow,2)
    return float(can_barrow)
can_barrow = calc_can_barrow()
corrected_barrow = can_barrow - can_barrow*prop_tax_rate
print("With a monthly payment of $2850.00 you can afford a loan of $"+str(round(corrected_barrow,2)))

def calc_mortgage_payment():
    mortgage_payment = corrected_barrow/((1-(1+mortgage_rate/12)**(-12*30))/(mortgage_rate/12))
    mortgage_payment = round(mortgage_payment,2)
    return mortgage_payment
payment = calc_mortgage_payment()
print(payment)

if down_payment > corrected_barrow*0.18:
    PMI = True
    print("Paying PMI")
else:
    PMI = False
    print("Not Paying PMI")

mortgage_principal = corrected_barrow - down_payment
# mortgage_payment = calc_mortgage_payment()
payment = payment + payment*PMI*0.018
total_monthly_payments = round(payment,2)
print(str(total_monthly_payments)+str(mortgage_principal))

