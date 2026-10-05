def count_digit(n, digit):
    if n == 0:
        return 0

    if n % 10 == digit:
        return 1 + count_digit(n // 10, digit)
    else:
        return count_digit(n // 10, digit)


n = int(input("Enter a number: "))
digit = int(input("Enter the digit to count: "))

print("Count:", count_digit(n, digit))