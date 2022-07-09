import random


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_script():
    value = (random.randint(0, 10))
    answer = "yes" if value % 2 == 0 else 'no'
    return answer, value
