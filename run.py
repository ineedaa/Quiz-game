from questions import QUESTIONS

score = 0
question_index = 0


def display_quiz():
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
            if 1 <= data_str <= 3:
                break
            else:
                print("Please enter a valid option number.")
        except ValueError:
            print("Please enter a valid option number.")
    return data_str


def check_user_answer(data_str):
    """ Checks the user answer whether its correct or incorrect """
    answer = [d['correctanswer'] for d in QUESTIONS]
    if data_str == int(answer[question_index]):
        print("\nWell done !!Correct Answer!!")
        print(f"You scored {score}/8 questions!")
        print("-------------------------------------------------------\n")
        return True
    else:
        print("\nOops!!Incorrect Answer!!!")
        print(f"The answer is option no:{int(answer[question_index])}")
        print("-------------------------------------------------------\n")
        return False


def display_final_result():
    """ Displays the final result at the end of the Game"""
    if score == 8:
        print(f"Congragulations {name.upper()}!!! \nYou scored {score}/8\n")
    else:
        print(f"{name.upper()} Your total score = {score}/8\n \
                Better Luck Next Time!\n")



    print("\n")
    print("-----------------------------------------------")
    print("Welcome to the Quiz Game!!!")
    name = input('Please enter your name:  ')
    print(f"\nHi {name.upper()}!,welcome to the quiz game!\n")
    print("Choose the right answer from the options given")
    print("Please enter your answer as either 1 ,2 or 3")
    print("Press 'Enter' after you entered your options")
    print("------------------------------------------------\n")


def play_quiz():
    question_index = 0
    score = 0
    while question_index < (len(QUESTIONS)):
        
        display_quiz(question_index)
        get_user_answer(question_index)
        user_answer = get_user_answer(question_index)
        check_response = check_user_answer(data_str,question_index)
        if check_response:
            score += 1
        question_index += 1
    display_final_result(question_index)
        


    
    
