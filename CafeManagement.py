# Menu of restraurant

menu = {
    'Burger': 50,
    'Pizza': 100,
    'Pasta': 120,
    'French Fries': 40,
    'Sandwich': 60,
    'Hot Dog': 40,
    'Coke': 30,
    'Pepsi': 30,
    'Sprite': 30,
    'Fanta': 30,
    'Mirinda': 30,
    '7 Up': 30,
    'Mountain Dew': 30,
    'Dew': 30,
    'Cold Coffee': 50,
    'Hot Coffee': 50,
    'Cold Tea': 30,
    'Hot Tea': 30,
    'Ice Cream': 20,
    'Cake': 30,
}

print("Welcome to the restaurant")
print("Burger: Rs50\nPizza: Rs100\nPasta: Rs120\nFrench Fries: Rs40\nSandwich: Rs60\nHot Dog: Rs40\nCoke: Rs30\nPepsi: Rs30\nSprite: Rs30\nFanta: Rs30\nMirinda: Rs30\n7 Up: Rs30\nMountain Dew: Rs30\nDew: Rs30\nCold Coffee: Rs50\nHot Coffee: Rs50\nCold Tea: Rs30\nHot Tea: Rs30\nIce Cream: Rs20\nCake: Rs30\n")

order_total = 0

item_1 = input("Enter the item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print (f"Your item{item_1} has been added to your order")
    print (f"Your total amount is {order_total}")

else: 
    print(f"Ordered item {item_1} is not available yet")

another_order = input("Do you want to order anything else? (Yes/No): ")

if another_order == "Yes":
    item_2 = input("Enter the name of second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet!")

else:
    print(f"Thank you, Your total amount is {order_total}")
print (f"The total amount of item is {order_total}")
print ("Goodbye")