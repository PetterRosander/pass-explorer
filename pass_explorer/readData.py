#!/usr/bin/env python3
"""
********************************************
* Imports
********************************************
"""
import os as os


"""
********************************************
* Class passwordReader
* This currently not the correct name
* for this class, TODO: rename to something
* like folderExplorer
********************************************
"""
class passwordRead():
    """
    Methods
    """
    def __init__(self, path = os.getenv('HOME') + '/.password-explore/'):
        self.root = path

    def readUsers(self):
        dircontent = os.listdir(self.root)
        users = []

        for dir in dircontent:
            spt = dir.split('.')
            if len(spt) == 1:
                users.append(spt[0])

        return users

    def readFolders(self):
        dircontent = os.listdir(self.root + self.user)
        folders = []

        for dir in dircontent:
            folders.append(dir)

        return folders

    def readPasswords(self):
        dircontent = os.listdir(self.root + self.user + '/' + self.folder)
        passwords = []
        f = open('pass.log', 'w')
        f.write(str(dircontent) + '\n')
        f.close()

        for dir in dircontent:
            spt = dir.split('.')
            passwords.append(spt[0])

        return passwords

    """
    Exposed class variables
    """
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user

    @property
    def folder(self):
        return self._folder

    @folder.setter
    def folder(self, folder):
        self._folder = folder
