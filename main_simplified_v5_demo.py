import board
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import touchio

# The built-in demo that the board came with, but I stripped out a bunch of the
# examples I wasn't going to use, like the audio and servo motor sections.

# One pixel connected internally!
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Capacitive touch on A2
touch = touchio.TouchIn(board.A2)

######################### HELPERS ##############################

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]

######################### MAIN LOOP ##############################

i = 0
while True:
  # spin internal LED around! autoshow is on
  dot[0] = wheel(i & 255)
  i = (i+1) % 256  # run from 0 to 255

  # use A2 as capacitive touch to turn on internal LED
  print("A2 touch: %d" % touch.raw_value, end="\t")
  if touch.value:
      print("A2 touched!", end ="\t")
  led.value = touch.value

  time.sleep(0.01) # make bigger to slow down

  print("")
