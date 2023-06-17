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


