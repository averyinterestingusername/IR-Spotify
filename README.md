# IR-Spotify

Hello! Ever since I got an Infrared (IR) controller, I've wanted to make a project with it. At first I thought of 

## Instructions

To make this work, you need a Raspberry Pi, an IR controller & receiver, and an external speaker. The Raspberry Pi gets input from the IR receiver (which itself gets input from the user pressing keys on the IR controller), and uses the Spotify API to execute a command based on the input.

### Setup

Follow the following [guide](https://github.com/spotipy-dev/spotipy/blob/2.22.1/TUTORIAL.md) until Step 2. to start using the Spotify API.

infrared im using https://www.dfrobot.com/product-366.html

Then, manipulate my files:
- Download the files from this repsitory
- Fill out the credentials.py file
- Upload your files to your Raspberry Pi (USB stick, file sharing, email... whatever suits you best)

Install the package 'Spotipy' on your Raspberry Pi
Plug the IR receiver into your raspi (wiring)
Connect a speaker
have an instace of spotify open

### Running the program

Make sure the Raspberry Pi has an instance of [Spotify](https://open.spotify.com/) open, and is the active device*
Run the spotify.py file
Try pressing the pause/play button.

Voilà! That should allow you to control the songs with your IR controller, and play the using the Raspberry Pi!

*A device becomes active to Spotify when they were the last device that has played a song, and that hasn't been too long ago.
