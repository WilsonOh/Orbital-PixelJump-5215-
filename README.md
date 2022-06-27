# NUS Orbital 21/22 Team PixelJump (5215)

## Running the game
### Run the packaged executable
Go to `releases` and follow the instructions for your OS.<br>
The packaged executables are only tested on limited hardware so there may be some problems that we have not faced.<br>
The most reliable way is to run the program from source, which will be explained below.
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
The screen resolution of the game can be changed by adjusting the `screen_width` and `screen_height` keys
#### FPS
It is not reccomended to change the FPS as it may cause some unwanted behaviours
#### Player velocity and gravity
Feel free to mess around with the velocity and gravity of the player :smile:


### Project Poster
![project_poster](https://drive.google.com/uc?export=view&id=1PGN96EeY3W1sAmu5yI9t0f8UK_mXxqME)
