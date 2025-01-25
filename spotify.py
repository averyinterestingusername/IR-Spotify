from ir import IR, GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import credentials


GPIO.setmode(GPIO.BCM)
GPIO.setup(credentials.IR_PIN, GPIO.IN)

ir = IR(27)

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=credentials.CLIENT_ID,
                                               client_secret=credentials.CLIENT_SECRET,
                                               redirect_uri=credentials.REDIRECT_URI,
                                               scope="user-library-read,user-read-playback-state,user-modify-playback-state,user-read-private,playlist-read-collaborative,playlist-read-private"))

devices = spotify.devices()
for device in devices['devices']:
    if device['is_active']:
        device_id = device['id']

playlists = spotify.current_user_playlists(limit=50, offset=0)['items']
playlist_ids = [playlist['id'] for playlist in playlists]
playlist_index = playlist_ids.index(spotify.current_playback(market=None, additional_types=None)['context']['uri'][17:])

paused = not spotify.current_playback()['is_playing']
volume_percent = spotify.current_playback()['device']['volume_percent']
power = True


def pause_play():
    global paused
    if paused:
        spotify.start_playback(device_id=device_id)
    else:
        spotify.pause_playback(device_id=device_id)
        
    paused = not paused


def vol_up():
    global volume_percent
    volume_percent += 10
    if volume_percent > 100:
        volume_percent = 100
    spotify.volume(volume_percent, device_id=device_id)


def vol_down():
    global volume_percent
    volume_percent -= 10
    if volume_percent < 0:
        volume_percent = 0
    spotify.volume(volume_percent, device_id=device_id)
    

def next_song():
    spotify.next_track(device_id=device_id)


def prev_song():
    spotify.previous_track(device_id=device_id)
    
    
def next_playlist():
    global playlist_index
    playlist_index += 1
    playlist_index %= len(playlist_ids)
    spotify.start_playback(device_id=device_id, context_uri=f'spotify:playlist:{playlist_ids[playlist_index]}')


def prev_playlist():
    global playlist_index
    playlist_index -= 1
    playlist_index %= len(playlist_ids)
    spotify.start_playback(device_id=device_id, context_uri=f'spotify:playlist:{playlist_ids[playlist_index]}')
    
    
def stop():
    global power
    power = False
    

def nothing():
    pass


key_keys = {
    'Power': stop,
    'Function/Stop': nothing,
    'Rewind': prev_song,
    'Pause/Play': pause_play,
    'Fast Forward': next_song,
    'Vol +': vol_up,
    'Vol -': vol_down,
    'Down': next_playlist,
    'Up': prev_playlist,
    'EQ': nothing,
    'Start/Repeat': nothing,

    0: nothing,
    1: nothing,
    2: nothing,
    3: nothing,
    4: nothing,
    5: nothing,
    6: nothing,
    7: nothing,
    8: nothing,
    9: nothing,
}


if __name__ == "__main__":
    try:
        while power:
            key = ir.get_ir_key()
            
            if key is not None:
                print(key)
                key_keys[key]()
    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        GPIO.cleanup()

