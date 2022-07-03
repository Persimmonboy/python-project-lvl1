import prompt
import random

def welcome():
    print("Welcome to the Brain Games!")

def get_user_name():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name

def run_engine(game_name):
    i = 0
    welcome()
    name = get_user_name()
    print(game_name.TASK)
    while i < 3:
        answer, question = game_name.game_script()
        print("Question: {}".format(question))
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print ("Correct!")
            i += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {}!".format(name))
    print("Congratulations, {}!".format(name))





