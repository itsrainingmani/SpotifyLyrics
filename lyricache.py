import sys, os
import json
import time


def format_names(song, artist):
    return "{}_{}_lyr.txt".format(artist, song)


class Lyricache:
    def __init__(self):
        # Get the files in the current directory
        curdir_list = os.listdir(path=".")
        cache_name = ".cache"

        if cache_name not in curdir_list:
            print("Cache Folder does not exist. Creating one...")

            # Try to create the cache dir
            try:
                os.mkdir(path=os.path.join(os.getcwd(), cache_name))
                self.cache_dir = os.path.join(os.getcwd(), cache_name)
                print("Cache Folder has been created")
            except FileExistsError:
                print("Unable to create Cache Folder")
        else:
            print("Cache Folder already exists")
            self.cache_dir = os.path.join(os.getcwd(), cache_name)

    def get_cache_dir(self):
        return self.cache_dir

    def add_to_cache(self, song, artist, lyrics):
        lyr_cache_name = format_names(song, artist)
        pass

    def check_cache(self, song, artist):
        lyr_cache_name = format_names(song, artist)
        print(lyr_cache_name)
        if self.cache_dir:
            cachedir_list = os.listdir(path=self.cache_dir)
            if lyr_cache_name not in cachedir_list:
                return False
            else:
                return True
        else:
            print("Cache Folder does not exist. Exiting...")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def clear_cache(self):
        if self.cache_dir:
            cachedir_list = os.listdir(path=self.cache_dir)
            for f in cachedir_list:
                f_path = os.path.join(self.cache_dir, f)
                try:
                    os.remove(f_path)
                except:
                    print("Cache File - {} could not be removed".format(f))
            print("Cache Folder cleared")
        else:
            print("Cache Folder does not exist")


if __name__ == "__main__":
    c = Lyricache()
    print(c.get_cache_dir())
    # c.clear_cache()
    print(c.check_cache("blackened", "metallica"))
