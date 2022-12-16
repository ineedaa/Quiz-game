# Quiz Game

Quiz game is a Python terminal game that runs in the Code Institute mock terminal on Heroku.

Users can play this game on any device.Each game has eight general knowledge questions.

![website in different screens](docs/responsive.png)



## User Stories

- As a visiting user,I would like to play the quiz game.
- I would like to enter my name which only includes less than 8 characters.
- There are total 8 questions that  I needs to be answered.
- After choosing among the three options of answer provided,I  can choose the right option number.
- By pressing  the Enter key,I will know whether the answer is right or wrong.
- As a visiting user,I am aware that I can only enter either 1,2,or 3.All the other entries will return as error.
- By finishing the eight questions ,I  get the final score of the game.


## Features

### Existing Features

#### Start Page
- The page displays the welcome message and asks the user to enter the name.
  ![startpage](docs/runprogram.png)

- The user should enter the name only in alphabets less than eight characters.
- If the user enters their name with more than 8 characters or in numerics, it displays an error message.  
  ![errormessage](docs/errorname.png)

#### Quiz 
- After the user enters the name, the instructions are displayed before starting the game.
- The quiz contains a set of one question, and three options shown at a time.
  ![displayquestion](docs/displayquestions.png)

- The user can pick either 1 ,2 ,3 option and press Enter.
- If the user enters anything other than the three options, user gets an error message.
  ![displayerror](docs/answervalidation.png)]


#### Score Area
- If the user enters the correct answer, user gets a correct answer response immediately.
 ![correctanswer](docs/correctanswer.png)

- If the user enters a wrong answer, the user gets the incorrect answer message.
  ![incorrectanswer](docs/wronganswer.png)

- The questions have numbers that counts the questions out of 8. This is useful for the user to know which question they are on and how many are left.

#### Final Result
- when the user finishes the eight questions ,the user is given the game's total score.
- If the user scores all the correct answers, user gets a positive message.
  ![winresultmessage](docs/winquiz.png) 

- If the user fails to get even one answer wrong, user gets the game's total score.
  ![failedmessage](docs/wronganswer.png)

## Features Left to Implement

- In the future,this website may add more features , such as a timer, and a previous key option, when the user wants to go back to the previous question.  

## Color scheme

- The colors used in this project by adding an external library [colorit](https://pypi.org/project/color-it/).
- In the terminal, 'pip install color-it' was entered and installed the library.
- Red color(Colors.red) is given for validation errors and for incorrect answer messages.
- Green color(Colors.green) is given to correct answers.
- Yellow color(Colors.yellow) is given for win message and orange for a fail message.

## Technology
The technology used in this website is :
  - **Python** language used for creating the game.
  - **Gitpod**  as a workspace.
  - **GitHub**  for version control of the game.
  - **Code institute python essentials template*** for creating the project.
  - **Heroku** for deploying the project.
  - [colorit](https://pypi.org/project/color-it/).
  - For coloring the main headings and message alerts, colorit library is used.
  - [re](https://docs.python.org/3/library/re.html).
  - The functions in this module let you check if a particular string matches a given regular expression. Used for validating the input user name. 

## Tools

* [Am I Responsive](https://ui.dev/amiresponsive)
* [GitPod](https://www.gitpod.io/)
* [GitHub](https://github.com/)
* [Lucidchart](https://www.lucidchart.com/pages)

## Testing

### Quiz Page
 
 - When user runs the program, the user receives the home page.
   
   ![home page](docs/runprogram.png)

 - User can enter their name . If more than 8 characters or no name entered or any numeric characters entered, user gets an error message.

    ![errormessage](docs/errorname.png)

 -  User gets the question displayed and can either 1, 2, or 3.If the  user enters anything other than these options, user gets an error message.

    ![displayerror](docs/answervalidation.png)]
    
 -  If the user enters the correct answer,user gets a positive message saying the answer is correct.  
    ![correct answer](docs/correctanswer.png)

 - Also user gets an incorrect answer message if the answer is incorrect.
   
   ![incorrectanswer](docs/wronganswer.png)
 
 - After finishing the eight questions, the user gets the final result.If all the answers are correct, the user gets this message.
   
   ![winresultmessage](docs/winquiz.png)
 - If one of the answers is wrong, the user gets this message.
    
    ![failedmessage](docs/wronganswer.png)
 
### Validator Testing
 -  PEP8
      - No errors were returned from PEP8online.com.

### Fixed Bugs
   - Noted the user name input validation error,when the user is not entering a name or entering numeric characters,its accepted by the system.To fix this error ,a user validation function is created.

### Supported Browsers
  - Compatible to Google Chrome.
  - Used chrome stimulator for testing mobile screens.

## Deployment
-  This project was deployed using Code Institute's mock terminal for Heroku.

### Heroku
-  Fork or clone this repository in Github.
-  Createa new Heroku App.
-  Set the buildbacks to Python and NodeJs in that order.
-  Link the Heroku app to the repository.
-  Click on Deploy.
### Gitpod 
- In GitHub repository,click on the Gitpod icon on the right hand side .
- Within the Gitpod,open the run.py file
- In terminal,write 'python3 run.py' command.
- The terminal runs the program.

## Credits

  - The content  was taken from [Google](https://www.google.com/quiz/).
  - Code Institute for the deployment Terminal.
  - Fixing my code issues by using [stackoverflow](https://stackoverflow.com/)
  - Fixed bugs with support of my mentor Rohit Sharma.
  