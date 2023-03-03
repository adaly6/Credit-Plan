# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:15:23 2023

@author: Andrew Daly

The purpose for this code is for a homework assignment in Computational Thinking. 
This code takes the input from a user and outputs a table of an indefinite amount of 
time the balance on a purchase price remains. The output table shows how many months 
are needed for repayment as defined by the fixed rates of 10% down payment, 12% annual
interest rate, and monthly payment of 5%.

"""


purchase_price = float(input("Enter the purchase price: "))
down_payment = purchase_price * 0.1
balance = purchase_price - down_payment
monthly_interest_rate = 0.12 / 12
monthly_payment = (purchase_price - down_payment) * 0.05

print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

month = 1
while balance > 0:
    interest = balance * monthly_interest_rate
    principal = monthly_payment - interest
    if balance < monthly_payment:
        monthly_payment = balance + interest
        principal = balance
    ending_balance = balance - principal
    
    if balance == principal:
        payment = balance
        interest = 0
    else:
        payment = monthly_payment
        
    print("{:3d} {:14.2f} {:16.2f} {:18.2f} {:12.2f} {:15.2f}".format(month, balance, interest, principal, payment, ending_balance))
    
    balance = ending_balance
    
    if balance == 0:
        monthly_payment = balance + interest
    
    month += 1

