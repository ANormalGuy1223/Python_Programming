ind = int(input("Enter the points of ind: "))
pak = int(input("Enter the points of pak: "))
aus = int(input("Enter the points of aus: "))

if ind > pak:
    if ind > aus:
        print("India won the game")
    else:
        print("Australia won the game")
else:
    if pak > aus:
        print("Pakistan won the game")
    else:
        print("Australia won the game")