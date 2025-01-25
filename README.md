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

Then, install the package 'spotipy' on your Raspberry Pi.
- The following command should do the trick: py -m pip install spotipy --upgrade

Plug the IR receiver into your Raspberry Pi
- The wire of your IR receiver should have three pins:
- <img width="600" alt="Wire" src="https://dfimg.dfrobot.com/enshop/image/data/FIT0011/200420%20Update/53AU4166_564x376.jpg"/>

- Your Raspberry Pi's pins:
- <img width="600" alt="Raspberry Pi Pins" src="https://www.raspberrypi.com/documentation/computers/images/GPIO-Pinout-Diagram-2.png?hash=df7d7847c57a1ca6d5b2617695de6d46"/>

- Plug:
  - The red one into "5V Power",
  - The black one into "Ground",
  - And the green one into one of the many GPIO pins (remember the pin number)

Connect your external speaker to your Raspberry Pi:
- Either plub it into the audio jack,
- Or use Bluetooth.

Lastly, manipulate my files:
- Download the files from this repsitory
- Fill out the credentials.py file with
  - Your [Spotify details](https://developer.spotify.com/dashboard)
  - The GPIO pin you plugged your green wire into
- Upload your files to your Raspberry Pi (USB stick, file sharing, email... whatever suits you best)

### Running the program

Make sure the Raspberry Pi has an instance of [Spotify](https://open.spotify.com/) open (or better yet, find a way to download Spotify *), and is the active device.
- The active device is the last device that has recently played a song on Spotify.
Run the spotify.py file.
Try pressing the pause/play button on your IR controller.

Voilà! That should allow you to control the songs with your IR controller, and play the using the Raspberry Pi!

### * That was sarcastic! You can't (easily) download Spotify on Linux.
