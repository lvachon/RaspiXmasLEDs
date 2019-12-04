#!/usr/bin/env python3
import random
import board
import neopixel
import time

pixel_pin = board.D18

num_pixels = 110

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
brights = []
offset = 0.0



min_bright = 32
max_bright = 255

for i in range(0,num_pixels):
	a = random.randrange(min_bright,max_bright)
	brights.append(a)

while(True):
	for i in range(0,num_pixels):
		brights[i]+=random.randrange(-1,2)
		if(brights[i]>max_bright):
			brights[i]=max_bright
		if(brights[i]<min_bright):
			brights[i]=min_bright
		pixels[i]=(brights[i], brights[i], brights[i])
	pixels.show()
	time.sleep(0.01)

