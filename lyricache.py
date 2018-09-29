import sys, os
import json
import time


class Lyricache:
    def __init__(self):
        # Get the files in the current directory
        curdir_list = os.listdir(path=".")

        if ".cache" not in curdir_list:
            print("Cache Folder not present. Creating one...")

            # Try to create the cache dir
            try:
                os.mkdir(path=os.getcwd() + "/.cache")
                self.cache_dir = os.getcwd() + "/.cache"
                print("Cache Folder has been created")
            except FileExistsError:
                print("Unable to create Cache Folder")
        else:
            print("Cache Folder already exists")
            self.cache_dir = os.getcwd() + "/.cache"

    def getCacheDir(self):
        return self.cache_dir


if __name__ == "__main__":
    c = Lyricache()
