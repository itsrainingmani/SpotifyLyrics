import sys, os
import json
import pprint
import azlyrics as az
import spotipy
import spotipy.util as util

def load_params_and_get_token():
    params = json.load(open('client_secrets.json'))
    scope = 'user-read-currently-playing'
    auth_token = util.prompt_for_user_token(params['username'], scope, 
                        client_id=params['client_id'],
                        client_secret=params['client_secret'],
                        redirect_uri=params['redirect_uri']
                        )
    return auth_token

def main():
    token = load_params_and_get_token()
    if token:
        sp = spotipy.Spotify(auth=token)
        curr_track = ""
        try:
            results = sp.current_user_playing_track()
            artist_name = results['item']['album']['artists'][0]['name']
            song_name = results['item']['name']
            if song_name != curr_track:
                curr_track = song_name
                lyrics = az.extract_lyrics(artist_name, song_name)
                full_lyrics = lyrics.join('\n')
                print(full_lyrics, end='')
            else:
                pass
            # current_progress = results['progress_ms']
            # total_duration = results['item']['duration_ms']
            # progress = round((current_progress/total_duration) * 100, 2)
            # print("\r{} by {} - {}%".ljust(50,' ').format(song_name, artist_name, progress), end='')
        except TypeError:
            print("\rNo Track is playing", end='')
    else:
        print("Can't get token")

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('\b\b  \n\rShutting Down')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
