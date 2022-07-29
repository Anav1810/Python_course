from msilib.schema import ControlEvent


filepath = "HW/files/file6.txt"
code = []
text = []


with open(filepath, "r") as fo:
    content = fo.read()
starts = []
ends = []
for i in range(len(content)):
    if content.startswith('NM_START', i):
        print(i)
        starts.append(i)

for i in range(len(content)):
    if content.startswith('NM_END', i):
        ends.append(i)

a = 0
for i in range(len(starts)):
    codestr = content[int(starts[i]+8): int(ends[i])]
    textstr = content[a: starts[i]]
    a = a+ends[i]+6
    code.append(codestr)
    text.append(textstr)
print(text)
print(code)