#!/usr/bin/env python3
import random
import board
import neopixel
import time

pixel_pin = board.D18

num_pixels = 110

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
colors = []
offset = 0.0


def wheel(pos):
    if(pos < 2*255/5):
        return (0,32,0)
    if(pos < 4*255/5):
        return (186, 0, 0)
    return(255, 128, 32)
oldcolors=[]
for i in range(0,num_pixels-1):
	pixels[i]=(0,0,0)
	oldcolors.append((0,0,0))
pixels.show()
fadesteps=15.0
while(True):
	for i in range(0,num_pixels-1):
		oldcolors[i] = pixels[i]
	newincolor=wheel(random.randrange(255))

	for p in range(0,(int)(fadesteps)):
		pixels[0]=(
			(int)(newincolor[0]*p/fadesteps+oldcolors[0][0]*(fadesteps-p)/fadesteps) , 
			(int)(newincolor[1]*p/fadesteps+oldcolors[0][1]*(fadesteps-p)/fadesteps) , 
			(int)(newincolor[2]*p/fadesteps+oldcolors[0][2]*(fadesteps-p)/fadesteps))
		for i in range(1,num_pixels-1):
			newcolor = oldcolors[i-1]
			oldcolor = oldcolors[i]

			pixels[i]=(
				(int)(oldcolor[0]*(p/fadesteps)+newcolor[0]*((fadesteps-p)/fadesteps)) ,
				(int)(oldcolor[1]*(p/fadesteps)+newcolor[1]*((fadesteps-p)/fadesteps)) , 
				(int)(oldcolor[2]*(p/fadesteps)+newcolor[2]*((fadesteps-p)/fadesteps)))
		pixels.show()
		
