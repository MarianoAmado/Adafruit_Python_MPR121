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

viento =  mixer.Sound("/home/pi/toca/sounds/viento.wav")
cascabel = mixer.Sound("/home/pi/toca/sounds/cascabel.wav")
trueno =  mixer.Sound("/home/pi/toca/sounds/trueno.wav")
rocas =  mixer.Sound("/home/pi/toca/sounds/rocas.wav")
pasos =  mixer.Sound("/home/pi/toca/sounds/pasos.wav")
lobo =  mixer.Sound("/home/pi/toca/sounds/lobo.wav")
caballo =  mixer.Sound("/home/pi/toca/sounds/caballo.wav")
burro =  mixer.Sound("/home/pi/toca/sounds/burro.wav")
bats =  mixer.Sound("/home/pi/toca/sounds/bats.wav")
agua =  mixer.Sound("/home/pi/toca/sounds/agua.wav")
agua2 =  mixer.Sound("/home/pi/toca/sounds/agua2.wav")
agua3 =  mixer.Sound("/home/pi/toca/sounds/agua3.wav")


sounds = [ viento, cascabel, trueno, rocas, pasos, lobo, caballo, burro, bats, agua, agua2, agua3 ]

cascabel.play()

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
