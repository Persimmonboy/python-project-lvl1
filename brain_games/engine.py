import prompt


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
        answer, value = game_name.game_script()
        print("Question: {}".format(value))
        user_answer = prompt.string('Your answer: ')
        if answer == user_answer:
            print("Correct!")
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print("Congratulations, {}!".format(name))
