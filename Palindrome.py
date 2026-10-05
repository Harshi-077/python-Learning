t=int(input("Enter no.of test cases: "))
for _ in range(t):
    n=int(input("Enter a number:"))
    if n>1:
        s=str(n)
        n1=s[::-1]
    if n==n1:
        print("palindrome")
    else:
        print("Not a palindrome")
