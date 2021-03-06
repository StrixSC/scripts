#/usr/bin/env python3
import math
import quantumrandom
import os
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-d", "--directory", dest="wallpapers_dir", help="Specify directory containing the wallpaper images", metavar="DIR")

user = os.getlogin()
args = parser.parse_args()

try:
    wallpapers = os.listdir(args.wallpapers_dir)
    random_wp_num = math.floor(quantumrandom.randint(0, len(wallpapers)))
    selected_wp = args.wallpapers_dir + wallpapers[random_wp_num]
    print(selected_wp)
    os.system("DISPLAY=:0.0 /usr/bin/feh --bg-scale " + "\"" + selected_wp + "\"")
except:
    print("Specified directory is either not a directory or does not contain any image files")
