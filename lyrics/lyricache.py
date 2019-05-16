import os
import pickle


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

    def get_cache_dir_list(self):
        return os.listdir(self.cache_dir)

    def add_to_cache(self, song, artist, lyrics):
        if self.cache_dir:
            if not self.is_in_cache(song, artist) and len(lyrics) > 1:
                lcn = format_names(song, artist)
                with open(os.path.join(self.cache_dir, lcn), "wb") as cache_file:
                    pickle.dump(lyrics, cache_file)
            else:
                return
        else:
            print("Cache Folder does not exist\n")
            return

    def read_from_cache(self, song, artist):
        if self.cache_dir:
            if self.is_in_cache(song, artist):
                lcn = format_names(song, artist)
                lyrics = []
                with open(os.path.join(self.cache_dir, lcn), "rb") as cache_file:
                    lyrics = pickle.load(cache_file)
                return lyrics
            else:
                return
        else:
            print("Cache Folder does not exist\n")
            return

    def is_in_cache(self, song, artist):
        if self.cache_dir:
            lcn = format_names(song, artist)
            cachedir_list = os.listdir(path=self.cache_dir)
            return lcn in cachedir_list
        else:
            print("Cache Folder does not exist\n")
            return

    def clear_cache(self):
        if self.cache_dir:
            cachedir_list = os.listdir(path=self.cache_dir)
            for f in cachedir_list:
                f_path = os.path.join(self.cache_dir, f)
                try:
                    os.remove(f_path)
                except OSError:
                    print("Cache File - {} could not be removed\n".format(f))
            print("Cache Folder cleared\n")
        else:
            print("Cache Folder does not exist\n")
