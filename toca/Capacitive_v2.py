import sys
import time

import Adafruit_MPR121.MPR121 as MPR121
from pygame import mixer

mixer.pre_init(22050, -16, 2, 512)
mixer.init()

cap = MPR121.MPR121()
if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)

snare = mixer.Sound("sounds/Snare.wav")
kick = mixer.Sound("sounds/Kick.wav")
hihat = mixer.Sound("sounds/Hihat.wav")

sounds = [snare, kick, hihat]

last_touched = cap.touched()
while True:
    current_touched = cap.touched()

    for i in range(len(sounds)):
        pin_bit = 1 << i

        if current_touched & pin_bit and not last_touched & pin_bit:
            print('{0} touched!'.format(i))
            sounds[i].play()

        if not current_touched & pin_bit and last_touched & pin_bit:
            print('{0} released!'.format(i))

    last_touched = current_touched
    time.sleep(0.02)