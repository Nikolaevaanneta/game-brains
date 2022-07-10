import random

def assignment():
    return 'Find the greatest common divisor of given numbers.'
    
def get_answer_and_question():   
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)
    question = f'{x} {y}'
    answer = get_gcd(x, y)

    return str(answer), question

def get_gcd(x, y):
    if not y:
        return x
    return get_gcd(y, x%y)
    
  
