#!/usr/bin/env python3
import os as os

class passwordRead():
    def __init__(self, path = os.getenv('HOME') + '/.password-store'):
        self.root = path
        self.gpgFiles = []

    def __del__(self):
        pass

    def __read__(self, directory):
        dircontent = os.listdir(directory)

        for dir in dircontent:
            if os.path.isdir(self.root + '/'+ dir):
                self.__read__(self.root + '/'+ dir)
            elif dir != '.gpg-id':
                self.gpgFiles.append(dir)

    def read(self, directory = ''):
        self.__read__(self.root)



if __name__ == '__main__':
    reader = passwordRead()
    reader.read()
    print(reader.gpgFiles)

