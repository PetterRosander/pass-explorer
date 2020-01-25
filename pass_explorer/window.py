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

        self.currXind = 0
        self.currYind = 0
        self.exit = False
        self.next = False
        self.backspace = False

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

    def drawStartWindow(self):
        """
        TODO: Set border settings in another draw class
        should not be hardcoded here
        """
        self.stdscr.vline(1, 0, cs.ACS_VLINE, self.y - 3)
        self.stdscr.hline(0, 1, cs.ACS_HLINE, self.x - 2)
        self.stdscr.addch(0, 0, cs.ACS_ULCORNER)
        self.stdscr.addch(0, self.x - 1, cs.ACS_URCORNER)

        self.stdscr.vline(1, self.x - 1, cs.ACS_VLINE, self.y - 3)
        self.stdscr.hline(self.y - 2, 1, cs.ACS_HLINE, self.x - 2)
        self.stdscr.addch(self.y - 2, 0, cs.ACS_LLCORNER)
        self.stdscr.addch(self.y - 2, self.x - 1, cs.ACS_LRCORNER)

        self.stdscr.vline(1, self.x // 5, cs.ACS_VLINE, self.y - 2)
        self.stdscr.addch(0, self.x // 5, cs.ACS_TTEE)
        self.stdscr.addch(self.y - 2, self.x // 5, cs.ACS_BTEE)

        self.stdscr.vline(1, self.x * 3 // 5, cs.ACS_VLINE, self.y - 2)
        self.stdscr.addch(0, self.x * 3 // 5, cs.ACS_TTEE)
        self.stdscr.addch(self.y - 2, self.x * 3 // 5, cs.ACS_BTEE)

    def enumerateUsers(self, users):
        for ind, f in enumerate(users):
            if ind == self.currXind:
                self.stdscr.addstr(ind + 1, 1, f, cs.A_STANDOUT)
            else:
                self.stdscr.addstr(ind + 1, 1, f)
        self.stdscr.refresh()

    def enumerateFolders(self, folders):
        for ind, f in enumerate(folders):
            if ind == self.currXind:
                self.stdscr.addstr(ind + 1, (self.x // 5) + 1, f, cs.A_STANDOUT)
            else:
                self.stdscr.addstr(ind + 1, (self.x // 5) + 1, f)
        self.stdscr.refresh()

    def enumeratePasswords(self, passwords):
        for ind, f in enumerate(passwords):
            if ind == self.currXind:
                self.stdscr.addstr(ind + 1, (self.x * 3 // 5) + 1, f,
                                   cs.A_STANDOUT)
            else:
                self.stdscr.addstr(ind + 1, (self.x * 3 // 5) + 1, f)
        self.stdscr.refresh()

    def getKey(self):
        key = self.stdscr.getkey()
        if key == 'j':
            self.currXind += 1
        elif key == 'k':
            self.currXind -= 1
        elif key == 'l':
            self.next = True
        elif key == 'q':
            self.exit = True

    def __getPassword__(self):
        key = ''
        passwd = ''
        while key != '\n':
            key = self.stdscr.getch()
            if key == 127:
                self.stdscr.addch(self.y - 1, 9 + len(passwd), ' ')
                passwd = passwd[:-1]
            elif key == 10:
                break
            else:
                passwd += chr(key)
                self.stdscr.addch(self.y - 1, 9 + len(passwd), '*')

        return passwd

    def pickUser(self, users):
        self.next = False
        while not self.next:
            self.enumerateUsers(users)
            self.getKey()
        return self.currXind

    def pickFolder(self, folders):
        self.next = False
        self.currXind = 0
        while not self.next:
            self.enumerateFolders(folders)
            self.getKey()
        return self.currXind

    def pickPassword(self, folders):
        self.next = False
        self.currXind = 0
        while not self.next:
            self.enumeratePasswords(folders)
            self.getKey()
        return self.currXind

    def getPassword(self):
        self.stdscr.addstr(self.y - 1, 0, "Password:", cs.A_STANDOUT)
        return self.__getPassword__()
