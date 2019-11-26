#!/usr/bin/env python3
import window as _win

win = _win.window()
try:
    win.main()
except Exception as e:
    win.__del__()
    print(e)
del win
