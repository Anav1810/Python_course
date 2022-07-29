filepath = "sample1.txt"
fileobj = open(filepath, "r")
for line in fileobj:
    print(line)
fileobj.close()