def print_number(n):
    if n>10:
        return
    print(n, end=" ")
    print_number(n+1)
print_number(1)