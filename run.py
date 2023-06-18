# =====================================
# IMPORTS
# =====================================
# 3rd party
import random
import time
import sys
import os
from curses import wrapper

# Internal
import introduction_screen as intro
import authentication as a
import display_constructor as d

# =====================================
# CLASS DEFINITION
# =====================================


class Board:
    """
    A class used to represent the game area.
    """

    grid_points = {}

    def draw_snake(self, window, coordinates):
        """Draws snake on board at given coordinates

        Args:
            window (obj): represents current window
            coordinates (set): a set of tuples containing (y,x) coordinates
        """

        # Delete any residual charater
        for e in coordinates:
            window.addstr(*e, " ")
            window.refresh()
        window.addstr(*coordinates[0], "@")

        for segment in coordinates[1:]:
            window.addstr(*segment, "*")
            window.refresh()

        # Keep the blinker at tail of snake and not at second from last element
        window.refresh()
        d.curses.setsyx(*coordinates[-1])
        d.curses.doupdate()

        time.sleep(0.2)

    def draw_food(self, window, food_coordinates):
        """Draws food, marked as X on board at given coordinates

        Args:
            window (obj): reprsents current window
            food_coordinates (set): set of tuples containing (y,x) coordinates
        """
        window.addstr(*food_coordinates, "X")
        window.refresh()


class BoardElement:
    """Superclass to define board elements i.e. snake, food and wall.
    All of these elements have coordinates as common proprty.
    """

    def __init__(self, coordinates):
        self.coordinates = coordinates


class Snake(BoardElement):
    """Represents a snake on board"""

    def __init__(self, coordinates):
        BoardElement.__init__(self, coordinates)

    def remove(self, window):
        """Before redrawing the snake, \
        it removes the previously drawn snake from board

        Args:
            window (obj): represents current window
        """
        for c in self.coordinates:
            window.addstr(*c, " ")

    def move_snake(self, direction):
        """Moves snake one step in given direction.
        This is achieved by redrawing the head one step forward \
            and removing one element from tail. \
        Movement is achieved my mathematical sum of \
        snake's body coordinates with given direction.
        Args:
            direction (array): reprsents direction as (y,x)
        """
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


class Wall(BoardElement):
    """Represents wall on board"""

    def __init__(self, coordinates):
        BoardElement.__init__(self, coordinates)


class Game:
    def __init__(self, player_name, score, game_status):
        self.player_name = player_name
        self.score = score
        self.game_status = game_status


# =====================================
# FUNCTION DEFINITION
# =====================================


def get_food_coordinates(board, wall, snake):
    """Returns a random point on board that is neither a wall nor a snake

    Args:
        board (obj): object of Board class
        wall (obj): object of Wall class
        snake (obj): object of Snake class

    Returns:
        list: [y,x] point on grid
    """
    food_coordinates = board.difference(wall, snake)
    food_coordinate = random.choice(list(food_coordinates))
    return food_coordinate


def find_encountered_object(
    snake_head_position,
    snake_old_coordinates,
    wall_coordinates,
    food_coordinates,
):
    """Returns the object encountered by snake's head following its movement

    Args:
        snake_head_position (tuple): \
            location of snake's head on grid represented by (y,x)
        snake_old_coordinates (list):\
             location of previous'y drawing snake's head and body on grid
        wall_coordinates (set): location of wall on grid
        food_coordinates (list): location of food on grid

    Returns:
        str: returns the object encountered by head of snake
    """
    if (
        set(snake_head_position).intersection(set(snake_old_coordinates))
        != set()
    ):
        return "snake"

    if set(snake_head_position).intersection(set(wall_coordinates)) != set():
        return "wall"

    if set(snake_head_position).intersection(set(food_coordinates)) != set():
        return "food"


