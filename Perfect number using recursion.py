def sum_divisors(n, i=1):
    if i >= n:
        return 0

    if n % i == 0:
        return i + sum_divisors(n, i + 1)

    return sum_divisors(n, i + 1)


n = int(input("Enter a number: "))

if n > 1 and sum_divisors(n) == n:
    print("Perfect number")
else:
    print("Not a perfect number")