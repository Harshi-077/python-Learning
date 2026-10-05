
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("Enter operator: ")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if b==0:
        print("Division by zero is not allowed")
    else:
        print(a/b)
elif op=="%":
    if b==0:
        print("Division by zero is not allowed")
    else:
        print(a%b)
else:
    print("Invalid operator")