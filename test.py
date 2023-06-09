import curses
import time

stdscr=curses.initscr()

def main(stdscr):
  for i in range(10):
      # output i
      stdscr.addstr(f"{i} ")
      # refresh stdscr to newscr(not show on the screen)
      stdscr.noutrefresh()
      # move the cursor of newscr to (1,0)
      curses.setsyx(1,0)
      # show it 
      curses.doupdate()
      time.sleep(1)
    


if __name__=="__main__":
  curses.wrapper(main)