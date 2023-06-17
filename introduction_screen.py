# Welcome Text

from termcolor import colored
from pyfiglet import Figlet


def welcome_text():
    print(70*'#')
    f = Figlet(font="standard")
    print(colored(f.renderText('WELCOME TO SNAKE'), 'green'))
    print(70*'#')

    # Rules
    f = Figlet(font="contessa")
    print(colored(f.renderText("RULES"), 'red'))
    print("""> You are a snake.Eat your prey and get as big as you can.
> Use arrow keys (up, down, left, right) to navigate.
> Do not eat yourself. Do not hit the wall.
""")
    print(70*'#')


def game_over_text(score, old_high_score):
    print(70*'#')
    f = Figlet(font="standard")
    print(colored(f.renderText('GAME OVER'), 'green'))
    print(70*'#')
    

    if score > old_high_score:
        print(f"\nYour new high score is: {score}.")
    
    if score == old_high_score:
        print(f"\nYour high score is unchanged. It is {score}.")
    
    if score < old_high_score:
        print(f"\nYour current score is {score}. You did not beat your previous high score, which is {old_high_score}.")
     