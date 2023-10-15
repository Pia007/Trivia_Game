import random
import json
from dashboard_pkg.intro import show_intro, show_difficulty
from dashboard_pkg.play import get_difficulty, start_game, get_stats

# Load trivia questions from the JSON data
with open('trivia_questions.json', 'r') as file:
    trivia_data = json.load(file)

# ...

stats = []
user = ""

difficulty_db = {
    "1": "easy",
    "2": "average",
    "3": "hard",
}
level = ""

while True:
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
        username = input("Hi! What's your name? ")

        if username == "":
            print("Please enter a valid name.")
        else:
            while True:
                # user = username
                show_difficulty()
                # try:
                difficulty_option = input("Please select a level of difficulty: ")
                num_questions = int(input("Enter the number of questions you want to answer: "))
                
                try: 
                    if difficulty_option == "1":
                        level = get_difficulty(difficulty_db, username, difficulty_option)
                        start_game(username, level, trivia_data[level], num_questions)  # Pass questions for the selected level
                        break
                    elif difficulty_option == "2":
                        level = get_difficulty(difficulty_db, username, difficulty_option)
                        start_game(username, level, trivia_data[level], num_questions)  # Pass questions for the selected level
                        break
                    elif difficulty_option == "3":
                        level = get_difficulty(difficulty_db, username, difficulty_option)
                        start_game(username, level, trivia_data[level], num_questions)  # Pass questions for the selected level
                        break
                    elif difficulty_option == "4":
                        break
                    else:
                        print("Please select a valid option.")
                except:
                    print("Please select a valid option.")
            
    elif option == "3":
        get_stats(username, level, num_questions=5)

    elif option == "4":
        print("\nEnding the game. Goodbye! 👋\n")
        break
    else:
        print("Please select a valid option.")