
t=int(input("Enter n.of test cases: "))
for _ in range(t):
    n=int(input("Enter a number: "))
    a=0
    b=1

    for i in range(n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
    print()
