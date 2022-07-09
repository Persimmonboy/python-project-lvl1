import random
import operator


ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '//': operator.floordiv}


TASK = 'What is the result of the expression?'


def game_script():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op = random.choice(list(ops.keys()))
    answer = str(ops.get(op)(num1, num2))
    value = ("{} {} {}?".format(num1, op, num2))
    return answer, value
