# NUS Orbital 21/22 Team PixelJump (5215)

## Game Instructions
- A and D to move left/right
- Spacebar to jump/double-jump
- M to mute all sounds and music
- Escape to pause the game

## Running the game
### Option 1 :
### Run the packaged executable
Go to [releases](https://github.com/WilsonOh/Orbital21-22-PixelJump-5215/releases/tag/v0.5.0) and follow the instructions for your OS.<br>
The packaged executables are only tested on limited hardware so there may be some problems that we have not faced.<br>
If the executable packages do not work, then the most reliable way is to run the program from source, which will be explained below.

### Option 2 :
### Running from source
1. Make sure you have `python3.10` installed. You can download and install it from https://www.python.org/downloads/
2. Clone the repo and `cd` into it
3. Install `pygame` by running `pip install pygame` to install it globally, or create a python `venv`<sup>[1]</sup> and install it there
4. If you're using a `venv`, activate it and then run `python3 src/main.py`

[1] Create a `venv` by running `python3 -m venv venv`

### Configuring Game Settings
All the configurable settings are stored in the `settings/settings.json` file in the game folder.<br>
Since the current version of `PIXELJUMP` does not support in-game settings configuration yet, the only way to adjust the game settings is to edit the `settings.json` file.
#### Screen Resolution
The game is in `1920x1080` by default as it was the resolution we had in mind when designing the game but you can change it to your liking.<br>
The screen resolution of the game can be changed by adjusting the `screen_width` and `screen_height` keys in `settings.json`
#### FPS
It is not reccomended to change the FPS as it may cause some unwanted behaviours
#### Player velocity and gravity
Feel free to mess around with the velocity and gravity of the player :smile:


### Project Poster
![project_poster](https://drive.google.com/uc?export=view&id=1aqh3d5f08MciOXuNbmsdHS0T8P3vGBgA)
