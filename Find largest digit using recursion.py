def largest_digit(n):
    if n==0:
        return 0
    return max(n%10, largest_digit(n//10))
n=int(input("Enter a number: " ))
print(largest_digit(n))