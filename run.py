
# Inspired from https://towardsdatascience.com/
# prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b

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
print("""Eat your food and get as big as you can. 
Use arrow keys (up, down, left, right) to navigate.
Do not eat yourself. Do not hit the wall.
""")
print(70*'#')

# Creation of window object is taken from https://www.developer.com/languages/python/python-curses-text-drawing/

import curses
import sys

def main():
  # BEGIN ncurses startup/initialization...
  # Initialize the curses object.
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
  try:
    # Coordinates start from top left, in the format of y, x.
    stdscr.addstr(0, 0, "Hello, world!")
    screenDetailText = "This screen is [" + str(curses.LINES) + "] high and [" + str(curses.COLS) + "] across."
    startingXPos = int ( (curses.COLS - len(screenDetailText))/2 )
    stdscr.addstr(3, startingXPos, screenDetailText)
    stdscr.addstr(5, curses.COLS - len("Press a key to quit."), "Press a key to quit.")

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
