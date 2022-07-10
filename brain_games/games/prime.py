from operator import truediv
import random

def assignment():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'

def get_answer_and_question():
    question = random.randrange(1, 50)
    answer = 'no' if num_prime(question) else 'yes'
    return answer, question

def num_prime(num):
    x = 2
    while x < num:
        if num % x == 0:
            return False
        x += 1
    return True
        