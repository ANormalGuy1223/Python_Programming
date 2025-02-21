marks=int(input("Enter the marks: "))

if marks > 70:
    print("You got A grade")
elif marks > 60 and marks < 70:
    print("You got B grade")
elif marks > 50 and marks < 60:
    print("You got C grade")
elif marks > 40 and marks < 50:
    print("You got D grade")
else:
    print("You got F grade")