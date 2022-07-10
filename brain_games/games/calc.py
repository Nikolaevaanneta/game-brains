import random
import operator

def assignment():
    return 'What is the result of the expression?'
    
def get_answer_and_question():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        }
    x = random.randrange(1, 10)
    y = random.randrange(1, 10)

    operation = random.choice(list(operations.keys()))
    question = f'{x} {operation} {y}'
    answer = str(operations[operation](x, y))
    return  str(answer) , question
