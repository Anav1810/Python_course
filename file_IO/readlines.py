# filename = "sample1.txt"
# fileobj = open(filename, "r")
# content = fileobj.readlines()
# print(type(content))
# print(len(content))
# print(content)
# fileobj.close()




# filename = "sample1.txt"
# fileobj = open(filename, "r")
# for line in fileobj.readlines():
#     print(line)
# fileobj.close()



# No output will be printed for second loop as the file pointer
# reached the end of the file in the first loop and file was not closed


# filename = "sample1.txt"
# fileobj = open(filename, "r")
# for line in fileobj.readlines():
#     print(line)



# for line in fileobj.readlines():
#     print(line)



# This time both the loops will generate outpouts as we have used
# close() properly
filename = "sample1.txt"
fileobj = open(filename, "r")
for line in fileobj.readlines():
    print(line)
fileobj.close()

fileobj = open(filename, "r")
for line in fileobj.readlines():
    print(line)
fileobj.close()
