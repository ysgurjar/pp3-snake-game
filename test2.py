class Board:
    """Represents display screen for game"""
    def __init__(self, grid_points):
        """Reoresents a list of ALL grid-points in x,y coordinate system on which board elements will be drawn"""
        self.grid_points=grid_points
    
    def draw_wall(coordinates):
        """Draws wall at given coordinates on the board"""
        pass

    def draw_snake(coordinates):
        """Draws a snake at given coordinates on the board"""
        pass

    def draw_food(coordinates):
        """Draws a food element at given coordinates on grid"""

class BoardElement:
    def __init__(self,coordinates):
        self.coordinates=coordinates

class Snake(BoardElement):
    """Represents snake on board"""
    def __init__(self, coordinates):
        BoardElement.__init__(self, coordinates)
    
    def update_snake(coordinates):
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


if __name__=="__main__":
    snake=Snake([(1,1),(2,2),(3,3)])
    print(snake)
    print(snake.coordinates)
