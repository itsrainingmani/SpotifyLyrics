import sys, os
import json
import pprint
import azlyrics as az
import spotipy
import spotipy.util as util

from colorama import init, Fore

def load_params_and_get_token():
    params = json.load(open('client_secrets.json'))
    scope = 'user-read-currently-playing'
    auth_token = util.prompt_for_user_token(params['username'], scope, 
                        client_id=params['client_id'],
                        client_secret=params['client_secret'],
                        redirect_uri=params['redirect_uri']
                        )
    return auth_token

def main(curr_tr):
    token = load_params_and_get_token()
    if token:
        sp = spotipy.Spotify(auth=token)
        try:
            results = sp.current_user_playing_track()
            artist_name = results['item']['album']['artists'][0]['name']
            song_name = results['item']['name']
            current_progress = results['progress_ms']
            total_duration = results['item']['duration_ms']
            progress = round((current_progress/total_duration) * 100, 2)
            if song_name != curr_tr:
                lyrics = az.extract_lyrics(artist_name, song_name)
                # full_lyrics = '\n'.join(lyrics)
                print(Fore.RED + "\r{} by {}\n\n".format(song_name, artist_name), end='')
                # print(full_lyrics + '\n')
                az.pretty_print_lyrics(lyrics)
                print(Fore.GREEN + "\rProgress - {}%".ljust(20,' ').format(progress), end='')
                return song_name
            else:
                print(Fore.GREEN + "\rProgress - {}%".ljust(20, ' ').format(progress), end='')
                return song_name
        except TypeError:
            print(Fore.RED + "\rNo Track is playing", end='')
    else:
        print("Can't get token")

if __name__ == "__main__":
    init(autoreset=True)
    curr_track = ""
    while True:
        try:
            curr_track = main(curr_track)
        except KeyboardInterrupt:
            print('\b\b  \n\rShutting Down')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
