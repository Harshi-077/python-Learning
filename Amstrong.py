t=int(input("Enter no.of test cases:"))
for _ in range(t):
    n=int(input("Enter a number: "))
    sum=0
    digits=len(str(n))
    temp=n
    while temp>0:
        digit=temp%10
        sum=sum+digit**digits
        temp=temp//10
    if sum==n:
        print("Amstrong number")
    else:
        print("Not an Amstrong number")
