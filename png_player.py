#!/usr/bin/env python3
import random
import board
import neopixel
import time

pixel_pin = board.D18

num_pixels = 110

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
animation = []

f = open("sparklesNribbons.ppm","r")
format = f.readline()
comment = f.readline()
dimensions = f.readline().split()
data = f.read()
data = data.split()	
for y in range(0,dimensions[1]):
	animation.append([])
	for x in range(0,dimensions[0]):
		index = 3*(x+y*dimensions[0])
		animation[y].append(data[index],data[index+1],data[index+2])

animIndex=0
while(True):
	for x in range(0,dimensions[0]):
		pixels[x]=animation[animIndex][x]
	pixels.show()
	animIndex = (animIndex+1)%dimensions[1]
	time.sleep(0.03)
	
