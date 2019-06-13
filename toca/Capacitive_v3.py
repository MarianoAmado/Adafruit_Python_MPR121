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

trompeta =  mixer.Sound("/home/pi/toca/sounds/juego/trompeta.wav")
piano = mixer.Sound("/home/pi/toca/sounds/juego/piano.wav")
tren =  mixer.Sound("/home/pi/toca/sounds/juego/tren.wav")
timbre =  mixer.Sound("/home/pi/toca/sounds/juego/timbre.wav")
snare =  mixer.Sound("/home/pi/toca/sounds/juego/snare.wav")
osito =  mixer.Sound("/home/pi/toca/sounds/juego/osito.wav")
laser =  mixer.Sound("/home/pi/toca/sounds/juego/laser.wav")
kick =  mixer.Sound("/home/pi/toca/sounds/juego/kick.wav")
crash =  mixer.Sound("/home/pi/toca/sounds/juego/crash.wav")
chifle =  mixer.Sound("/home/pi/toca/sounds/juego/chifle.wav")
burro =  mixer.Sound("/home/pi/toca/sounds/juego/burro.wav")
bateria =  mixer.Sound("/home/pi/toca/sounds/juego/bateria.wav")


sounds = [ trompeta, piano, tren, timbre, snare, osito, laser, kick, crash, chifle, burro, bateria ]

piano.play()

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
    time.sleep(0.04)

    last_touched = current_touched
    #time.sleep(0.08)
