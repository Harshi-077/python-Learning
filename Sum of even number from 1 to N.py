def sum_even(n):
    if n<=0:
        return 0
    if n%2==0:
        return n+sum_even(n-1)
    return sum_even(n-1)
n=int(input("Enter a number: "))
print(sum_even(n))
    
