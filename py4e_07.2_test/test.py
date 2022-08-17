# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
if fname != "mbox-short.txt" : fname = "mbox-short.txt"
fh = open(fname)

count = 0
compute = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    _lookup = line.find(":")
    _num = line[_lookup+1:].strip()
    num = float(_num)
    compute = num + compute

print("Average spam confidence:", compute/count)
