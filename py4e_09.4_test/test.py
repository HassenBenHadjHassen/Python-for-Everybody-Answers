name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dct = dict()

for line in handle:
    line.strip()
    if not line.startswith("From ") : continue
    words = line.split()
    dct[words[1]] = dct.get(words[1], 0) + 1

count = None
email = None

for key in dct:
    if count is None : count = dct[key]

    if count < dct[key]:
        count = dct[key]
        email = key
print(email, count)

