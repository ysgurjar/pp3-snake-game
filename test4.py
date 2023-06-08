
# Inspired from https://towardsdatascience.com/
# prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b

#import display_constructor as d
import random
import time
import sys
from curses import wrapper
from termcolor import colored
from pyfiglet import Figlet

# Font styles can be found at http://www.figlet.org/examples.html

# Welcome Text
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