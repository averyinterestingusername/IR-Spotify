# IR-Spotify

Hello! Ever since I got an Infrared (IR) controller, I've wanted to make a project with it. 

After a while (and many failed ideas!), I got the idea to make this, so I did.

### Short Input

I spent countless hours trying to find out how to let my Raspberry Pi get input from my IR controller, by reading the data received by the IR receiver. This ended up taking so long because simply reading the value on the signal pin (which is, of course, the first thing I tried) led to gibberish, and anything I found online was very vague and only applicable to models other than mine.

Eventually, I decided to revisit the webpage of the supplier I got the IR kit from (namely [Core Electronics](https://core-electronics.com.au/ir-kit-for-arduino.html)). From there, I espied a link which might help me further, and followed it to the original manufacturer ([DFRobot](https://www.dfrobot.com/product-366.html)). I visited what I thought might prove to be most fruitful, their wiki, to see if I could glean anything there.

I could, and found some vital sample code on the following [wiki entry](https://wiki.dfrobot.com/IR_Kit_SKU_DFR0107_). However, it was written in Arduino C++ (Does it have a specific name?). Great. 

I proceded to translate the c++ code into micropython. An arduous task, indeed, and when I was finished... it still didn't recognise the keypresses on the IR controller. It turned out, and this wasn't explained anywhere, that the keys were misconfigured in the code, and they didn't match up with my kit. As such, when the signals were decoded, the program didn't recognise them as a known key, and threw an error. Eventually, I figured out I could print the value the program did receive, and then manually recalibrate each key to the actual value received. Once I had managed that, the program actually worked! Since it was ugly, I also cleaned it up, and turned it into a class. Finally, I was on track to hook it up to Spotify.

Which I did (I mean, what did you expect?).

## Instructions

To make this work, you need to have
- A Raspberry Pi
- An IR controller & receiver ([the one I'm using](https://www.dfrobot.com/product-366.html))
- And an external speaker

The IR receiver gets input from the user pressing key on the controller, which the Raspberry Pi then uses to execute a command from the Spotify API. 
- Different buttons on the IR controller transmit signals at different frequencies, which the receiver can pick up on.
- These different frequencies are read and decoded by my program running on the Raspberry Pi
- Using these decoded values, different things can be done; In my project, they're used to determine how the music should be manipulated.
- The Raspberry Pi uses the decoded values to execute a command from the Spotify API, which then affects the music. Examples include:
  - Pausing / Playing the music
  - Changing the volume
  - Skipping a song or rewinding to a previous one
  - Changing playlists saved on your Spotify account

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
- Upload your files to your Raspberry Pi (USB stick, ssh, file sharing, email... whatever suits you best)

### Running the program

Before running the program:
- Make sure the Raspberry Pi has an instance of [Spotify](https://open.spotify.com/) open (or better yet, find a way to download Spotify *), and is the active device.
  - The active device is the last device that has recently played a song on Spotify.

Then:
- Run the spotify.py file.
- Try pressing the pause/play button on your IR controller.

Voilà! That should allow you to control the songs with your IR controller, and play the using the Raspberry Pi!

### * That was sarcastic! You can't (easily) download Spotify on Linux. 

(Sorry, I spent a long time agonising over that fact.)
