

n=int(input("Enter a number: "))
if n>0 and (n & (n-1))==0:
    print("Yes")
elif n%2==0:
    print("No")
else:
    print(n)