name = input("Enter your age:")
while name =="":
    print("You did not enter your name:")
    name = input("Enter your name:")
    print(f"Hello {name} ")

    #age

age = int(input("Enter your age:"))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age:"))
    print(f"you are {age} years old")

#food
food = input("enter a food you like (q to quit:)")
while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like (q to quit:)")

    print("bye")
    