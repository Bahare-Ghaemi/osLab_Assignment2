import math

while True:

    print("welcome to my calculator!")
    print("+ sum")
    print("- sub")
    print("* mul")
    print("/ div")
    print("sin")
    print("cos")
    print("tan")
    print("cot")
    print("log")
    print("exit")

    op = input("enter operator : ")

    if op=='sin' or op=='cos' or op=='tan' or op=='cot' or op=='log':
        a = int(input("enter number : "))
    else:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))

    if op == '+':
        result = a+b
    elif op == '-':
        result = a-b
    elif op == '*':
        result = a*b
    elif op == '/':
        if b!= 0:
            result = a/b
        else:
            "can not devide by 0 !!!"
    elif op == 'sin':
        result = math.sin(a)
    elif op == 'cos':
        result = math.cos(a)
    elif op == 'tan':
        result = math.tan(a)
    elif op == 'cot':
        result = math.cot(a)
    elif op == 'log':
        result = math.log(a)
    elif op == 'exit':
        break
    else:
        "command not found !!!"

    print(result)