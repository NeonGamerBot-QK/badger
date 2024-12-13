import badger2040
import time
import badger_os
import jpegdec
import os
import re
# Global Constants
# Measurements are in pixels
WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

# PNG images are not supported on the Universe 2023 badge.
# Enable this flag to allow this app to run on those badges.
BACK_COMPAT_MODE = False

LEFT_PADDING = 7
NAME_HEIGHT = 45
LASTNAME_HEIGHT = 30
DETAILS_HEIGHT = 18
LINE_SPACING = 2
DETAILS_TEXT_SIZE = 2

BADGE_PATH = "/badges/badge.txt"

FONTS = ["bitmap8", "serif", "sans", "gothic"]
THICKNESSES = [1, 4, 4, 2]
SIZE_ADJ = [1, 0.3, 0.3, 0.3]

# Will be replaced with badge.txt
# "Universe 2024", first_name, lastname_name, company, title, pronouns to the file on separate lines.
DEFAULT_TEXT = """Counterspell :D
Saahil Dutta
saahild.com
he/him
i
d
k
"""

badger = badger2040.Badger2040()
print("Badger :3")
def think():
    badger.led(25)
    time.sleep(1)
    badger.led(-100)

def reset_screen():
    badger.set_pen(255)
    badger.clear()
    badger.update()


reset_screen()
# Call halt in a loop, on battery this switches off power.
# On USB, the app will exit when A+C is pressed because the launcher picks that up.
while True:
    badger.keepalive()
    badger.halt()