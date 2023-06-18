"""
Provides the curses module capabilities and
a seperate display screen for game to play

Prvoides functions that will draw game boundries
and return a list og all coordinates on dispaly screen
"""
# =====================================
# IMPORTS
# =====================================
import curses

# =====================================
# FUNCTION DEFINITIONS
# =====================================


def wall_constructor():
    """Constructs wall around the screen of
    vertical length of 20 and horizontal length
    equal to display width

    Returns:
        set: a set of tuples containing wall coordinates on display
    """
    wall_coordinates = set()
    # Constructing vertical walls. remember y,x representation in addstr
    for i in range(20):
        stdscr.addstr(i, curses.COLS - 1, "O")
        stdscr.addstr(i, 0, "O")
        wall_coordinates.add((i, curses.COLS - 1))
        wall_coordinates.add((i, 0))
    # Constructing horizontal wall, remember y,x representation in addstr
    for i in range(curses.COLS):
        stdscr.addstr(0, i, "O")
        stdscr.addstr(20, i, "O")
        wall_coordinates.add((0, i))
        wall_coordinates.add((20, i))
    stdscr.refresh()
    return wall_coordinates


def calculate_display_coordinates():
    """Calculated each and every point available on grid

    Returns:
        set: a set of tuples containing all grid points
    """
    grid_points = set()
    for x in range(20):
        for y in range(curses.COLS - 1):
            grid_points.add((x, y))
    return grid_points


def clear_screen(screen_points):
    """Erases charcter by drawing an empty
    string at grid point

    Args:
        screen_points (list): list of grid points that needs to be erased
    """
    for point in screen_points:
        stdscr.addstr(*point, " ")
        stdscr.refresh()
