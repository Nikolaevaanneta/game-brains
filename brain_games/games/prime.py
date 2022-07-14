from operator import truediv
import random

def assignment():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'

def get_answer_and_question():
    question = random.randrange(1, 50)
    answer = 'yes' if num_prime(question) else 'no'
    return answer, question

def num_prime(num):
    if num == 1:
        return True
    x = 2
    while x < num:
        if num % x == 0:
            return False
        x += 1
    return True
        