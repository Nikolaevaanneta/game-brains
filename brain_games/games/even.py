
import prompt
import random

def assignment():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
    
def get_answer_and_question():   
        question = random.randrange(1, 100)
        answer = 'yes' if question % 2 == 0 else 'no'
        return str(answer), question
