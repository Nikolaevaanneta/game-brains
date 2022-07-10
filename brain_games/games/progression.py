import random

def assignment():
    return 'What number is missing in the progression?'

def get_answer_and_question():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = 10

    progression = list(range(start, (start + length * step), step))

    hidden_index = random.randrange(0, length)
    answer, progression[hidden_index] = progression[hidden_index], '..'
    question = ' '.join(map(str, progression))

    return str(answer), question
