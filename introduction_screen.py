"""
This module provides the text on the terminal at the beginning \
    of game and end of a game
"""
# =====================================
# IMPORTS
# =====================================
from termcolor import colored
from pyfiglet import Figlet

# =====================================
# FUNCTION DEFINITIONS
# =====================================


def welcome_text():
    """Provides welcome text at the beginning of the game"""
    print(70 * "#")
    f = Figlet(font="standard")
    print(colored(f.renderText("WELCOME TO SNAKE"), "green"))
    print(70 * "#")

    # Rules
    f = Figlet(font="contessa")
    print(colored(f.renderText("RULES"), "red"))
    print(
        """> You are a snake.Eat your prey and get as big as you can.
> Use arrow keys (up, down, left, right) to navigate.
> Do not eat yourself. Do not hit the wall.
"""
    )
    print(70 * "#")


def game_over_text(score, old_high_score):
    """Prints text on terminal when game is over

    Args:
        score (int): score from the game that was just over
        old_high_score (int): user's high score stored in database
    """
    print(70 * "#")
    f = Figlet(font="standard")
    print(colored(f.renderText("GAME OVER"), "green"))
    print(70 * "#")

    if score > old_high_score:
        print(f"\nYour new high score is: {score}.")

    if score == old_high_score:
        print(f"\nYour high score is unchanged. It is {score}.")

    if score < old_high_score:
        print(f"\nYour current score is {score}.")
        print(f"You couldn't beat your previous high score {old_high_score}.")
