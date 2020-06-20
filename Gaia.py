from PIL import Image
import random

import pathlib
import sys
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget, QApplication, QDesktopWidget
from PyQt5.QtCore import Qt, QPointF, QPoint
from PyQt5 import QtCore, QtWidgets
from functools import partial
import wx

app = wx.App(False)
x, y = wx.GetDisplaySize()

pathlib.Path().absolute()

newpath = __file__.replace("Gaia.py", "")
newpath2 = newpath.replace("/", "\\")


class SpecialBG(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        # mess with border-radius, thatDarklordGuy!
        self.setStyleSheet("""
                background-image: url("""+newpath+"""img/buttons/frame2.png);
                text-align: center;
                border-radius: 50px;
                border: 1px solid rgba(237,174,28,0%);
                padding: 0px;
                """)

def exittheapp():
    sys.exit()








def gaia(value):
    global playersnumber
    playersnumber= value
    map = Image.open(newpath2+"img\map3-4empty.jpg")
    map_copy = map.copy()

    coordinates = [(940, 900), (1667, 818), (1373, 1491), (646, 1571), (209, 981), (500, 307), (1229, 226), (1957, 143), (2394, 735), (2102, 1410)]
    coordinates_scrolls = [(5015, 1500), (5245, 1500), (5475, 1500), (5705, 1500), (5935, 1500), (6165, 1500), (6395, 1500)]
    coordinates_cities =[(5096, 566)]
    coordinates_ratiles = [(5070, 681), (5320, 681), (5570, 681), (5820, 681), (6070, 681), (6320, 681)]
    coordinates_rtiles = [(5030, 992), (5280, 992), (5530, 992), (5780, 992), (6025, 992), (6275, 992), (5130, 1215), (5634, 1215), (6110, 1215)]
    coordinates_endgametiles = [(4195, 1152), (4197, 1405)]
    coordinates_roundtiles = [(3590, 880), (3685, 739), (3832, 662), (4000, 668), (4143, 755), (4220, 903)]
    roundtiles_angles = [74, 44, 14, -16, -46, -76]



    tiles = ["g01.png", "g02.png", "g03.png", "g04.png", "g05.png", "g06.png", "g07.png", "g08.png", "g09.png", "g10.png"]
    tiles_2p = ["g01.png", "g02.png", "g03.png", "g04.png", "g05-flipped.png", "g06-flipped.png", "g07-flipped.png"]
    placedtiles = []
    scroll_tiles = ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png", "09.png", "10.png"]
    r_tiles = ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png", "09.png"]
    r_a_tiles = ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png", "09.png", "10.png", "11.png", "12.png", "13.png", "14.png", "15.png"]
    round_tiles = ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png", "07.png", "08.png", "09.png", "10.png"]
    endgame_tiles = ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png"]
    cities_tiles = ["01.png", "02.png", "03.png", "04.png", "05.png", "06.png"]

    k = 0



    for i in range(3+int(playersnumber)):
        a = random.choice(scroll_tiles)
        tile = Image.open(newpath2+"img\scrolls" + "\\" + a)
        map_copy.paste(tile, coordinates_scrolls[i], tile)
        scroll_tiles.remove(a)

    a = random.choice(cities_tiles)
    tile = Image.open(newpath2+"img\cities" + "\\" + a)
    map_copy.paste(tile, coordinates_cities[0], tile)

    for i in range(6):
        a = random.choice(round_tiles)
        tile = Image.open(newpath2+"img"+"\\"+"roundscores" + "\\" + a)
        rotated = tile.rotate(roundtiles_angles[i])
        map_copy.paste(rotated, coordinates_roundtiles[i], rotated)
        round_tiles.remove(a)

    for i in range(6):
        a = random.choice(r_a_tiles)
        tile = Image.open(newpath2+"img"+"\\"+"advresearchtiles" + "\\" + a)
        map_copy.paste(tile, coordinates_ratiles[i], tile)
        r_a_tiles.remove(a)

    for i in range(2):
        a = random.choice(endgame_tiles)
        tile = Image.open(newpath2+"img"+"\\"+"finalscoring" + "\\" + a)
        map_copy.paste(tile, coordinates_endgametiles[i], tile)
        endgame_tiles.remove(a)

    for i in range(9):
        a = random.choice(r_tiles)
        tile = Image.open(newpath2+"img"+"\\"+"researchtiles" + "\\" + a)
        map_copy.paste(tile, coordinates_rtiles[i], tile)
        r_tiles.remove(a)


    if(int(playersnumber) == 2):
        match_numbers = 0
        while(k != 7):
            a = random.choice(tiles_2p)
            if(k == 0):
                tile = Image.open(newpath2+"img" + "\\" + a)
                placedtiles.append(a)
                map_copy.paste(tile, coordinates[k], tile)
                tiles_2p.remove(a)
                k += 1
            else:
                if(k == 1):
                    if(a == "g01.png"):
                        if(placedtiles[0] == "g02.png"):
                            match_numbers += 1
                        else:
                            tile = Image.open(newpath2+"img" + "\\" + a)
                            placedtiles.append(a)
                            map_copy.paste(tile, coordinates[k], tile)
                            tiles_2p.remove(a)
                            k += 1
                    else:
                        tile = Image.open(newpath2+"img" + "\\" + a)
                        placedtiles.append(a)
                        map_copy.paste(tile, coordinates[k], tile)
                        tiles_2p.remove(a)
                        k += 1
                else:
                    if(k == 2):
                        if(a == "g02.png"):
                            if (placedtiles[0] == "g01.png"):
                                match_numbers += 1
                            else:
                                tile = Image.open(newpath2+"img" + "\\" + a)
                                placedtiles.append(a)
                                map_copy.paste(tile, coordinates[k], tile)
                                tiles_2p.remove(a)
                                k += 1
                        else:
                            tile = Image.open(newpath2+"img" + "\\" + a)
                            placedtiles.append(a)
                            map_copy.paste(tile, coordinates[k], tile)
                            tiles_2p.remove(a)
                            k += 1
                    else:
                        if(k == 3):
                            if(a == "g02.png"):
                                    if (placedtiles[2] == "g01.png"):
                                        match_numbers += 1
                                    else:
                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                        placedtiles.append(a)
                                        map_copy.paste(tile, coordinates[k], tile)
                                        tiles_2p.remove(a)
                                        k += 1
                            else:
                                tile = Image.open(newpath2+"img" + "\\" + a)
                                placedtiles.append(a)
                                map_copy.paste(tile, coordinates[k], tile)
                                tiles_2p.remove(a)
                                k += 1
                        else:
                            if(k == 4):
                                if (a == "g02.png"):
                                    if (placedtiles[0] == "g01.png"):
                                        match_numbers += 1
                                    else:
                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                        placedtiles.append(a)
                                        map_copy.paste(tile, coordinates[k], tile)
                                        tiles_2p.remove(a)
                                        k += 1
                                else:
                                    if (a == "g01.png"):
                                        if (placedtiles[3] == "g02.png"):
                                            match_numbers += 1
                                        else:
                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                            placedtiles.append(a)
                                            map_copy.paste(tile, coordinates[k], tile)
                                            tiles_2p.remove(a)
                                            k += 1
                                    else:
                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                        placedtiles.append(a)
                                        map_copy.paste(tile, coordinates[k], tile)
                                        tiles_2p.remove(a)
                                        k += 1
                            else:
                                if(k == 5):
                                    if (a == "g01.png"):
                                        if (placedtiles[0] == "g02.png"):
                                            match_numbers += 1
                                        else:
                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                            placedtiles.append(a)
                                            map_copy.paste(tile, coordinates[k], tile)
                                            tiles_2p.remove(a)
                                            k += 1
                                    else:
                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                        placedtiles.append(a)
                                        map_copy.paste(tile, coordinates[k], tile)
                                        tiles_2p.remove(a)
                                        k += 1
                                else:
                                    if(k == 6):
                                        if (a == "g01.png"):
                                            if (placedtiles[5] == "g02.png"):
                                                match_numbers += 1
                                                k = 0
                                                placedtiles.append(a)
                                                tiles_2p.remove(a)
                                                tiles_2p = placedtiles.copy()
                                                del placedtiles[:]
                                            else:
                                                if (placedtiles[1] == "g02.png"):
                                                    match_numbers += 1
                                                    k = 0
                                                    placedtiles.append(a)
                                                    tiles_2p.remove(a)
                                                    tiles_2p = placedtiles.copy()
                                                    del placedtiles[:]
                                                else:
                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                    placedtiles.append(a)
                                                    map_copy.paste(tile, coordinates[k], tile)
                                                    tiles_2p.remove(a)
                                                    k += 1
                                        else:

                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                            placedtiles.append(a)
                                            map_copy.paste(tile, coordinates[k], tile)
                                            tiles_2p.remove(a)
                                            k += 1

        map_copy.save(newpath2+"generatedmap.png")
        map_copy.show()

    else:
        match_numbers = 0
        while (k != 10):
            a = random.choice(tiles)
            if(k == 0):
                tile = Image.open(newpath2+"img" + "\\" + a)
                placedtiles.append(a)
                map_copy.paste(tile, coordinates[k], tile)
                tiles.remove(a)
                k += 1
            else:
                if(k == 1):
                    if(a == "g04.png"):
                        if(placedtiles[0] == "g09.png"):
                            match_numbers += 1
                        else:
                            tile = Image.open(newpath2+"img" + "\\" + a)
                            placedtiles.append(a)
                            map_copy.paste(tile, coordinates[k], tile)
                            tiles.remove(a)
                            k += 1
                    else:
                        if(a == "g01.png"):
                            if (placedtiles[0] == "g02.png"):
                                match_numbers += 1
                            else:
                                tile = Image.open(newpath2+"img" + "\\" + a)
                                placedtiles.append(a)
                                map_copy.paste(tile, coordinates[k], tile)
                                tiles.remove(a)
                                k += 1
                        else:
                            if(a == "g10.png"):
                                if (placedtiles[0] == "g04.png"):
                                    match_numbers += 1
                                else:
                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                    placedtiles.append(a)
                                    map_copy.paste(tile, coordinates[k], tile)
                                    tiles.remove(a)
                                    k += 1
                            else:
                                tile = Image.open(newpath2+"img" + "\\" + a)
                                placedtiles.append(a)
                                map_copy.paste(tile, coordinates[k], tile)
                                tiles.remove(a)
                                k += 1

                else:
                    if (k == 2):
                        if (a == "g08.png"):
                            if (placedtiles[1] == "g10.png"):
                                match_numbers += 1
                            else:
                                if(placedtiles[0] == "g04.png"):
                                    match_numbers += 1
                                else:
                                    if (placedtiles[1] == "g03.png"):
                                        match_numbers += 1
                                    else:
                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                        placedtiles.append(a)
                                        map_copy.paste(tile, coordinates[k], tile)
                                        tiles.remove(a)
                                        k += 1
                        else:
                            if (a == "g09.png"):
                                if (placedtiles[0] == "g01.png"):
                                    match_numbers += 1
                                else:
                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                    placedtiles.append(a)
                                    map_copy.paste(tile, coordinates[k], tile)
                                    tiles.remove(a)
                                    k += 1
                            else:
                                if (a == "g02.png"):
                                    if (placedtiles[0] == "g01.png"):
                                        match_numbers += 1
                                    else:
                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                        placedtiles.append(a)
                                        map_copy.paste(tile, coordinates[k], tile)
                                        tiles.remove(a)
                                        k += 1
                                else:
                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                    placedtiles.append(a)
                                    map_copy.paste(tile, coordinates[k], tile)
                                    tiles.remove(a)
                                    k += 1
                    else:
                        if (k == 3):
                            if (a == "g02.png"):
                                if (placedtiles[2] == "g01.png"):
                                    match_numbers += 1
                                else:
                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                    placedtiles.append(a)
                                    map_copy.paste(tile, coordinates[k], tile)
                                    tiles.remove(a)
                                    k += 1
                            else:
                                if (a == "g09.png"):
                                    if (placedtiles[2] == "g04.png"):
                                        match_numbers += 1
                                    else:
                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                        placedtiles.append(a)
                                        map_copy.paste(tile, coordinates[k], tile)
                                        tiles.remove(a)
                                        k += 1
                                else:
                                    if (a == "g04.png"):
                                        if (placedtiles[2] == "g10.png"):
                                            match_numbers += 1
                                        else:
                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                            placedtiles.append(a)
                                            map_copy.paste(tile, coordinates[k], tile)
                                            tiles.remove(a)
                                            k += 1
                                    else:
                                        if (a == "g08.png"):
                                            if (placedtiles[0] == "g10.png"):
                                                match_numbers += 1
                                            else:
                                                if (placedtiles[0] == "g03.png"):
                                                    match_numbers += 1
                                                else:
                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                    placedtiles.append(a)
                                                    map_copy.paste(tile, coordinates[k], tile)
                                                    tiles.remove(a)
                                                    k += 1
                                        else:
                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                            placedtiles.append(a)
                                            map_copy.paste(tile, coordinates[k], tile)
                                            tiles.remove(a)
                                            k += 1
                        else:
                            if (k == 4):
                                if (a == "g02.png"):
                                    if (placedtiles[0] == "g01.png"):
                                        match_numbers += 1
                                    else:
                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                        placedtiles.append(a)
                                        map_copy.paste(tile, coordinates[k], tile)
                                        tiles.remove(a)
                                        k += 1
                                else:
                                    if (a == "g09.png"):
                                        if (placedtiles[0] == "g04.png"):
                                            match_numbers += 1
                                        else:
                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                            placedtiles.append(a)
                                            map_copy.paste(tile, coordinates[k], tile)
                                            tiles.remove(a)
                                            k += 1
                                    else:
                                        if (a == "g04.png"):
                                            if (placedtiles[0] == "g10.png"):
                                                match_numbers += 1
                                            else:
                                                if (placedtiles[3] == "g08.png"):
                                                    match_numbers += 1
                                                else:
                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                    placedtiles.append(a)
                                                    map_copy.paste(tile, coordinates[k], tile)
                                                    tiles.remove(a)
                                                    k += 1
                                        else:
                                            if (a == "g01.png"):
                                                if (placedtiles[3] == "g02.png"):
                                                    match_numbers += 1
                                                else:
                                                    if(placedtiles[3] == "g09.png"):
                                                        match_numbers += 1
                                                    else:
                                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                                        placedtiles.append(a)
                                                        map_copy.paste(tile, coordinates[k], tile)
                                                        tiles.remove(a)
                                                        k += 1
                                            else:
                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                placedtiles.append(a)
                                                map_copy.paste(tile, coordinates[k], tile)
                                                tiles.remove(a)
                                                k += 1
                            else:
                                if(k == 5):
                                    if (a == "g01.png"):
                                        if (placedtiles[0] == "g02.png"):
                                            match_numbers += 1
                                        else:
                                            if (placedtiles[0] == "g09.png"):
                                                match_numbers += 1
                                            else:
                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                placedtiles.append(a)
                                                map_copy.paste(tile, coordinates[k], tile)
                                                tiles.remove(a)
                                                k += 1
                                    else:
                                        if (a == "g04.png"):
                                            if (placedtiles[0] == "g08.png"):
                                                match_numbers += 1
                                            else:
                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                placedtiles.append(a)
                                                map_copy.paste(tile, coordinates[k], tile)
                                                tiles.remove(a)
                                                k += 1
                                        else:
                                            if (a == "g10.png"):
                                                if (placedtiles[4] == "g08.png"):
                                                    match_numbers += 1
                                                else:
                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                    placedtiles.append(a)
                                                    map_copy.paste(tile, coordinates[k], tile)
                                                    tiles.remove(a)
                                                    k += 1
                                            else:
                                                if (a == "g03.png"):
                                                    if (placedtiles[4] == "g08.png"):
                                                        match_numbers += 1
                                                    else:
                                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                                        placedtiles.append(a)
                                                        map_copy.paste(tile, coordinates[k], tile)
                                                        tiles.remove(a)
                                                        k += 1
                                                else:
                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                    placedtiles.append(a)
                                                    map_copy.paste(tile, coordinates[k], tile)
                                                    tiles.remove(a)
                                                    k += 1
                                else:
                                    if(k == 6):
                                        if (a == "g04.png"):
                                            if (placedtiles[5] == "g09.png"):
                                                match_numbers += 1
                                            else:
                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                placedtiles.append(a)
                                                map_copy.paste(tile, coordinates[k], tile)
                                                tiles.remove(a)
                                                k += 1
                                        else:
                                            if (a == "g01.png"):
                                                if (placedtiles[5] == "g02.png"):
                                                    match_numbers += 1
                                                else:
                                                    if (placedtiles[1] == "g09.png"):
                                                        match_numbers += 1
                                                    else:
                                                        if (placedtiles[1] == "g02.png"):
                                                            match_numbers += 1
                                                        else:
                                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                                            placedtiles.append(a)
                                                            map_copy.paste(tile, coordinates[k], tile)
                                                            tiles.remove(a)
                                                            k += 1
                                            else:
                                                if (a == "g10.png"):
                                                    if (placedtiles[5] == "g04.png"):
                                                        match_numbers += 1
                                                    else:
                                                        if (placedtiles[0] == "g08.png"):
                                                            match_numbers += 1
                                                        else:
                                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                                            placedtiles.append(a)
                                                            map_copy.paste(tile, coordinates[k], tile)
                                                            tiles.remove(a)
                                                            k += 1
                                                else:
                                                    if (a == "g03.png"):
                                                        if (placedtiles[0] == "g08.png"):
                                                            match_numbers += 1
                                                        else:
                                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                                            placedtiles.append(a)
                                                            map_copy.paste(tile, coordinates[k], tile)
                                                            tiles.remove(a)
                                                            k += 1
                                                    else:
                                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                                        placedtiles.append(a)
                                                        map_copy.paste(tile, coordinates[k], tile)
                                                        tiles.remove(a)
                                                        k += 1
                                    else:
                                        if(k == 7):
                                            if (a == "g04.png"):
                                                if (placedtiles[6] == "g09.png"):
                                                    match_numbers += 1
                                                else:
                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                    placedtiles.append(a)
                                                    map_copy.paste(tile, coordinates[k], tile)
                                                    tiles.remove(a)
                                                    k += 1
                                            else:
                                                if (a == "g01.png"):
                                                    if (placedtiles[6] == "g02.png"):
                                                        match_numbers += 1
                                                    else:
                                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                                        placedtiles.append(a)
                                                        map_copy.paste(tile, coordinates[k], tile)
                                                        tiles.remove(a)
                                                        k += 1
                                                else:
                                                    if (a == "g10.png"):
                                                        if (placedtiles[6] == "g04.png"):
                                                            match_numbers += 1
                                                        else:
                                                            if (placedtiles[6] == "g08.png"):
                                                                match_numbers += 1
                                                            else:
                                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                                placedtiles.append(a)
                                                                map_copy.paste(tile, coordinates[k], tile)
                                                                tiles.remove(a)
                                                                k += 1
                                                    else:
                                                        if (a == "g03.png"):
                                                            if (placedtiles[1] == "g08.png"):
                                                                match_numbers += 1
                                                            else:
                                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                                placedtiles.append(a)
                                                                map_copy.paste(tile, coordinates[k], tile)
                                                                tiles.remove(a)
                                                                k += 1
                                                        else:
                                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                                            placedtiles.append(a)
                                                            map_copy.paste(tile, coordinates[k], tile)
                                                            tiles.remove(a)
                                                            k += 1
                                        else:
                                            if(k == 8):
                                                if (a == "g04.png"):
                                                    if (placedtiles[1] == "g09.png"):
                                                        match_numbers += 1
                                                    else:
                                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                                        placedtiles.append(a)
                                                        map_copy.paste(tile, coordinates[k], tile)
                                                        tiles.remove(a)
                                                        k += 1
                                                else:
                                                    if (a == "g01.png"):
                                                        if (placedtiles[1] == "g02.png"):
                                                            match_numbers += 1
                                                        else:
                                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                                            placedtiles.append(a)
                                                            map_copy.paste(tile, coordinates[k], tile)
                                                            tiles.remove(a)
                                                            k += 1
                                                    else:
                                                        if (a == "g10.png"):
                                                            if (placedtiles[1] == "g04.png"):
                                                                match_numbers += 1
                                                            else:
                                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                                placedtiles.append(a)
                                                                map_copy.paste(tile, coordinates[k], tile)
                                                                tiles.remove(a)
                                                                k += 1
                                                        else:
                                                            if (a == "g02.png"):
                                                                if (placedtiles[7] == "g01.png"):
                                                                    match_numbers += 1
                                                                else:
                                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                                    placedtiles.append(a)
                                                                    map_copy.paste(tile, coordinates[k], tile)
                                                                    tiles.remove(a)
                                                                    k += 1
                                                            else:
                                                                if (a == "g09.png"):
                                                                    if (placedtiles[7] == "g01.png"):
                                                                        match_numbers += 1
                                                                    else:
                                                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                                                        placedtiles.append(a)
                                                                        map_copy.paste(tile, coordinates[k], tile)
                                                                        tiles.remove(a)
                                                                        k += 1
                                                                else:
                                                                    if (a == "g08.png"):
                                                                        if (placedtiles[7] == "g04.png"):
                                                                            match_numbers += 1
                                                                        else:
                                                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                                                            placedtiles.append(a)
                                                                            map_copy.paste(tile, coordinates[k], tile)
                                                                            tiles.remove(a)
                                                                            k += 1
                                                                    else:
                                                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                                                        placedtiles.append(a)
                                                                        map_copy.paste(tile, coordinates[k], tile)
                                                                        tiles.remove(a)
                                                                        k += 1
                                            else:
                                                if(k == 9):
                                                    if (a == "g08.png"):
                                                        if (placedtiles[8] == "g10.png"):
                                                            k = 0
                                                            placedtiles.append(a)
                                                            tiles.remove(a)
                                                            tiles = placedtiles.copy()
                                                            del placedtiles[:]

                                                        else:
                                                            if (placedtiles[1] == "g04.png"):
                                                                k = 0
                                                                placedtiles.append(a)
                                                                tiles.remove(a)
                                                                tiles = placedtiles.copy()
                                                                del placedtiles[:]
                                                            else:
                                                                if (placedtiles[8] == "g03.png"):
                                                                    k = 0
                                                                    placedtiles.append(a)
                                                                    tiles.remove(a)
                                                                    tiles = placedtiles.copy()
                                                                    del placedtiles[:]
                                                                else:
                                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                                    placedtiles.append(a)
                                                                    map_copy.paste(tile, coordinates[k], tile)
                                                                    tiles.remove(a)
                                                                    k += 1
                                                    else:
                                                        if (a == "g09.png"):
                                                            if (placedtiles[1] == "g01.png"):
                                                                k = 0
                                                                placedtiles.append(a)
                                                                tiles.remove(a)
                                                                tiles = placedtiles.copy()
                                                                del placedtiles[:]
                                                            else:
                                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                                placedtiles.append(a)
                                                                map_copy.paste(tile, coordinates[k], tile)
                                                                tiles.remove(a)
                                                                k += 1
                                                        else:
                                                            if (a == "g02.png"):
                                                                if (placedtiles[1] == "g01.png"):
                                                                    k = 0
                                                                    placedtiles.append(a)
                                                                    tiles.remove(a)
                                                                    tiles = placedtiles.copy()
                                                                    del placedtiles[:]
                                                                else:
                                                                    tile = Image.open(newpath2+"img" + "\\" + a)
                                                                    placedtiles.append(a)
                                                                    map_copy.paste(tile, coordinates[k], tile)
                                                                    tiles.remove(a)
                                                                    k += 1
                                                            else:
                                                                if (a == "g10.png"):
                                                                    if (placedtiles[2] == "g04.png"):
                                                                        k = 0
                                                                        placedtiles.append(a)
                                                                        tiles.remove(a)
                                                                        tiles = placedtiles.copy()
                                                                        del placedtiles[:]
                                                                    else:
                                                                        tile = Image.open(newpath2+"img" + "\\" + a)
                                                                        placedtiles.append(a)
                                                                        map_copy.paste(tile, coordinates[k], tile)
                                                                        tiles.remove(a)
                                                                        k += 1
                                                                else:
                                                                    if (a == "g04.png"):
                                                                        if (placedtiles[2] == "g09.png"):
                                                                            k = 0
                                                                            placedtiles.append(a)
                                                                            tiles.remove(a)
                                                                            tiles = placedtiles.copy()
                                                                            del placedtiles[:]
                                                                        else:
                                                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                                                            placedtiles.append(a)
                                                                            map_copy.paste(tile, coordinates[k], tile)
                                                                            tiles.remove(a)
                                                                            k += 1
                                                                    else:
                                                                        if (a == "g01.png"):
                                                                            if (placedtiles[2] == "g02.png"):
                                                                                k = 0
                                                                                placedtiles.append(a)
                                                                                tiles.remove(a)
                                                                                tiles = placedtiles.copy()
                                                                                del placedtiles[:]
                                                                            else:
                                                                                tile = Image.open(newpath2+"img" + "\\" + a)
                                                                                placedtiles.append(a)
                                                                                map_copy.paste(tile, coordinates[k], tile)
                                                                                tiles.remove(a)
                                                                                k += 1
                                                                        else:
                                                                            tile = Image.open(newpath2+"img" + "\\" + a)
                                                                            placedtiles.append(a)
                                                                            map_copy.paste(tile, coordinates[k], tile)
                                                                            tiles.remove(a)
                                                                            k += 1
        map_copy.save(newpath2+"generatedmap.png")
        map_copy.show()

class SimpleRoundedCorners(QWidget):
    def __init__(self):
        super(SimpleRoundedCorners, self).__init__()

        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def initUI(self):
        winwidth = 628
        winheight = 285
        VBox = QVBoxLayout()
        roundyround = SpecialBG(self)
        VBox.addWidget(roundyround)



        self.setLayout(VBox)
        # transparency cannot be set for window BG in style sheets, so...
        # self.setWindowOpacity(0.5)
        self.setWindowFlags(
            Qt.FramelessWindowHint  # hides the window controls
            #| Qt.WindowStaysOnTopHint  # forces window to top... maybe

        )
        # alternative way of making base window transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 100% transparent
        pushButton = QtWidgets.QPushButton(self)
        pushButton.setGeometry(QtCore.QRect(80, 70, 130, 130))
        pushButton.setStyleSheet("#button1{\n"
                                 "background-image: url("+newpath+"img/buttons/button2p.png);\n"


                                 "border-radius: 90x;\n"
                                 "border: 1px solid rgba(237,174,28,0%);\n"
                                 "background-repeat: none;\n"
                                 "}"
                                 "#button1:pressed\n"
                                 "{\n"
                                 "background-image: url("+newpath+"img/buttons/button2p-pushed.png);\n"
                                 "}")
        pushButton.setObjectName("button1")
        pushButton.clicked.connect(partial(gaia, 2))
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(255, 70, 130, 130))
        self.pushButton_2.setStyleSheet("#button2{\n"
                                        "background-image: url("+newpath+"img/buttons/button3p.png);\n"


                                        "border-radius: 90x;\n"
                                        "border: 1px solid rgba(237,174,28,0%);\n"
                                        "background-repeat: none;\n"
                                        "}"
                                        "#button2:pressed\n"
                                        "{\n"
                                        "background-image: url("+newpath+"img/buttons/button3p-pushed.png);\n"
                                        "}")
        self.pushButton_2.setObjectName("button2")
        self.pushButton_2.clicked.connect(partial(gaia, 3))
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 70, 130, 130))
        self.pushButton_3.setStyleSheet("#button3{\n"
                                        "background-image: url("+newpath+"img/buttons/button4p.png);\n"


                                        "border-radius: 90x;\n"
                                        "border: 1px solid rgba(237,174,28,0%);\n"
                                        "background-repeat: none;\n"
                                        "}"
                                        "#button3:pressed\n"
                                        "{\n"
                                        "background-image: url("+newpath+"img/buttons/button4p-pushed.png);\n"
                                        "}")
        self.pushButton_3.setObjectName("button3")
        self.pushButton_3.clicked.connect(partial(gaia, 4))
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 38, 130, 130))
        self.pushButton_4.setStyleSheet("#button3{\n"
                                        "background-image: url("+newpath+"img/buttons/buttonexit.png);\n"


                                        "border-radius: 90x;\n"
                                        "border: 1px solid rgba(237,174,28,0%);\n"
                                        "background-repeat: none;\n"
                                        "}"
                                        "#button3:pressed\n"
                                        "{\n"
                                        "background-image: url("+newpath+"img/buttons/buttonexit-pushed.png);\n"
                                        "}")
        self.pushButton_4.setObjectName("button3")
        self.pushButton_4.clicked.connect(exittheapp)
        px = x * 1.25 / 2 - winwidth / 2
        py = y * 1.25 / 2 - winheight / 2
        print(x)
        print(y)
        self.setGeometry(px, py, winwidth, winheight)
        self.setWindowTitle('Simple Rounded Corners')
        self.show()


def main():
    app = QApplication(sys.argv)
    merry = SimpleRoundedCorners()
    sys.exit(app.exec_())

if __name__ == '__main__':
     main()

root.mainloop()
