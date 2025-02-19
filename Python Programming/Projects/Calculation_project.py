num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))
choice=int(input("""
                 Press 1 for addition
                 Press 2 for subtraction
                 Press 3 for multiplication
                 Press 4 for division
                 
                 Enter your choice: """))


if choice==1:
    ans=num1+num2
elif choice==2:
    ans=num1-num2
elif choice == 3:
    ans= num1*num2
elif choice == 4:
    ans = num1/num2
else:
    print("You have entered the wrong number")
    
print(f"Answer is {ans}")    