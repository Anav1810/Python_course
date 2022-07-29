filepath = "sample1.txt"
fileobj = open(filepath, "r")

FLAG = True
while FLAG:
    content = fileobj.readline()
    if content == "":
        FLAG = False
    print(content, end="")

fileobj.close()