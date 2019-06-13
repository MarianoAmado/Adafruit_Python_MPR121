
#import pygame
import time
import serial

from pygame import mixer

ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0]

# pygame.init()
mixer.pre_init(22050, -16, 2, 512)
mixer.init()

snare = mixer.Sound("sounds/Snare.wav")
kick = mixer.Sound("sounds/Kick.wav")
hihat = mixer.Sound("sounds/Hihat.wav")

play = snare.play()

while True:
	read_serial=ser.readline()
	s[0] = str(ser.readline())

	if (int(s[0]) == 1):
		snare.play()
		time.sleep(.01)