def initialise(window):
    """Sets up intial board before starting the game

    Args:
        window (obj): represents current window

    Returns:
        obj: board and board-elements i.e. snake, wall and food
    """
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
    food = Food(
        get_food_coordinates(
            board.grid_points, wall.coordinates, set(snake.coordinates)
        )
    )
    board.draw_food(window, food.coordinates)
    # Reset player name and high score
    return board, wall, snake, food


def run_game(window):
    """Main game logic

    Args:
        window (obj): represents current window
    """

    # Don't block I/O calls - allows snake to move without user input
    window.nodelay(True)
    # Start game
    game = Game("user", 0, "running")
    # Initialise
    board, wall, snake, food = initialise(window)
    directions = {
        "KEY_UP": (-1, 0),
        "KEY_DOWN": (1, 0),
        "KEY_LEFT": (0, -1),
        "KEY_RIGHT": (0, 1),
    }
    direction = directions.get("KEY_RIGHT")
    while True:
        # Save the coordinates of snake
        snake_old_coordinates = list(snake.coordinates)
        # Remove previously drawn snake
        snake.remove(window)
        # Move snake to new coordinates either based
        # on default behaviour or uesr key input
        try:
            capture_key = window.getkey()
        except Exception:
            capture_key = None

        # prevent snake from moving 180 degrees.
        # It can only move 90 degrees
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
        # Redraw snake
        board.draw_snake(window, snake.coordinates)
        # Check whether snake has encountered itsef, food or wall
        encountered_object = find_encountered_object(
            snake_head_position,
            snake_old_coordinates,
            wall.coordinates,
            [(food.coordinates)],
        )
        if encountered_object == "wall" or encountered_object == "snake":
            # Game over
            d.clear_screen(board.grid_points)
            d.clear_screen(
                {
                    (22, 1),
                    (22, 2),
                    (22, 3),
                    (22, 4),
                    (22, 5),
                    (22, 6),
                    (22, 7),
                    (22, 8),
                    (22, 9),
                    (22, 10),
                }
            )
            return game.score
        if encountered_object == "food":
            # increase snake length
            snake_old_coordinates.insert(0, snake_head_position[0])
            snake_new_coordinates = snake_old_coordinates
            snake.coordinates = snake_new_coordinates.copy()
            # increase score
            game.score = game.score + 10
            window.addstr(22, 1, "score:" + str(game.score))
            # Draw food at given coordinates
            food = Food(
                get_food_coordinates(
                    board.grid_points, wall.coordinates, set(snake.coordinates)
                )
            )
            board.draw_food(window, food.coordinates)


def main():
    # Welcome text
    intro.welcome_text()
    while True:
        # Ask user to choose between sign-in and sign-up.
        is_user_choice_valid, user_choice = a.choose_signing_option()
        # Get user_name
        if is_user_choice_valid is True:
            user_name = a.get_user_name()
        # Validate user name-loop until valid username is provided
        is_username_valid, user_name = a.validate_user_name(user_name)
        # Get password
        if is_username_valid is True:
            pwd = a.get_pwd()
        # Validate password-loop until vaild password is provided
        is_pwd_valid, pwd = a.validate_pwd(pwd)
        # Run additional validation
        is_add_validation_ok = a.additional_validation(
            user_name, pwd, user_choice
        )
        # Break out of loop if everything is validated and start game
        if is_add_validation_ok is True:
            break

    print("\nYou are logged in now. \n")
    print("Your game is about to start.\n")
    for i in reversed(range(5)):
        print(i)
        time.sleep(1)
    # Start game
    d.stdscr = d.curses.initscr()
    window = d.stdscr
    score = wrapper(run_game)

    # End game and clear screen
    os.system("clear")    
    # Game over text
    intro.game_over_text(score, a.get_high_score(user_name))
    print("Redirecting to main screen.. Please wait..")
    # Check and update high score if necessary
    a.update_gsheet_high_score(user_name, score)
    time.sleep(10)


# =====================================
# RUN PROGRAM
# =====================================
if __name__ == "__main__":
    while True:
        main()
