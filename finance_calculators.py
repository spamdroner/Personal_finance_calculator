# author:   spamdroner@icloud.com
# date:     16th - 23rd October 2022
# desc:     Capstone project: investment and home loan repayment calculator

import math 

# Ask user which calculator they would like to use
calculator = input("""From the menu below, choose which calculator you'd like to use: 

investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan. \n""").lower()

# Check whether user made the correct selection/input
if (calculator == "bond") or (calculator == "investment"):
    print(f"You have chosen to use the {calculator} calculator.")
else:
    print(f"You have entered '{calculator}' which isn't an appropriate selection. " +
    "Please choose again.")

# calculations for investment earnings or home loan repayments
if calculator == "investment": #investment calculator
    user_investment = float(input("How much money will you initially deposit? "))
    interest_rate = float(input("What is the applicable interest rate? " +
    "(enter only the number - do not enter the % symbol): "))
    number_of_years = int(input("How many years will you be investing for? "))
    interest = input("Do you want a simple or compound interest rate? ").lower()

    # In the formulae below the following represent:
    # 'r' is the interest rate
    # 'P' is the amount the user deposits
    # 't' is the number of years that money is being invested for
    # 'A' is the total amount once interest has been applied
    
    if interest == "simple": # calculations for simple interest rate
        # formula: A = P * (1 + r * t)
        r = interest_rate / 100
        total_amount = user_investment * (1 + r * number_of_years)
        interest_earned = total_amount - user_investment # interest earned 
        print(f"Your total investment at maturity will be R{round(total_amount, 2)}")
        print(f"You will earn interest of R{round(interest_earned, 2)} over the course " + 
        f"of {number_of_years} years.") # 2 print statements for clea output.

    elif interest == "compound": # calculations for compound interest
        # formula: A = P(1+r) ^ t
        total_amount = user_investment * (1+(interest_rate/100)) ** number_of_years
        interest_earned = total_amount - user_investment
        print(f"Your total investment at maturity will be R{round(total_amount, 2)}")
        print(f"You will earn interest of R{round(interest_earned, 2)} over the course " + 
        f"of {number_of_years} years.") # 2 print statements for clea output.
    
    else: # output to display if user didn't make the appropriate selection
        print(f"Your selection '{interest}' is not correct. Please choose again.")

else: # ELSE defaults to bond since it's the only alternative
    value_of_house = float(input("What is the present value of the house? "))
    interest_rate = float(input("What is the applicable interest rate? " +
    "(enter only the number without the % symbol) "))
    number_of_months = int(input("How many months will you be making repayments for? "))

    # formula for calculating home loan repayment: x = (i.P)/(1 - (1+i) ** (-n))
    # In the formula the following represent:
    # 'P' is the present value of the house
    # 'i' is the monthly interest rate (annual interest rate / 100)
    # 'n' is the number of months over which the bond will be repaid

    i = interest_rate / 100 / 12 
    P = value_of_house
    n = number_of_months
    total_amount = (i * P) / (1 - math.pow((1+i), -n))

    print(f"For a house with the value of R{value_of_house} and an interest ")
    print(f"rate of {interest_rate}%, repayable over {number_of_months} months, ")
    print(f"the monthly repayable amount is R{round(total_amount, 2)}")
