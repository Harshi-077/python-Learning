
H=int(input('Enter first number: '))
D=int(input("Enter second number: "))
K=int(input("Enter third number: "))
if H>D and H>K:
    print(f"Largest is:{H}")
elif D>H and D>K:
    print(f"Largest is:{D}")
else:
    print(f"Largest is:{K}")