#!/usr/bin/env python3
import traceback as tb
import pass_explorer.window as _win
import pass_explorer.gpgInterface as _gpg
import pass_explorer.readData as explorer
import os as os

def setUserAndPassword(gpg, exp, user, passwd):
    gpg.password = passwd
    gpg.user = user
    exp.user = user
    exp.password = passwd

def run():
    exception = ''
    try:
        HOME = os.getenv('HOME')
        root = HOME + '/.password-explorer/'
        win = _win.window()
        gpg = _gpg.execHandler(root)
        exp = explorer.passwordRead(root)

        users = exp.readUsers()
        win.drawStartWindow()
        uInd = win.pickUser(users)
        passwd = win.getPassword()

        setUserAndPassword(gpg, exp, users[uInd], passwd)

        valid = gpg.validateUser(exp.root)

        if valid:
            folders = exp.readFolders()
            fInd = win.pickFolder(folders)

            exp.folder = folders[fInd]
            passwordFiles = exp.readPasswords()

            pInd = win.pickPassword(passwordFiles)

            gpg.folder = folders[fInd]
            password = gpg.decryptPassword(passwordFiles[pInd])

        else:
            pass

    except Exception as e:
        excpetion = e

    finally:
        del win

    if exception:
        tb.print_exc()
        print(excpetion)
    if valid:
        print(password)
    else:
        print(valid)
