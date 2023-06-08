
# Inspired from https://towardsdatascience.com/
# prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b


import display_constructor as d
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

        d.curses.curs_set(0)
        window.refresh()
        time.sleep(0.5)

    def draw_food(self, window, food_coordinates):
        """Draws a food element at given coordinates on grid"""
        window.addstr(*food_coordinates, 'X')

        d.curses.curs_set(0)
        window.refresh()
        time.sleep(0.5)


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
        d.curses.curs_set(0)

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
    def __init__(self, player_name, high_score, game_status):
        self.player_name = player_name
        self.high_score = high_score
        self.game_status = game_status

    def terminate():
        """End game"""


def get_food_coordinates(board, wall, snake):
    """Returns a random point on board that is neither a wall nor a snake"""
    food_coordinates = board.difference(wall, snake)
    food_coordinate = random.choice(list(food_coordinates))
    return food_coordinate


def grabbed_object():
    """Returns the object that snake intercepts as it moves on the grid"""


def initialise(window):
    """Sets up intial board before starting the game"""
    board = Board()

    # Get a list of all display coordinates as a set
    board.grid_points = d.calculate_display_coordinates()

    # Construct wall, i.e. boundary of the game and get a list of wall coordinates
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


# Get termnimal window object which is to be used as in main logic to draw elements
window = d.stdscr

# Start terminal window (as a drawing board)
d.start_screen(window)

# Don't block I/O calls
window.nodelay(True)


def main(window):

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

    for i in range(30):

        # save the coordinates of snake
        snake_old_coordinates = snake.coordinates
        # remove previously drawn snake
        snake.remove(window)
        # move snake to new coordinates either based
        # on default behaviour or uesr key input
        try:
            capture_key = window.getkey()
        except:
            capture_key = None

        direction = directions.get(capture_key, direction)

        snake.move_snake(direction)

        # Save the new coordinates of snake
        snake_new_coordinates = snake.coordinates
        # redraw snake
        board.draw_snake(window, snake.coordinates)

        # Check whether snake has encountered itsef, food or wall

        encountered_object = encountered_object(
            snake_new_coordinates,
            snake_old_coordinates,
            wall.coordinates)

        if encountered_object=="wall" or encountered_object=="snake":
            """game over"""
        
        if encountered_object=="food":
            """increase snake length"""

    d.end_screen(window)
    # End game


if __name__ == "__main__":

    wrapper(main)

#     # wall_coordianates,
#     # snake_coordinates,
#     # food_coordinates)
#     # # Loop
#     #   while game.status=="running":
#             # run_game()
#     #

# def run_game():
#     # Move snake
#     #     snake.move(direction)

#     #   # Following the move, check the object grabbed i.e. wall, itself or food
#     #     grabbed_object=snake.grabbed_object()

#     #   # Depending on the grabbed object, either terminate the game or increase snake size
#     #     if grabbed_object==wall or grabbed_object== itself:
#     #     # Terminate game
#     #     # Compare user's current score against recorded high score, update if necessary
#     #     # Take user back to home page
#     #     elif grabbed_object= food:
#     #     #update snake with new head and body
#     #     #update high score for given user
#     #     snake.update()
#     #     else:
#     #     # continue moving snake in same direction
