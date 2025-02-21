temp = int(input("Enter the temprature: "))

if temp >= 0 and temp <= 100:
    print("Water")
elif temp > 100:
    print("Air")
else :
    print("Ice")