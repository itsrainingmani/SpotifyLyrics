import sys, os
import json
import time


class Lyricache:
    def __init__(self):
        # Get the files in the current directory
        curdir_list = os.listdir(path=".")

        if ".cache" not in curdir_list:
            print("Cache Folder does not exist. Creating one...")

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

    def clearCache(self):
        if self.cache_dir:
            cachedir_list = os.listdir(path=self.cache_dir)
            for f in cachedir_list:
                f_path = self.cache_dir + "/" + f
                try:
                    os.remove(f_path)
                except:
                    print("Cache File - {} could not be removed".format(f))
            print("Cache Folder cleared")
        else:
            print("Cache Folder does not exist")


if __name__ == "__main__":
    c = Lyricache()
    print(c.getCacheDir())
