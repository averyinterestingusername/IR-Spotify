# IR-Spotify

Hello! Ever since I got an Infrared (IR) controller, I've wanted to make a project with it. After many failed ideas, I had this one, and I pursued it.

## Instructions

To make this work, you need to have
- A Raspberry Pi
- An IR controller & receiver ([the one I'm using](https://www.dfrobot.com/product-366.html))
- And an external speaker

The IR receiver gets input from the user pressing key on the controller, which the Raspberry Pi then uses to execute a command from the Spotify API.

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
