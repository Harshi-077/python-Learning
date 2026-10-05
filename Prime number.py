
t=int(input("Enter no.of test cases: "))
for i in range(t):
    n=int(input("Enter a number:"))
    if n>2:
        for j in range(2,int(n**0.5)+1):
            if n%j==0:
                print("Not a prime")
            else:
                print("Prime")