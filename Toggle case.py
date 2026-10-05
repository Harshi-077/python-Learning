x=input("Enter string: ")
result =""
for ch in x:
    if ch.isupper():
        result+=ch.lower()
    if ch.islower():
        result+=ch.upper()
print(result)