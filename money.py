import math

n = int(input("Enter amount: "))
if n >= 25:
    quarter = math.floor(n/25)
    print("You have", quarter, "quarter(s)")
    total_quarter = 25 * quarter
    n -= total_quarter
if n >= 10:
    dime = math.floor(n/10)
    print("and", dime, "dime(s)")
    total_dime = 10 * dime
    n -= total_dime
if n >= 5:
    nickel = math.floor(n/5)
    print("and", nickel, "nickel(s)")
    total_nickel = 5 * nickel
    n -= total_nickel
if n >= 1:
    penny = math.floor(n/1)
    print("and", penny, "penny(s)")
    total_penny = 1 * penny
    n -= total_penny
