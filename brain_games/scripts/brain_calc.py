import random
import operator
import prompt

ops = {'+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv}


def calc():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    i = 0
    print('What is the result of the expression?')
    while i < 3:
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)  
        op = random.choice(list(ops.keys()))
        answer = str(ops.get(op)(num1,num2))
        print("Question: {} {} {}?".format(num1, op, num2))
        guess = prompt.string('Your answer: ')
        if answer == guess:
            print ("Correct!")
            i += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(guess,answer))


   



            
