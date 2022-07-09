import random


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_script():
    value = (random.randint(1, 100))
    k = 0
    for i in range(2, (value // 2 + 1)):
        if (value % i == 0):
            k += 1
    if (k <= 0):
        answer = 'yes'
    else:
        answer = 'no'
    return answer, value
