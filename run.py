
# Inspired from https://towardsdatascience.com/
# prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b


import random
import time
import sys
import os
from curses import wrapper
from termcolor import colored
from pyfiglet import Figlet

# Font styles can be found at http://www.figlet.org/examples.html


# Welcome Text
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

# Build game


class Board:

    grid_points = {}

    def draw_snake(self, window, coordinates):
        """Draws a snake at given coordinates on the board"""
        # Delete any residual charater
        for e in coordinates:
            window.addstr(*e, ' ')
            window.refresh()
        window.addstr(*coordinates[0], '@')

        for segment in coordinates[1:]:
            window.addstr(*segment, '*')
            window.refresh()

        # d.curses.curs_set(0) - optional. Turned off for heroku CLI
        window.refresh()
        d.curses.setsyx(*coordinates[-1])
        d.curses.doupdate()

        time.sleep(0.2)

    def draw_food(self, window, food_coordinates):
        """Draws a food element at given coordinates on grid"""
        window.addstr(*food_coordinates, 'X')

        # d.curses.curs_set(0) - optional. Turned off for heroku CLI
        window.refresh()


class BoardElement:
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Snake(BoardElement):
    """Represents snake on board"""

    def __init__(self, coordinates):
        BoardElement.__init__(self, coordinates)

    def remove(self, window):
        """Remove previously drawn snake"""
        for c in self.coordinates:
            window.addstr(*c, ' ')
        # d.curses.curs_set(0) - optional. Turned off for heroku CLI

    def move_snake(self, direction):
        """Moves snake around the board"""
        head = self.coordinates[0]
        zip_obj = zip(head, direction)
        coordinate = [sum(x) for x in zip_obj]
        new_head = tuple(coordinate)
        self.coordinates.insert(0, new_head)
        self.coordinates.pop(-1)


class Food(BoardElement):
    """Represents food for snake on board"""

    def __init__(self, coordinates):
        BoardElement.__init__(self, coordinates)

    def update_food(coordinates):
        """randomly generate a food, represented as a dot on a board"""


class Wall(BoardElement):
    """Represents wall on board"""

    def __init__(self, coordinates):
        BoardElement.__init__(self, coordinates)


class Game:
    def __init__(self, player_name, score, game_status):
        self.player_name = player_name
        self.score = score
        self.game_status = game_status

    def terminate():
        """End game"""


def get_food_coordinates(board, wall, snake):
    """Returns a random point on board that is neither a wall nor a snake"""
    food_coordinates = board.difference(wall, snake)
    food_coordinate = random.choice(list(food_coordinates))
    return food_coordinate


def find_encountered_object(snake_head_position,
                            snake_old_coordinates,
                            wall_coordinates,
                            food_coordinates):
    """Returns the object that snake intercepts as it moves on the grid"""
    if set(snake_head_position).intersection(set(snake_old_coordinates)) != set():
        return "snake"

    if set(snake_head_position).intersection(set(wall_coordinates)) != set():
        return "wall"

    if set(snake_head_position).intersection(set(food_coordinates)) != set():
        return "food"


def initialise(window):
    """Sets up intial board before starting the game"""
    board = Board()

    # Get a list of all display coordinates as a set
    board.grid_points = d.calculate_display_coordinates()

    # Construct boundary of the game and get a list of wall coordinates
    wall = Wall(d.wall_constructor())

    # Define initial body of snake
    snake = Snake([(3, 5), (3, 4), (3, 3), (3, 2)])
    # Draw snake at given coordinates
    board.draw_snake(window, snake.coordinates)

    # Draw food at given coordinates
    food = Food(get_food_coordinates(board.grid_points,
                wall.coordinates, set(snake.coordinates)))
    board.draw_food(window, food.coordinates)

    # Reset player name and high score

    return board, wall, snake, food


import display_constructor as d

# Get termnimal window object. To be used as in main logic to draw elements
window = d.stdscr


def main(window):
    # Start terminal window (as a drawing board)
    d.start_screen(window)

    # Don't block I/O calls
    window.nodelay(True)

    # Start game
    game = Game("YG", 0, "running")

    board, wall, snake, food = initialise(window)

    directions = {
      "KEY_UP": (-1, 0),
      "KEY_DOWN": (1, 0),
      "KEY_LEFT": (0, -1),
      "KEY_RIGHT": (0, 1)
      }
    direction = directions.get("KEY_RIGHT")

    for i in range(300):

        # save the coordinates of snake
        snake_old_coordinates = list(snake.coordinates)
        # remove previously drawn snake
        snake.remove(window)
        # move snake to new coordinates either based
        # on default behaviour or uesr key input
        try:
            capture_key = window.getkey()
        except:
            capture_key = None

        match (direction, capture_key):
            case ((-1, 0), "KEY_DOWN"):
                pass
            case ((1, 0), "KEY_UP"):
                pass
            case ((0, -1), "KEY_RIGHT"):
                pass
            case ((0, 1), "KEY_LEFT"):
                pass
            case _:
                direction = directions.get(capture_key, direction)

        snake.move_snake(direction)

        # Save the new coordinates of snake
        snake_head_position = [list(snake.coordinates)[0]]
        # redraw snake
        board.draw_snake(window, snake.coordinates)

        # Check whether snake has encountered itsef, food or wall

        encountered_object = find_encountered_object(
            snake_head_position,
            snake_old_coordinates,
            wall.coordinates,
            [(food.coordinates)])

        if encountered_object == "wall" or encountered_object == "snake":
            """game over"""
            break

        if encountered_object == "food":
            """increase snake length"""

            # increase snake length
            snake_old_coordinates.insert(0, snake_head_position[0])
            snake_new_coordinates = snake_old_coordinates
            snake.coordinates = snake_new_coordinates.copy()

            # increase score
            game.score = game.score + 10
            window.addstr(22, 1, " score:" + str(game.score))

            # Draw food at given coordinates
            food = Food(get_food_coordinates(board.grid_points,
                                             wall.coordinates,
                                             set(snake.coordinates)))
            board.draw_food(window, food.coordinates)


if __name__ == "__main__":
    wrapper(main)
    os.system('clear')
    welcome_text()