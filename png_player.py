#!/usr/bin/env python3
import random
import board
import neopixel
import time
import sys

pixel_pin = board.D18

num_pixels = 110

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
animations = []

for i in range(1,len(sys.argv)):
	animations.append([])
	f = open(sys.argv[1],"r")
	format = f.readline()
	comment = f.readline()
	dimensions = f.readline().split()
	maxval = f.readline()
	data = f.read()
	data = data.split()
	for y in range(0,int(dimensions[1])):
		animations[i-1].append([])
		for x in range(0,int(dimensions[0])):
			index = 3*(x+y*int(dimensions[0]))
			animations[i][y].append((int(data[index+0]),int(data[index+1]),int(data[index+2])))

frameIndex=0
animIndex=0
animCount=len(sys.argv)-1
loopCount=0
maxLoops=4
while(True):
	for x in range(0,int(dimensions[0])):
		pixels[x]=animations[animIndex][frameIndex][x]
	pixels.show()
	frameIndex = (frameIndex+1)%int(dimensions[1])
	if(frameIndex==0):
		loopCount=loopCount+1
		if(loopCount==5):
			loopCount=0
			animIndex=(animIndex+1)%animCount
	time.sleep(0.05)
