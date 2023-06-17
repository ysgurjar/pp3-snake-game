
# Inspired from https://towardsdatascience.com/
# prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b


import random
import time
import sys
import os
from curses import wrapper
import introduction_screen as intro
import authentication as a
import display_constructor as d

# Font styles can be found at http://www.figlet.org/examples.html


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


#import display_constructor as d

# Get termnimal window object. To be used as in main logic to draw elements



def run_game(window):
    # Start terminal window (as a drawing board)
    #d.start_screen(window)

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
            d.clear_screen(board.grid_points)
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


def main():
    """ Main executable logic """
    # welcome text
    intro.welcome_text()
    while True:
        # ask user to choose between sign-in and sign-up.
        is_user_choice_valid, user_choice= a.choose_signing_option()
        # user can press 9 to navigate back to home menu

        # get user_name
        if is_user_choice_valid==True:
            user_name=a.get_user_name()
            Game.player_name=user_name
        # validate user name
        is_username_valid, user_name=a.validate_user_name(user_name)
        # get password
        if is_username_valid==True:
            pwd=a.get_pwd()
        # validate password
        is_pwd_valid,pwd=a.validate_pwd(pwd)

        # run additional validation
        is_add_validation_ok= a.additional_validation(user_name, pwd, user_choice)
        # write user name and password to google sheet
        if is_add_validation_ok==True:
            break
            #g_sheet_update_status=write_userinfo(user_name,pwd)
        # confirm user status as signed in
        #if g_sheet_update_status==True:
        pass
            # print (" you are logg in now")
            # your game will begin in 5,4,3,2,1...
        # user can press 8 to sign out 
    print("\nYou are logge in now. \n")
    print("Your game is about to start.\n")
    
    for i in reversed(range(5)):
        print(i)
        time.sleep(1)

    
    start_game=True
    # start game
    if start_game==True:
        d.stdscr = d.curses.initscr()
        window = d.stdscr
        wrapper(run_game)
    # end game
    os.system('clear')
    # write high score if necessary
    print("your high score is zero.")
    # restart game for same user with an option to sign out and sign in as a new user

    # ask user to sign 

    # if user name and password are validated, 

if __name__ == "__main__":
    while True:
        main()
    
    
    
    