def welcome_message():
    print("Hello, welcome to the Food Ordering Chatbot!")

def get_user_info():
    name = input("What is your name? ")
    age = input("Hello " + name + ", how old are you? ")
    return name, age

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Check the food menu")
    print("2. Place an order")
    print("3. Ask for help")
    print("4. Exit")

def handle_menu_choice(choice, name):
    if choice == "1":
        print("\nHere's our menu:")
        print("- Pizza")
        print("- Burger")
        print("- Salad")
        print("- Pasta")
    elif choice == "2":
        food = input("What would you like to order? ")
        print("Great choice! One " + food + " coming right up.")
    elif choice == "3":
        print("I'm here to help! You can check the menu or place an order.")
    elif choice == "4":
        print("Goodbye, " + name + "! Thanks for visiting.")
        return False
    else:
        print("Invalid option. Please choose again.")
    return True

def chatbot():
    welcome_message()
    name, age = get_user_info()
    running = True
    while running:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        running = handle_menu_choice(choice, name)

chatbot()