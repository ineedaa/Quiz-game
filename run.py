""" This variable consists of dictionary of 8 questions in a list."""

QUESTIONS = [{'question': 'Q1:What is the capital of France?',
              'option1': 'Paris', 'option2': 'Berlin', 'option3': 'Madrid',
              'correctanswer': '1'},
             {'question': 'Q2:What is the largest ocean in the world?',
              'option1': 'Atlantic Ocean', 'option2': 'Pacific Ocean',
              'option3': 'Indian Ocean', 'correctanswer': '2'},
             {'question': 'Q3:What is the capital of Australia?',
              'option1': 'Sydney',
              'option2': 'Canberra',
              'option3': 'Melbourne',
              'correctanswer': '2'},
             {'question': 'Q4:What is the currency of Japan?',
              'option1': 'Dollar',
              'option2': 'Pound',
              'option3': 'Yen',
              'correctanswer': '3'},
             {'question': 'Q5:What is the tallest mountain in the world?',
              'option1': 'K2',
              'option2': 'Mount Everest',
              'option3': 'Lhotse',
              'correctanswer': '2'},
             {'question': 'Q6:What is the most populous city in the world?',
              'option1': 'Beijing',
              'option2': 'Istanbul',
              'option3': 'Mumbai',
              'correctanswer': '1'},
             {'question': 'Q7:What is the largest planet in the solar system?',
              'option1': 'Earth',
              'option2': 'Mars',
              'option3': 'Jupiter',
              'correctanswer': '3'},
             {'question': 'Q8:What theory explains the origin of universe?',
              'option1': 'Evolution',
              'option2': 'General Relativity',
              'option3': 'Big Bang Theory',
              'correctanswer': '3'}]

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
    get_user_answer()


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
    check_user_answer(data_str)


def check_user_answer(data_str):
    """ Checks the user answer whether its correct or incorrect """
    answer = [d['correctanswer'] for d in QUESTIONS]
    global question_index
    if data_str == int(answer[question_index]):
        global score
        score += 1
        print("\nWell done !!Correct Answer!!")
        print(f"You scored {score}/8 questions!")
        print("-------------------------------------------------------\n")
    else:
        print("\nOops!!Incorrect Answer!!!")
        print(f"The answer is option no:{int(answer[question_index])}")
        print("-------------------------------------------------------\n")
    question_index += 1
    if question_index == (len(QUESTIONS) - 1):
        display_final_result()
    else:
        display_quiz()


def display_final_result():
    """ Displays the final result at the end of the Game"""
    if score == 8:
        print(f"Congragulations!!! \n Your final score is {score}/ 8.!!!\n")
    else:
        print(f"Your scored {score}/8 questions\nBetter Luck Next Time!!!\n")


print("\n")
print("-----------------------------------------------")
print("Welcome to the Quiz Game!!!")
print("Choose the right answer from the options given")
print("Please enter your answer as either 1 ,2 or 3")
print("Press 'Enter' after you entered your options")
print("------------------------------------------------\n")


display_quiz()
