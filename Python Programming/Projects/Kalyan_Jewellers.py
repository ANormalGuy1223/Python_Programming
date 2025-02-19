#(totalamount*25)/100
#Male>65: 
#21-31k: 20%
#32-51: 30%
#51k+: 35%
#Male<65: 
#21-31k: 10%
#32-51: 20%
#51k+: 25%
#Female>65: 
#21-31k: 25%
#32-51: 35%
#51k+: 40%
#Female<65: 
#21-31k: 20%%
#32-51: 30%
#51k+: 35%
print("Welcome to Kalyan Jwellers!\n")
name = input("Enter your name: ")
gender = input("Enter your gender (M/F): ")
age = int(input("Enter your age: "))

product=input("Enter product: ")
gram=int(input("Enter Product gram: "))

print("Current gold price: 7975")
totalgold=gram*7975
print(f"Total Gold rate: {totalgold}")
makingcharges=845
print("---------------------------------------")

print(f"Making Charges (1 Gram): {makingcharges}")
tmakingcharges=gram*makingcharges
print(f"Total Making Charges: {tmakingcharges}")

totalamount=totalgold +  tmakingcharges

print("---------------------------------------")

print(f"Total Amount: {totalamount}")

if gender == "M" and age > 65:
    if totalamount > 21000 and totalamount < 31000:
        print("Discount = 20%")
        discountam=(totalamount*20)/100
    if totalamount > 31000 and totalamount < 51000:
        print("Discount = 30%")
        discountam=(totalamount*30)/100
    if totalamount > 51000:
        print("Discount = 35%")
        discountam=(totalamount*35)/100
    
elif gender == "M" and age < 65:
    if totalamount > 21000 and totalamount < 31000:
        print("Discount = 10%")
        discountam=(totalamount*10)/100
    if totalamount > 31000 and totalamount < 51000:
        print("Discount = 20%")
        discountam=(totalamount*20)/100
    if totalamount > 51000:
        print("Discount = 25%")
        discountam=(totalamount*25)/100

elif gender == "F" and age > 65:
    if totalamount > 21000 and totalamount < 31000:
        print("Discount = 25%")
        discountam=(totalamount*25)/100
    if totalamount > 31000 and totalamount < 51000:
        print("Discount = 35%")
        discountam=(totalamount*35)/100
    if totalamount > 51000:
        print("Discount = 40%")
        discountam=(totalamount*40)/100
    
else:
    if totalamount > 21000 and totalamount < 31000:
        print("Discount = 20%")
        discountam=(totalamount*20)/100
    if totalamount > 31000 and totalamount < 51000:
        print("Discount = 30%")
        discountam=(totalamount*30)/100
    if totalamount > 51000:
        print("Discount = 35%")
        discountam=(totalamount*35)/100

print(f"Discount Amount: {discountam}")
print("---------------------------------------")
print(f"\nNetworth: {totalamount-discountam}")
print("---------------------------------------")
