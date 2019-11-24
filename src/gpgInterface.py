#!/usr/bin/env python3

import subprocess as sub

class execHandler():
    def __init__(self, password = 'asdf1234'):
        self.password = password

    def __del__(self):
        self.password = ''

    def decrypt(self, file):
        proc = sub.Popen(['gpg', '--batch', '--passphrase-fd', '0', '--decrypt', file], stdin = sub.PIPE,
            stdout = sub.PIPE, stderr = sub.PIPE)
        (stdout, stderr) = proc.communicate(input = self.password.encode('utf-8'), timeout = 15)
        print(stdout)

    def encrypt(self, file, user):
        proc = sub.Popen(['gpg', '--encrypt', '-o', file, '-r', user], stdin = sub.PIPE,
            stdout = sub.PIPE, stderr = sub.PIPE)
        (stdout, stderr) = proc.communicate(input = self.password.encode('utf-8'), timeout = 15)



if __name__ == '__main__':
    ex = execHandler()
    ex.encrypt('./encrypted.gpg', 'petter.rosander@gmail.com')
    ex.decrypt('./encrypted.gpg')
