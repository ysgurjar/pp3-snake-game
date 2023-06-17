import curses

# BEGIN ncurses startup/initialization...
# Initialize the curses object. Stdscr stands for standard screen i.e. display in the terminal

def display_caught_exceptions(caughtExceptions):
# Display Errors if any happened:
    if "" != caughtExceptions:
        print ("Got error(s) [" + caughtExceptions + "]")

def start_screen(stdscr):

    try:
        # Do not echo keys back to the client.
        curses.noecho()

        # Non-blocking or cbreak mode... do not wait for Enter key to be pressed.
        curses.cbreak()

        # Turn off blinking cursor
        #curses.curs_set(False)
        
        # Enable color if we can...
        if curses.has_colors():
            curses.start_color()


    except Exception as err:
        # Just printing from here will not work, as the program is still set to
        # use ncurses.
        print ("Some error [" + str(err) + "] occurred.")
        caughtExceptions = str(err)
        display_caught_exceptions(caughtExceptions)
         
def end_screen(stdscr):
     # Turn off cbreak mode...
        curses.nocbreak()

        # Turn echo back on.
        curses.echo()

        # Restore cursor blinking.
        #curses.curs_set(True)

        # Turn off the keypad...
        stdscr.keypad(False)

        # Restore Terminal to original state.
        curses.endwin()

def wall_constructor():
    wall_coordinates=set()

    # Constructing vertical walls. remember y,x representation in addstr
    for i in range(20):
            stdscr.addstr(i, curses.COLS-1, "O")
            stdscr.addstr(i, 0, "O")
            wall_coordinates.add((i,curses.COLS-1))
            wall_coordinates.add((i,0))
    # Constructing horizontal wall, remember y,x representation in addstr
    for i in range(curses.COLS):
            stdscr.addstr(0, i, "O")
            stdscr.addstr(20, i, "O")
            wall_coordinates.add((0,i))
            wall_coordinates.add((20,i))
    stdscr.refresh()
    return wall_coordinates

def calculate_display_coordinates():
    grid_points=set()
    for x in range(20):
        for y in range(curses.COLS-1):
            grid_points.add((x,y))
    return grid_points

def clear_screen(screen_points):
    for point in screen_points:
        stdscr.addstr(*point," ")
        stdscr.refresh()