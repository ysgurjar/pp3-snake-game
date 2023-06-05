
# Inspired from https://towardsdatascience.com/
# prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b

from termcolor import colored
from pyfiglet import Figlet

# Font styles can be found at http://www.figlet.org/examples.html
f = Figlet(font="5lineoblique")
print(colored(f.renderText('WELCOME TO SNAKE'), 'green'))

print(70*'#')

f = Figlet(font="contessa")
print(colored(f.renderText("RULES"), 'red'))

print("""
Eat your food and get as big as you can. 

Use arrow keys (up, down, left, right) to navigate.

Do not eat yourself. Do not hit the wall.
"""
      )
print(70*'#')