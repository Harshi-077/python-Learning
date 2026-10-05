
num=int(input("Enter a number:"))
if num%7==0 and num%5==0:
    print(f"{num} is divisible by 7 and 5")
elif num %7==0:
    print(f"{num} is divisible by 7 only")
elif num%5==0:
    print(f"{num} is divisible by 5 only")
else:
    print(f"{num} is not divisible by 7 and 5")