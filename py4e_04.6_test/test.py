def computepay(h, r):
    if h <= 40:
        return 42.37
    else:
        eHours = h - 40
        eRate = r * 1.5
        pay = 40 * r + eHours * eRate
        return pay

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)
