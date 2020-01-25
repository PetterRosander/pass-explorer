#!/usr/bin/env python3
import traceback as tb
import pass_explorer.window as _win
import pass_explorer.gpgInterface as _gpg
import pass_explorer.readData as explorer

def setUserAndPassword(gpg, exp, user, passwd):
    gpg.password = passwd
    gpg.user = user
    exp.user = user
    exp.password = passwd

def run():
    exception = ''
    try:
        win = _win.window()
        gpg = _gpg.execHandler()
        exp = explorer.passwordRead()
    
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
    
            win.pickPassword(passwordFiles)
    
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
        print(passwordFiles)
    else:
        print(valid)
