""" A regular expression (or RE) ,the functions in this module let you check
    if a particular string matches a given regular expression ."""
import re
from colorit import Colors, color
from questions import QUESTIONS


def display_quiz(question_index):
    """
    Displays the question and options on the page by geting the value of
    question_index parameter
    """
    question = QUESTIONS[question_index]
    print(question['question'])
    for key, value in question.items():
        if key.startswith('option'):
            print(f"{key[6:]}.{value}")
    print("\n")


def get_user_answer():
    """ Get user answer from the options and validate if the answer is right
 and returns the user answer."""
    while True:
        try:
            data_str = int(input("Enter the correct option number: \n"))
            # Validate the user answer
            if 1 <= data_str <= 3:
                break
            print(color("Please enter a valid option number.", Colors.red))
        except ValueError:
            print(color("Please enter a valid option number.", Colors.red))
    return data_str


def check_user_answer(user_answer, question_index):
    """ Checks the user answer whether its correct or incorrect by taking the
    parameters user_answer and question_index and returns True or False"""
    answer = [d['correctanswer'] for d in QUESTIONS]
    if user_answer == int(answer[question_index]):
        print(color("\nWell done !!Correct Answer!!", Colors.green))
        print("-------------------------------------------------------\n")
        return True
    print(color("\nOops!!Incorrect Answer!!!", Colors.red))
    print(f"The answer is option no:{int(answer[question_index])}")
    print("-------------------------------------------------------\n")
    return False


def display_final_result(name, score):
    """ Displays the final result at the end of the Game by taking parameters
     name and score"""
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
        name = input("Please enter your name: \n")
        if len(name) >= 8:
            print(color("Error: Name must be 2 to 8 characters.", Colors.red))
        elif not re.match("^[a-zA-Z]*$", name):
            print(color("Error: Name must contain only letters.", Colors.red))
        elif not name:
            print(color("Error: Name cannot be blank.", Colors.red))
        else:
            break
    print(color(f"\nHi {name.upper()},Welcome to the Quiz Game!", Colors.blue))
    return name


def display_instructions():
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
    display_instructions()
    # Loops through the questions.
    while question_index < (len(QUESTIONS)):
        display_quiz(question_index)
        user_answer = get_user_answer()
        check_response = check_user_answer(user_answer, question_index)
        if check_response:
            score += 1
        question_index += 1
    # if completed all the questions,print the final result.
    display_final_result(name, score)


if __name__ == '__main__':
    # Executes all the code in play_quiz function.
    play_quiz()
