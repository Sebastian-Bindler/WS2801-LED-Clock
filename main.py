# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:34:35 2021

@author: Sebi
"""
from datetime import datetime
import random
import time
import os
from inc.ledMin import setMin
from inc.ledHr import setHr
from inc.blink import blink

import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

hostname = "1.0.0.88" #example
response = os.system("ping -c 1 " + hostname)

# Configure the count of pixels:
PIXEL_COUNT = 189
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

def getMin():
    timeNow = datetime.now()
    return timeNow.minute

def getHr():
    timeNow = datetime.now()
    return timeNow.hour    
    
def randomNumber(_min, _max):
    r = random.randrange(_min, _max)
    return r    

def getColor():
    if getHr() >= 22 or getHr() < 8:
        rgb = [randomNumber(0, 16), randomNumber(0, 16), randomNumber(0, 16)]
    if getHr() >= 8 and getHr() < 22:
        rgb = [randomNumber(0, 128), randomNumber(0, 128), randomNumber(0, 128)]
    return rgb

def getBackround(rgb):
    if getHr() >= 22 or getHr() < 8:
        backround = [16 - rgb[0], 16 - rgb[1], 16 - rgb[2]]
    if getHr() >= 8 and getHr() < 22:
        backround = [128 - rgb[0], 128 - rgb[1], 128 - rgb[2]]
    return backround

def setBackround(backround):
    for i in range (0, PIXEL_COUNT):
        pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(backround[0], backround[1], backround[2]))

def test():
        rgb = getColor()
        setMin(getMin(), pixels, rgb)
        setHr(getHr(), pixels, rgb)

if __name__ == "__main__":
      
    rgb = []
    rgb = getColor()
    backround = []
    backround = getBackround(rgb)
    
    off = 0
    check = 300
    
    setBackround(backround)
    min = getMin()
    setMin(getMin(), pixels, rgb)
    
    hr = getHr()
    setHr(getHr(), pixels, rgb)
    
    hrNewColor = hr + 1
    if hrNewColor == 24:
        hrNewColor = 0
    
    while True:
        
        if check < 300:
            response = os.system("ping -c 1 " + hostname)
            
            date = datetime.now()
            print (date)
            check = 0
            
        if response != 0:
            pixels.clear()
            pixels.show()
            off = 1
            
        if response == 0:
            
            if off == 1:
                time.sleep(900)
                setBackround(backround)
                setMin(getMin(), pixels, rgb)
                setHr(getHr(), pixels, rgb) 
                off = 0
                
            # Get new color on hour change
            if getHr() == hrNewColor:
                hrNewColor = hrNewColor + 1
                if hrNewColor == 24:
                    hrNewColor = 0
                rgb = getColor()
            
            # set new minute
            if min != getMin():
                min = getMin()
                setMin(getMin(), pixels, rgb)
            
            # set new hour
            if hr != getHr():
                hr = getHr()
                setHr(getHr(), pixels, rgb)
            
            # blink dots
            blink(pixels, rgb)
            
            check = check + 1