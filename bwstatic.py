#!/usr/bin/env python3
import random
import board
import neopixel
import time

pixel_pin = board.D18

num_pixels = 110

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)


while(True):
	for i in range(0,num_pixels-1):
		x = random.randrange(255)
		pixels[i]=(x,x,x)
	pixels.show()
	time.sleep(0.1)

