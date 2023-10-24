import random
import fontstyle
from dashboard_pkg.intro import show_intro, show_difficulty

# Global variables to keep track of answered questions and correct answers
answered_questions = []
correct_answer_count = 0

def get_difficulty(difficulty_db, username, difficulty_option):
    if difficulty_option in difficulty_db: 
        return difficulty_db[difficulty_option]
    else:
        print("\nPlease select a valid option.")
        return ""
    
def play_game(username, level, trivia_data, num_questions):
    global answered_questions
    global correct_answer_count

    user_game_msg = fontstyle.apply(f"\n{username}, starting a/an {level} game with {num_questions} questions...", 'bold/green')
    correct = fontstyle.apply("Correct!", 'bold/green')
    invalid_answer = fontstyle.apply("Invalid input. You lose a question. Next time enter A, B, C, or D", 'bold/red')

    print(user_game_msg)

    # Iterate through trivia questions, limited to num_questions
    for i in range(num_questions):
        question_data = random.choice(trivia_data)
        trivia_data.remove(question_data)  # Remove the selected question

        question = question_data['question']
        correct_answer = question_data['correct_answer']
        incorrect_answers = question_data['incorrect_answers']

        # Combine correct and incorrect answers
        answer_options = [correct_answer] + incorrect_answers
        random.shuffle(answer_options)

        # Present the question and answer options
        print(fontstyle.apply(f"\nQuestion {i + 1}/{num_questions}:", 'bold/cyan'))
        print(fontstyle.apply(question, 'bold/yellow'))
        for j in range(len(answer_options)):
            print(fontstyle.apply(f"{chr(65 + j)}. {answer_options[j]}", 'bold/yellow'))

        # Get the player's answer
        user_answer = input("\nYour Answer (A, B, C, D): ").strip().upper()

        # Check if the answer is correct
        if user_answer in ['A', 'B', 'C', 'D']:
            user_answer_index = ord(user_answer) - ord('A')
            if answer_options[user_answer_index] == correct_answer:
                print(correct)
                correct_answer_count += 1
            else:
                print(fontstyle.apply(f"Sorry, the correct answer is {correct_answer}.", 'bold/red'))
        else:
            print(invalid_answer)

        # Record the answered question
        answered_questions.append(question)
        percentage_right = round((correct_answer_count / num_questions) * 100, 2)
        
    # Display the player's score at the end
    print(fontstyle.apply(f"\nYou got {correct_answer_count} correct out of {num_questions}", 'bold/green'))
    print(fontstyle.apply(f"{username.title()}, your final score: {percentage_right}%", 'bold/green'))


def get_questions(username, level):
    global answered_questions
    global correct_answer_count

    print(f"\n{username}, starting a/an {level} game...")

    # Print the answered questions and the number of correct answers
    print("\nAnswered Questions:")
    for i, question in enumerate(answered_questions, start=1):
        print(f"{i}. {question}")

    print(f"\n{username}, your number of correct answers: {correct_answer_count}/{len(answered_questions)}")




# Reset global variables when the program starts
answered_questions = []
correct_answer_count = 0