def reverse_number(n, rev=0):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit

    return reverse_number(n // 10, rev)


def is_palindrome(n):
    original = n
    reversed_num = reverse_number(n)

    return original == reversed_num


n = int(input("Enter a number: "))

if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")