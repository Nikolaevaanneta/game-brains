from platform import java_ver
import prompt

def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game.assignment())
    
    level = 3
    for _ in range(0, level):
        answer, question = game.get_answer_and_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')

