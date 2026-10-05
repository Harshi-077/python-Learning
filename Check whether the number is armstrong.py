def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


def armstrong_sum(n, digits):
    if n == 0:
        return 0

    digit = n % 10
    return digit ** digits + armstrong_sum(n // 10, digits)


n = int(input("Enter a number: "))

if n < 0:
    print("Armstrong numbers are checked here for non-negative integers.")
else:
    digits = count_digits(n)
    total = armstrong_sum(n, digits)

    if total == n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")