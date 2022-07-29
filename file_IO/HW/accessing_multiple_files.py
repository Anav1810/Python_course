import os


filespath = "files/"
files = os.listdir(filespath)

for file in files:
    filepath = os.path.join(filespath, file)
    print(filepath)