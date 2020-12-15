#!/usr/bin/env python3
import random
import board
import neopixel
import time
import sys
print("Init pixels")
pixel_pin = board.D18

num_pixels = 300

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)
animations = []
print("Load animations")
for i in range(1,len(sys.argv)):
	animations.append([])
	print("Loading:"+sys.argv[i])
	f = open(sys.argv[i],"r")
	format = f.readline()
	#comment = f.readline()
	dimensions = f.readline().split()
	maxval = f.readline()
	data = f.read()
	data = data.split()
	for y in range(0,int(dimensions[1])):
		animations[i-1].append([])
		for x in range(0,int(dimensions[0])):
			index = 3*(x+y*int(dimensions[0]))
			animations[i-1][y].append((int(data[index+0]),int(data[index+1]),int(data[index+2])))
	f.close()
print("Loaded "+str(len(animations))+" animations")
frameIndex=0
animIndex=0
animCount=len(animations)
loopCount=0
maxLoops=2
print("Playing!")
while(True):
	for x in range(0,num_pixels):
		pixels[x]=animations[animIndex][frameIndex][x]
	pixels.show()
	frameIndex = (frameIndex+1)%int(dimensions[1])
	if(frameIndex==0):
		loopCount=loopCount+1
		print("Loop:"+str(loopCount))
		if(loopCount==maxLoops):
			loopCount=0
			animIndex=(animIndex+1)%animCount
			print("Animation:"+str(animIndex))
	time.sleep(0.01)

