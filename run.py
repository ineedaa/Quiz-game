""" This variable consists of dictionary of 8 questions in a list."""

QUESTIONS = [{'question': 'What is the capital of France?',
              'option1': 'Paris', 'option2': 'Berlin', 'option3': 'Madrid',
              'correctanswer': '1'},
             {'question': 'What is the largest ocean in the world?',
              'option1': 'Atlantic Ocean', 'option2': 'Pacific Ocean',
              'option3': 'Indian Ocean', 'correctanswer': '2'},
             {'question': 'What is the capital of Australia?',
              'option1': 'Sydney',
              'option2': 'Canberra',
              'option3': 'Melbourne',
              'correctanswer': '2'},
             {'question': 'What is the currency of Japan?',
              'option1': 'Dollar',
              'option2': 'Pound',
              'option3': 'Yen',
              'correctanswer': '3'},
             {'question': 'What is the tallest mountain in the world?',
              'option1': 'K2',
              'option2': 'Mount Everest',
              'option3': 'Lhotse',
              'correctanswer': '2'},
             {'question': 'What is the most populous city in the world?',
              'option1': 'Beijing',
              'option2': 'Istanbul',
              'option3': 'Mumbai',
              'correctanswer': '1'},
             {'question': 'What is the largest planet in the solar system?',
              'option1': 'Earth',
              'option2': 'Mars',
              'option3': 'Jupiter',
              'correctanswer': '3'},
             {'question': 'What theory explains the origin of universe?',
              'option1': 'Evolution',
              'option2': 'General Relativity',
              'option3': 'Big Bang Theory',
              'correctanswer': '3'}]


def display_quiz():
    """
    Displays the question and options on the page
    """
    # Print the question
    for question in QUESTIONS:
        print(question['question'])
        # Print the options
        for key, value in question.items():
            if key.startswith('option'):
                print(f"{key[6:]}: {value}")
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
        

print("Welcome to the Quiz Game")
print("Choose the right answer from the options given")
print("Please enter your answer as 1 ,2 or 3")
display_quiz()
