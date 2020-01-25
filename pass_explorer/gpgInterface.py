#!/usr/bin/env python3

import subprocess as sub


class execHandler():
    def __init__(self, root):
        self.root = root

    def decrypt(self, file):
        proc = sub.Popen(['gpg', '--batch', '--passphrase-fd',
                          '0', '--decrypt', file], stdin = sub.PIPE,
                         stdout = sub.PIPE, stderr = sub.PIPE)
        (stdout, stderr) = proc.communicate(input =
                                            self.password.encode('utf-8'),
                                            timeout = 15)
        return stdout.decode('utf-8')

    def encrypt(self, file, user):
        proc = sub.Popen(['gpg', '--encrypt', '-o', file, '-r', user],
                         stdin = sub.PIPE, stdout = sub.PIPE,
                         stderr = sub.PIPE)
        (stdout, stderr) = proc.communicate(input =
                                            self.password.encode('utf-8'),
                                            timeout = 15)

    def validateUser(self, root):
        validFile = root + '/' + self._user + '.verify'
        out = self.decrypt(validFile)

        if out.rstrip() == self._user:
            return True
        else:
            return False

    def decryptPassword(self, password):
        passwdFile = self.root  + self._user + '/' + self._folder + '/' + password + '.gpg'
        return self.decrypt(passwdFile).rstrip()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

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
