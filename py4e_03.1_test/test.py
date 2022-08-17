hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)

def Calculate():
    if h < 40:
        pay = h * r
    else:
        eHours = h - 40
        eRate = r * 1.5
        pay = 40 * r + eHours * eRate
    print(pay)

Calculate()
