import random


TASK = 'What number is missing in the progression?'


def game_script():
    value = []
    progression_range = random.randint(5, 10)
    progression_step = random.randint(1, 5)
    item = (random.randint(0, 10))
    for i in range(1, progression_range + 1):
        item = item + progression_step
        value.append(item)
    random_index = random.randint(0, len(value) - 1)
    answer = str(value[random_index])
    value[random_index] = '..'
    return answer, (' '.join(map(str, value)))
