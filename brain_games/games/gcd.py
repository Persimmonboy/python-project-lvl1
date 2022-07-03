import math
import random

TASK = 'Find the greatest common divisor of given numbers.'

def game_script():
    num1 = random.randint(0,10)
    num2 = random.randint(0,10) 
    value = ("{} {}".format(num1, num2))
    answer = str((math.gcd (num1, num2)))
    return answer, value