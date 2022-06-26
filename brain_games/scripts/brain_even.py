import random, prompt


def even():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    i = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while i < 3:
        value = (random.randint(0, 100))
        print("Question: {}".format(value))
        answer = prompt.string('Your answer: ')
        if answer == 'yes' and value % 2 == 0:
            print ("Correct!")
            i += 1
        elif answer == 'no' and value % 2 != 0:
            print ("Correct!")
            i += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {}!".format(name))
    print("Congratulations, {}!".format(name))
            
