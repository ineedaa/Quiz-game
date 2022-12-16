""" A regular expression (or RE) ,the functions in this module let you check
    if a particular string matches a given regular expression ."""
import re
from colorit import Colors, color
from questions import QUESTIONS


def display_quiz(question_index):
    """
    Displays the question and options on the page
    """
    # Print the question
    question = QUESTIONS[question_index]
    print(question['question'])
    # Print the options
    for key, value in question.items():
        if key.startswith('option'):
            print(f"{key[6:]}.{value}")
    print("\n")


def get_user_answer():
    """ Get user answer from the options and validate if the answer is right"""
    while True:
        try:
            data_str = int(input("Enter the correct option number: "))
            # Validate the user answer
            if 1 <= data_str <= 3:
                break
            else:
                print(color("Please enter a valid option number.", Colors.red))
        # Print the error message if user input is not valid.
        except ValueError:
            print(color("Please enter a valid option number.", Colors.red))
    return data_str


def check_user_answer(user_answer, question_index):
    """ Checks the user answer whether its correct or incorrect """
    answer = [d['correctanswer'] for d in QUESTIONS]
    # Returns True if user answer is correct.
    if user_answer == int(answer[question_index]):
        print(color("\nWell done !!Correct Answer!!", Colors.green))
        print("-------------------------------------------------------\n")
        return True
    else:
        print(color("\nOops!!Incorrect Answer!!!", Colors.red))
        print(f"The answer is option no:{int(answer[question_index])}")
        print("-------------------------------------------------------\n")
        return False


def display_final_result(name, score):
    """ Displays the final result at the end of the Game"""
    # Check if user scored 8/8.
    if score == 8:
        print(color(f"Congratulations {name.upper()}!!! \n\
You scored {score}/8\n", Colors.yellow))
    else:
        print(color(f"{name.upper()} Your total score = {score}/8\n\
Better Luck Next Time!\n", Colors.orange))


def get_user_name():
    """ Get the user name after validating the input from user,should not
    contain numbers,or characters more than 8 """
    while True:
        print("\n")
        print("-----------------------------------------------")
        print("Welcome to the Quiz Game!!!\n")
        name = input("Please enter your name: ")
        # Check the length of the name
        if len(name) > 8:
            print("Error: Name must be 8 characters or less.")
        # Check that the name contains only letters
        elif not re.match("^[a-zA-Z]*$", name):
            print("Error: Name must contain only letters.")
        # Check that the name is not blank
        elif not name:
            print("Error: Name cannot be blank.")
        else:
            break
    print(color(f"\nHi {name.upper()},Welcome to the Quiz Game!", Colors.blue))
    return name


def game_instructions():
    """ Displays the game instructions at the start of the game """
    print("Choose the right answer from the options given")
    print("Please enter your answer as either 1 ,2 or 3")
    print("Press 'Enter' after you entered your options")
    print("------------------------------------------------\n")


def play_quiz():
    """ The main function which has the flow of this game,includes all the
        functions in order to continue the game."""
    question_index = 0
    score = 0
    name = get_user_name()
    game_instructions()
    # Loops through the functions till its less than len of QUESTIONS.
    while question_index < (len(QUESTIONS)):
        display_quiz(question_index)
        user_answer = get_user_answer()
        check_response = check_user_answer(user_answer, question_index)
        # Increment score by 1,if returns true.
        if check_response:
            score += 1
        # Increments the question index by 1.
        question_index += 1
    # if completes the full questions,print the final result.
    display_final_result(name, score)


if __name__ == '__main__':
    # Executes all the code in play_quiz function.
    play_quiz()
