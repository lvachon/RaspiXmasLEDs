#!/usr/bin/env python3
import random
import board
import neopixel
import time

pixel_pin = board.D18

num_pixels = 300

ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

def wheel(pos):
    if(pos < 2*255/5):
        return (0,32,0)
    if(pos < 4*255/5):
        return (186, 0, 0)
    return(255, 128, 32)


for i in range(0,num_pixels-1):
    pixels[i]=wheel(random.randrange(255))
pixels.show()

while(True):
    pixelindex = random.randrange(num_pixels-1)
    oldcolor = pixels[pixelindex]
    newcolor=oldcolor
    while(newcolor==oldcolor):
        newcolor = wheel(random.randrange(255))
    
    
    for i in range(0,30):
        pixels[pixelindex]=(
            (int)(oldcolor[0]*(30-i)/30.0+newcolor[0]*i/30.0),
            (int)(oldcolor[1]*(30-i)/30.0+newcolor[1]*i/30.0),
            (int)(oldcolor[2]*(30-i)/30.0+newcolor[2]*i/30.0)
        )
        pixels.show()
        time.sleep(0.001)

