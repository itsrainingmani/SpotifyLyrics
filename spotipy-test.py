import sys, os
import pprint
import json
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
        try:
            results = sp.current_user_playing_track()
            progress = results['progress_ms']
            duration = results['item']['duration_ms']
            print("Progress seconds - ", progress/1000)
            print("Duration seconds - ", duration/1000)
            print(results['item']['name'])
        except TypeError:
            print("No Track is playing")
    else:
        print("Can't get token")

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('Shutting Down')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
