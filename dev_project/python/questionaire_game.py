# Set a list of 5 questions using a dictionary
# Questions should be sent randomly
# User should be able to input an answer and receive a response back (correct or incorrect)
# If user is able to answer all answers correct, then get a nice message, otherwise to try again

import random

questions = {
    "What is 10 x 20?": 200,
    "Are you playing a game now?": "yes",
    "What color is a stop sign?": "red",
    "Where is the Eiffel Tower?": "paris",
    "What is 2 + 2?": 4
}

def ask_questions():
    correct_answers = 0
    for question in random.sample(list(questions.keys()), len(questions)):
        answer = input(question + " ")
        if answer.lower() == str(questions[question]).lower():
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")

    if correct_answers == len(questions):
        print("You got all the questions correct!")
    else:
        print("You got " + str(correct_answers) + " out of " + str(len(questions)) + " correct. Try again!")

ask_questions() 
