# ourgaiaprojectgames

This is my first app made using Python 3.7

The program is a setup generator for the Gaia Project boardgame i'm playing with friends. It promts you to choose the number of players then generates and returns an image containing the game setup for the choosen number of players.

It uses image manipulation (Pillow) to randomly arrange the various game tiles (map tiles, research tiles, round tiles etc.) into a full setup.
I also made a nifty minimal interface using PyQt5.

If you want to try it and tweak with the code, you can  download Gaia.py and the img folder and run it by yourself (make sure to install Pillow, PyQt5 and pathlib libraries).

Alternatively, you can just download the package with the .exe file from the link bellow and run Gaia.exe directly from there. https://drive.google.com/drive/folders/18odQu_yPSeRHY3FZwBQ_vsbz7W-U1LJu?usp=sharing


23.06.2020 Update
- The code had a problem as you couldn't run it on linux because it was using Windows separator "\" in paths. Replaced every \ with os.path.sep. Should work fine now.
- Replaced wxPython lib with tkinter for getting the screen size
