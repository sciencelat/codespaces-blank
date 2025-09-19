print("Hello, welcome to the ordering food Chatbot")

name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")

choice = input("Would you like to check the menu first or just order? (menu/order): ")

if choice.lower() == "menu":
    print("Here's our menu:")
    print("- Pizza")
    print("- Burger")
    print("- Salad")
    print("- Pasta")

food = input("What would you like to order? ")
print("Great choice! One " + food + " coming right up.")
print("Thanks for ordering, " + name + "!")
