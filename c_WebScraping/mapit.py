#!/usr/bin/env python
import webbrowser
import sys
import pyperclip

sys.argv  # ["mapit.py", "870", "Valencia", "St."]

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open("https://www.google.co.th/maps/place/" + address)
