from urllib.request import urlopen


fhand = urlopen("https://www.paypal.com/myaccount/summary")

for line in fhand:
    print(line.decode().strip())
