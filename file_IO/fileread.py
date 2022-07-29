"""
The key function for working with files in Python is the **open()** function.

The **open()** function takes two parameters; **filename**, and **mode**.

There are four different methods (modes) for opening a file:

- "r" - Read - Default value. Opens a file for reading, error if the file does not exist

- "a" - Append - Opens a file for appending, creates the file if it does not exist

- "w" - Write - Opens a file for writing, creates the file if it does not exist

- "x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

- "t" - Text - Default value. Text mode

- "b" - Binary - Binary mode (e.g. images)
"""


# filepath = "sample3.txt"
# fo = open(filepath)
# fo = open(filepath, "rt")
# fo = open(filepath, "a")
# fo = open(filepath, "w")
# fo = open(filepath, "x")


# print(fo)
# fo.close()


filepath = "sample.txt"
fo = open(filepath, "r")
whole = fo.read(10)
print((whole))
fo.close()
