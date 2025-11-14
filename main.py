def welcome_message():
    print("Hello, welcome to the Food Ordering Chatbot!")

def get_user_info():
    name = input("What is your name? ")
    age = input("Hello " + name + ", how old are you? ")
    mood = input("How are you feeling today? ").lower()
    return name, age, mood

def respond_to_mood(mood):
    if "good" in mood or "great" in mood or "happy" in mood:
        print("I'm glad you're feeling good!")
    elif "bad" in mood or "sad" in mood or "tired" in mood:
        print("I'm sorry you feel like that. Maybe some comfort food will help.")
    elif "angry" in mood or "upset" in mood:
        print("I understand. Ordering food might help you feel better.")
    elif "fine" in mood or "okay" in mood:
        print("Got it. Let's make today better.")
    else:
        print("Thanks for sharing how you're feeling.")

def show_menu():
    print("\nWhat would you like to do?")
    print("1. View full menu")
    print("2. Order food")
    print("3. Check order total")
    print("4. Ask the chatbot a question")
    print("5. Describe your mood again")
    print("6. Exit")

food_menu = {
    "pizza": 12,
    "burger": 10,
    "salad": 8,
    "pasta": 11,
    "fries": 5,
    "soda": 3,
    "ice cream": 6
}

def view_full_menu():
    print("\nMenu:")
    for item, price in food_menu.items():
        print(item.title() + " - $" + str(price))

def order_food(order):
    while True:
        item = input("What would you like to order? ").lower()
        if item in food_menu:
            order.append(food_menu[item])
            print("Added " + item + " to your order.")
        else:
            print("We don't have that.")
        again = input("Order something else? (yes/no) ").lower()
        if again != "yes":
            break

def check_total(order):
    if len(order) == 0:
        print("You haven't ordered anything yet.")
    else:
        print("Your total is $" + str(sum(order)))

def ask_question():
    q = input("Ask me anything: ").lower()
    if "hours" in q:
        print("We are open 24/7.")
    elif "recommend" in q:
        print("I recommend pizza or ice cream depending on your mood.")
    elif "hello" in q:
        print("Hello!")
    elif "help" in q:
        print("You can view the menu, order food, or check your total.")
    elif "love" in q:
        print("Love is important. Order some comfort food.")
    else:
        print("I'm not sure how to answer that.")

def chatbot():
    welcome_message()
    name, age, mood = get_user_info()
    respond_to_mood(mood)
    order = []
    running = True
    while running:
        show_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            view_full_menu()
        elif choice == "2":
            order_food(order)
        elif choice == "3":
            check_total(order)
        elif choice == "4":
            ask_question()
        elif choice == "5":
            new_mood = input("How are you feeling now? ").lower()
            respond_to_mood(new_mood)
        elif choice == "6":
            print("Goodbye " + name + "!")
            running = False
        else:
            print("Invalid choice.")


