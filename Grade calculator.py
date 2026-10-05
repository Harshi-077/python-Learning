
marks=int(input("Enter  your marks: "))
Grade="False"

if marks>=90:
    Grade="A"
elif marks>=80 and marks<90:
    Grade="B"
elif marks>=70 and marks<80:
    Grade="C"
elif marks>=60 and marks<70:
    Grade="D"
else:
    Grade="F"
print(f"Your grade is: {Grade}")
    