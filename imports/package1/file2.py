"""
import file1
from file1 import fun1


fun1()
file1.fun2()
"""
from file1 import *


fun1()
fun2()
print("Print from file 2: ", a, b)

"""
From file 1  23 64
fun1 running
fun2 executing
Print from file 2: 23 64
"""