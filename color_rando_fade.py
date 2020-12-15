#!/usr/bin/env python3
import random
import board
import neopixel
import time
import math

pixel_pin = board.D18

num_pixels = 300

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
oldColors = []
newColors = []

minBright = 32
maxBright = 255
fadeSteps = 60.0

def colorset(pos):
	pos = (int)(pos)%256
	if(pos < 2*255/5):
		return (0,32,0)
	if(pos < 4*255/5):
		return (186, 0, 0)
	return(255, 128, 32)

def fadeColor(colorA, colorB, pct):
	pct = (math.sin(pct*0.5*math.pi))
	return (
		(int)(pct*colorA[0]+(1-pct)*colorB[0]),
		(int)(pct*colorA[1]+(1-pct)*colorB[1]),
		(int)(pct*colorA[2]+(1-pct)*colorB[2])
		)

for i in range(0,num_pixels):
	oldColors.append(colorset(random.randrange(256)))
	newColors.append(colorset(random.randrange(256)))


while(True):
	oldColors=newColors.copy()
	for i in range(0,num_pixels):
		newColors[i]=colorset(random.randrange(256))
	for fadeStep in range(0,(int)(fadeSteps)):
		for i in range(0,num_pixels):
			pixels[i]=fadeColor(newColors[i],oldColors[i],fadeStep/fadeSteps)
		pixels.show()
		time.sleep(0.01)
	time.sleep(1)
