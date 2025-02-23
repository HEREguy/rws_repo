
import random

# this game should ask the user 6 questions randomly
# responses should be lowered case when inputted
# after responding to all questions, the user will get a result letting them know how many questions they responded correctly


questions = {
    "What color is the sky in the daytime?": "blue",
    "What is 4 x 5 x 5?": 100,
    "What is the first name of the founder of Amazon?": "jeff",
    "Who is the main character for Disney?": "mickey mouse",
    "What is 12 x 12?": 144,
    "What color is a yield sign": "yellow"
}

def questionnaire():
    correct_answers = 0
    for question in random.sample(list(questions.keys()), len(questions)):
        answer = input(question + " ")
        if answer.lower() == str(questions[question]).lower():
            print("You Got It!")
            correct_answers += 1
        else:
            print("Unfortunately, that's incorrect...")

    if correct_answers == len(questions):
        print("Great, you got all the questions right!!")
    else:
        print("You got " + str(correct_answers) + " out of " + str(len(questions)) + " correct. Please try again!")

questionnaire()
