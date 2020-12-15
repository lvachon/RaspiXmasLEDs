#!/usr/bin/env python3
import random
import board
import neopixel
import time

pixel_pin = board.D18

num_pixels = 300

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
colors = []
offset = 0.0

colorset = []

def getcolor(pos):
	p = pos-(int)(pos);
	pos=(int)(pos)%num_pixels
	fadesteps=1;
	oldcolor = colorset[pos]
	if(pos>0):
		newcolor = colorset[pos-1]
	else:
		newcolor = colorset[num_pixels-1]
	return ((int)(oldcolor[0]*(p/fadesteps)+newcolor[0]*((fadesteps-p)/fadesteps)) ,
	(int)(oldcolor[1]*(p/fadesteps)+newcolor[1]*((fadesteps-p)/fadesteps)) , 
	(int)(oldcolor[2]*(p/fadesteps)+newcolor[2]*((fadesteps-p)/fadesteps)))


def wheel(pos):
    if(pos < 2*255/5):
        return (0,32,0)
    if(pos < 4*255/5):
        return (186, 0, 0)
    return(255, 128, 32)

for i in range(0,num_pixels):
	colorset.append(wheel(random.randrange(255)));
pos=0
while(True):
	pos+=0.1;
	for i in range(0,num_pixels-1):
		pixels[i]=getcolor(pos+i)
	pixels.show()
	time.sleep(0.01)
		
