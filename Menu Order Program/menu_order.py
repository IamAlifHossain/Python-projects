menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25,
        "KFC": 2.99
        }

cart = []
total = 0
print("-------MENU-------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------")
while True:
    food = input("Enter food items (q to quit) = ")
    if food.lower()=="q":
        break
    elif menu.get(food) !=None:
        cart.append(food)
i = 1
print("-------Your Order-------")
for food in cart:
    print(f"{i}. {food}", end=" ")
    total+=menu.get(food)
    i+=1
print()
print(f"Total bill = ${total:.2f}")