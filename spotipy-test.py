import sys
import pprint
import json
import spotipy
import spotipy.util as util

params = json.load(open('client_secrets.json'))
scope = 'user-read-currently-playing'

# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()

token = util.prompt_for_user_token(params['username'], scope, 
                        client_id=params['client_id'],
                        client_secret=params['client_secret'],
                        redirect_uri=params['redirect_uri']
                        )

# print(spotipy.VERSION)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_playing_track()
    progress = results['progress_ms']
    duration = results['item']['duration_ms']
    print("Progress seconds - ", progress/1000)
    print("Duration seconds - ", duration/1000)
    pprint.pprint(results['item']['name'])
    
else:
    print("Can't get token for", username)