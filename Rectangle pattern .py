n=int(input("Enter a number:"))
for i in range(n):
    for j in range(n):
        if j==n-1-i:
            print("*",end="")
        else:
            print(n-j,end="")
    print()