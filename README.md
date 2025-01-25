# IR-Spotify

Hello! Ever since I got an Infrared (IR) controller, I've wanted to make a project with it. After many failed ideas, I had this one, and I pursued it.

## Instructions

To make this work, you need to have
- A Raspberry Pi
- An IR controller & receiver ([the one I'm using](https://www.dfrobot.com/product-366.html))
- And an external speaker

The IR receiver gets input from the user pressing key on the controller, which the Raspberry Pi then uses to execute a command from the Spotify API.

### Setup

Follow Step 1 of [this guide](https://github.com/spotipy-dev/spotipy/blob/2.22.1/TUTORIAL.md) to start using the Spotify API.

Then, manipulate my files:
- Download the files from this repsitory
- Fill out the credentials.py file
- Upload your files to your Raspberry Pi (USB stick, file sharing, email... whatever suits you best)

Install the package 'spotipy' on your Raspberry Pi.
- The following command should do the trick: py -m pip install spotipy --upgrade

Plug the IR receiver into your Raspberry Pi
- The wire of your IR receiver should have three pins:
<img width="600" alt="Wire" src="https://dfimg.dfrobot.com/enshop/image/data/FIT0011/200420%20Update/53AU4166_564x376.jpg"/>

- The red one needs to be plugged into power, the black one into ground, and lastly, the green one into some pin.
<img width="600" alt="Raspberry Pi Pins" src="https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png?hash=df7d7847c57a1ca6d5b2617695de6d46"/>

Connect your external speaker, either by plugging it into the audio jack, or by bluetooth.

### Running the program

Make sure the Raspberry Pi has an instance of [Spotify](https://open.spotify.com/) open, and is the active device*
Run the spotify.py file
Try pressing the pause/play button.

Voilà! That should allow you to control the songs with your IR controller, and play the using the Raspberry Pi!

*A device becomes active to Spotify when they were the last device that has played a song, and that hasn't been too long ago.
