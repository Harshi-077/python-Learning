def is_power_of_2(n):
    if n == 1:
        return True

    if n < 1 or n % 2 != 0:
        return False

    return is_power_of_2(n // 2)


n = int(input("Enter a number: "))

print(is_power_of_2(n))