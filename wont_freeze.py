# exceptions_user_division_calc.py

from microbit import *

sleep(1000)

print("Division Calculations")

while True:
    text = input("Enter numerator n: ")
    n = float(text)

    text = input("Enter denominator d: ")
    d = float(text)

    q = n / d

    print("Quotient q: ")
    print("q = n / d")
    print("  = ", n, " / ", d)
    print("  = ", q)

    print("Try again!")
    print()
