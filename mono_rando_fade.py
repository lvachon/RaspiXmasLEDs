
#!/usr/bin/env python3
import random
import board
import neopixel
import time
import math

pixel_pin = board.D18

num_pixels = 110

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.8, auto_write=False, pixel_order=ORDER)
oldColors = []
newColors = []

minBright = 0
maxBright = 255
fadeSteps = 60.0
gamma=1.8

def colorset(i):
	i = (int)(i)%256
	i = math.pow(i/256,gamma)
	return (
		(int)(i*(maxBright-minBright)+minBright),
		(int)(i*(maxBright-minBright)+minBright),
		(int)(i*(maxBright-minBright)+minBright)
	)

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
		if(i==0):
			print(newColors[0])
	for fadeStep in range(0,(int)(fadeSteps)):
		for i in range(0,num_pixels):
			pixels[i]=fadeColor(newColors[i],oldColors[i],fadeStep/fadeSteps)
		pixels.show()
		time.sleep(0.01)

