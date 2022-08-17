name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dct = {}
lst = []

for line in handle:
    if not line.startswith("From ") : continue
    words = line.split()
    hour = words[5].split(":")
    dct[hour[0]] = dct.get(hour[0], 0) + 1

for k,v in dct.items():
    lst.append((k,v))
lst.sort()

for k,v in lst:
    print(k,v)
