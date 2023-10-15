import random
from dashboard_pkg.intro import show_intro, show_difficulty

# Global variables to keep track of answered questions and correct answers
answered_questions = []
correct_answer_count = 0

def get_difficulty(difficulty_db, username, difficulty_option):
    if difficulty_option in difficulty_db:
        print(f"\n{username.title()}, you have selected a/an {difficulty_db[difficulty_option]} game. NICE!")    
        return difficulty_db[difficulty_option]
    else:
        print("Please select a valid option.")
        return ""
    
def start_game(username, level, trivia_data, num_questions):
    global answered_questions
    global correct_answer_count

    print(f"\n{username}, starting a/an {level} game with {num_questions} questions...")

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
        print(f"\nQuestion {i + 1}/{num_questions}:")
        print(question)
        for j in range(len(answer_options)):
            print(f"{chr(65 + j)}. {answer_options[j]}")

        # Get the player's answer
        user_answer = input("Your Answer (A, B, C, D): ").strip().upper()

        # Check if the answer is correct
        if user_answer in ['A', 'B', 'C', 'D']:
            user_answer_index = ord(user_answer) - ord('A')
            if answer_options[user_answer_index] == correct_answer:
                print("Correct!")
                correct_answer_count += 1
            else:
                print("My Selection: ", user_answer)
                print(f"Sorry, the correct answer is {correct_answer}.")
        else:
            print("Invalid input. Please enter A, B, C, or D.")

        # Record the answered question
        answered_questions.append(question)

    # Display the player's score at the end
    print(f"\n{username.title()}, your final score: {correct_answer_count}/{num_questions}")

    # Return to show_intro display
    # show_intro()



def get_questions(username, level, trivia_questions):
    global answered_questions
    global correct_answer_count

    print(f"\n{username}, starting a/an {level} game...")

    # Print the answered questions and the number of correct answers
    print("\nAnswered Questions:")
    for i, question in enumerate(answered_questions, start=1):
        print(f"{i}. {question}")

    print(f"\n{username}, your number of correct answers: {correct_answer_count}/{len(answered_questions)}")

def get_stats(username, level, num_questions):
    global correct_answer_count

    print(f"\n{username}, here are your statistics for the {level} game:")

    # Calculate the percentage of correct answers
    percentage_correct = (correct_answer_count / num_questions) * 100
    print(f"Number of questions: {len(answered_questions)}")
    print(f"Percentage of correct: {percentage_correct:.2f}%")
    
    

# Add the get_stats function here



# Reset global variables when the program starts
answered_questions = []
correct_answer_count = 0
