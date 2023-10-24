import random
import json
import fontstyle
from dashboard_pkg.intro import show_intro, show_difficulty
from dashboard_pkg.play import get_difficulty, play_game

# Load trivia questions from the JSON data
with open('./data/trivia_questions.json', 'r') as file:
    trivia_data = json.load(file)

stats = []
user = ""

difficulty_db = {
    "1": "easy",
    "2": "medium",
    "3": "hard",
}
level = ""

while True:
    show_intro()

    invalid_msg = fontstyle.apply("Please select a valid option.", 'bold/red')
    difficulty_msg = fontstyle.apply("\nPlease select a level of difficulty: ", 'bold/green')
    menu_prompt = fontstyle.apply("Please select an option from the menu: ", 'bold/green')
    name_prompt = fontstyle.apply("\nHi! What's your name? ", 'bold/green')
    num_questions_msg = fontstyle.apply("\nEnter the number of questions you want to answer: ", 'bold/green')
    num_questions_invalid_msg = fontstyle.apply("Sorry, the number of questions must be between 1 and 30.", 'bold/red')
    blank_name_msg = fontstyle.apply("\nPlease enter a valid name.", 'bold/red')
    only_letters_msg = fontstyle.apply("\nPlease enter a only letters.", 'bold/red')
    
    exit_msg = fontstyle.apply("\nEnding the game. Goodbye! 👋\n", 'bold/green')

    if user == "":
        print(fontstyle.apply("\nGame has not started yet.", 'bold/yellow'))
    else:
        print(f"Hi {user}!👋")

    # User input
    option = input(menu_prompt)


    if option == "1":
        
        username = input(name_prompt)
        

        if username == "":
            print(blank_name_msg)
        elif username.isalpha() == False:
            print(only_letters_msg)
        else:
            while True:
                show_difficulty()
                difficulty_option = input(difficulty_msg)

                if difficulty_option in ["1", "2", "3"]:
                    level = get_difficulty(difficulty_db, username, difficulty_option)

                    while True:
                        try:
                            num_questions = int(input(num_questions_msg))
                            if 1 <= num_questions <= 30:
                                play_game(username, level, trivia_data[level], num_questions)
                                break
                            else:
                                print(num_questions_invalid_msg)
                        except ValueError:
                            print(num_questions_invalid_msg)

                    break  # Exit from difficulty selection loop
                elif difficulty_option == "4":
                    break  # Exit to main menu
                else:
                    print(invalid_msg)

    elif option == "2":
        print(exit_msg)
        break

    else:
        print(invalid_msg)
