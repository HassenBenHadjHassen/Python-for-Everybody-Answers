largest = None
smallest = None
while True:
    try:
        _num = input("Enter a number: ")
        if _num == "done":
            break
        num = int(_num)

    except:
        print("Invalid input")

    if largest is None : largest = num
    if num > largest : largest = num

    if smallest is None : smallest = num
    if num < smallest : smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
