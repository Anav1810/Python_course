make list variables "text" and "code"
open file and extract its content into a string variable
split on basis of space to get a list of words
create a boolean variable "FLAG" whose value is "True"
loop over this list
    if FLAG is true
        keep adding words to "text"
    if the word is "NM_START" then
        append a "/" into text
        FLAG = False
    if FLAG is False
        keep adding words to "code"
    if the word is "NM_END"
        append "/" to code
        FLAG = True