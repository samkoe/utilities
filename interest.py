# interest.py
#
# Interest Calculator for Loan Repayment

from math import log

# Constants
rate = 0.04
balance = 111
monthly_payment = 111

# Formulas
i = (1 + (rate / 360)) ** 30 - 1

months = (-log(1 - (balance / monthly_payment) * i)) / (log(1 + i))

print(months)
print(months / 12)