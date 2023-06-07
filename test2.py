import time


class Board:

    grid_points = {}

    def draw_snake(self,window, coordinates):
        """Draws a snake at given coordinates on the board"""
        window.addstr(*coordinates[0], '@')
        for segment in coordinates[1:]:
            window.addstr(*segment, '*')
        
        d.curses.curs_set(0)
        window.refresh()
        time.sleep(4)
        
    def draw_food(self, window, food_coordinates):
        """Draws a food element at given coordinates on grid"""
        window.addstr(*food_coordinates[0], 'X')
                
        d.curses.curs_set(0)
        window.refresh()
        time.sleep(4)

class BoardElement:
    def __init__(self, coordinates):
        self.coordinates = coordinates


class Snake(BoardElement):
    """Represents snake on board"""

    def __init__(self, coordinates):
        BoardElement.__init__(self, coordinates)

    def update_snake(window, coordinates):
        """Increases snake length"""


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


def initialise(window):
    """Sets up intial board before starting the game"""
    board = Board()

    # Get a list of all display coordinates
    board.grid_points = d.calculate_display_coordinates()

    # Construct wall, i.e. boundary of the game and get a list of wall coordinates
    wall = Wall(d.wall_constructor())

    # Define initial body of snake
    snake = Snake([(3, 5), (3, 4), (3, 3),(3,2)])
    # Draw snake
    board.draw_snake(window,snake.coordinates)
    
    # Draw food
    food=Food([(3,8)])
    board.draw_food(window,food.coordinates)
    # Reset player name and high score


if __name__ == "__main__":

    import display_constructor as d

    # Get termnimal window object which is to be used as in main logic to draw elements
    window = d.stdscr
    
    # Start terminal window (as a drawing board)
    d.start_screen(window)


#   # Start game
    game = Game("YG", 0, "running")
    initialise(window)

    # End game
    d.end_screen(window)
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
