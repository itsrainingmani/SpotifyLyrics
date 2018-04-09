import sys
import pprint
import spotipy
import spotipy.util as util

SPOTIPY_CLIENT_ID='e38d35f21af14fc890865b3490ebf9b7'
SPOTIPY_CLIENT_SECRET='6ee628feba734425a81ed26b34897133'
SPOTIPY_REDIRECT_URI='http://localhost:8080'
scope = 'user-read-currently-playing'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, 
                        client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI)

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