
# Inspired from https://towardsdatascience.com/
# prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b

import sys
import curses
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

# Build game

wall = []


def initialize(stdscr):
    """Draw initial board, snake and food. Set current score to zero."""
    # Draw board. Coordinates start from top left, in the format of y, x.
    
    for i in range(20):
        stdscr.addstr(i,curses.COLS-1,"O")
        stdscr.addstr(i,0,"O")
    for i in range(curses.COLS):
        stdscr.addstr(0,i,"O")
        stdscr.addstr(20,i,"O")
    # Draw snake

    # Draw food

    # Set current score to zero
        
# Creation of window object is taken from https://www.developer.com/languages/python/python-curses-text-drawing/


def main():
  # BEGIN ncurses startup/initialization...
  # Initialize the curses object. stdscr refers to screen object
  stdscr = curses.initscr()

  # Do not echo keys back to the client.
  curses.noecho()

  # Non-blocking or cbreak mode... do not wait for Enter key to be pressed.
  curses.cbreak()

  # Turn off blinking cursor
  curses.curs_set(False)

  # Enable color if we can...
  if curses.has_colors():
    curses.start_color()

  # Optional - Enable the keypad. This also decodes multi-byte key sequences
  # stdscr.keypad(True)

  # END ncurses startup/initialization...

  caughtExceptions = ""

  # Primay logic i.e. try statement
  try:
    # # Autheticate user
    # is_user_autheticated=autheticate()

    # # If user is autheticated, start the game
    # if is_user_autheticated==True:
    #   # Draw initial board, snake and food, set game score to zero
      initialize(stdscr)

    # # Loop
    #   while True:
    #   # Move snake
    #     snake.move(direction)

    #   # Following the move, check the object grabbed i.e. wall, itself or food
    #     grabbed_object=snake.grabbed_object()

    #   # Depending on the grabbed object, either terminate the game or increase snake size
    #     if grabbed_object==wall or grabbed_object== itself:
    #     # Terminate game
    #     # Compare user's current score against recorded high score, update if necessary
    #     # Take user back to home page
    #     elif grabbed_object= food:
    #     #update snake with new head and body
    #     #update high score for given user
    #     snake.update()
    #     else:
    #     # continue moving snake in same direction

    # Actually draws the text above to the positions specified.
      stdscr.refresh()

    # Grabs a value from the keyboard without Enter having to be pressed (see cbreak above)
      stdscr.getch()
  except Exception as err:
   # Just printing from here will not work, as the program is still set to
   # use ncurses.
   # print ("Some error [" + str(err) + "] occurred.")
   caughtExceptions = str(err)

  # BEGIN ncurses shutdown/deinitialization...
  # Turn off cbreak mode...
  curses.nocbreak()

  # Turn echo back on.
  curses.echo()

  # Restore cursor blinking.
  curses.curs_set(True)

  # Turn off the keypad...
  # stdscr.keypad(False)

  # Restore Terminal to original state.
  curses.endwin()

  # END ncurses shutdown/deinitialization...

  # Display Errors if any happened:
  if "" != caughtExceptions:
   print ("Got error(s) [" + caughtExceptions + "]")

if __name__ == "__main__":
  main()
