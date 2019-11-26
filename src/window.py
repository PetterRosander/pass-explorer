#!/usr/bin/env python3
import curses as cs


class window():
    def __init__(self):
        """
        setup a ncurses friendly terminal
        and initialise the settings get window size
        Sets up the different border windows as well
        """
        self.stdscr = cs.initscr()
        cs.noecho()
        cs.cbreak()
        cs.curs_set(0)
        self.y, self.x = self.stdscr.getmaxyx()

        """
        TODO (see bellow as well)
        move the border size to another class handler
        """
        self.col1 = cs.newwin(0, self.x // 5, 0, 0)
        self.col2 = cs.newwin(0, self.x // 5, 0, self.x*3 // 5)
        self.col3 = cs.newwin(0, self.x*3 // 5, 0, self.x)

    def __del__(self):
        """
        End the current ncurses firendly terminal and
        clean up in order to get it back to normal when
        the application is done
        """
        self.stdscr.keypad(False)
        cs.nocbreak()
        cs.echo()
        cs.endwin()

    def updateSize(self):
        self.y, self.x = self.stdscr.getmaxyx()

    def drawWindow(self):
        """
        TODO: Set border settings in another draw class
        should not be hardcoded here
        """
        self.stdscr.border()
        self.stdscr.vline(1, self.x // 5, cs.ACS_VLINE, self.y - 2)
        self.stdscr.addch(0, self.x // 5 , cs.ACS_TTEE)
        self.stdscr.addch(self.y - 1, self.x // 5 , cs.ACS_BTEE)

        self.stdscr.vline(1, self.x*3 // 5, cs.ACS_VLINE, self.y - 2)
        self.stdscr.addch(0, self.x*3 // 5 , cs.ACS_TTEE)
        self.stdscr.addch(self.y - 1, self.x*3 // 5 , cs.ACS_BTEE)

        self.stdscr.refresh()


    def main(self):
        self.updateSize()
        self.stdscr.clear()
        self.drawWindow()

        self.stdscr.refresh()
        self.stdscr.getkey()
