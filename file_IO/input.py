# for i in list(map(int, input("Enter value: ").split())):
#     print(i*5)


# for var in [ele*5 for ele in list(map(int, input("Enter value: ").split()))]:
#     print(var)



def input2():
    a = float(input("Enter first: "))
    b = float(input("Enter second: "))
    return a + b


print(input2())