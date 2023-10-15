from dashboard_pkg.intro import show_intro


trivia_questions = {}
stats = []
user = ""
#game mode is short - best of 5 questions, medium-best of 7 questions, or long - best of 9 questions
# dificult is easy, medium, or hard

show_intro()

if user == "":
    print("Game has not started yet.")
else:
    print(f"Hi {user}!👋")


# User input
option = input("Please select an option from the menu: ")

if option == "1":
    print("TODO: Write instructions")

elif option == "2":
    print("TODO: Play game")

elif option == "3":
    print("TODO: Show stats")

elif option == "4":
    print("\nEnding the game. Goodbye! 👋\n")