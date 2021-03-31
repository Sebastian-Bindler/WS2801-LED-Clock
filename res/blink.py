# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:48:13 2021

@author: Sebi
"""

import RPi.GPIO as GPIO
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import time

# Configure the count of pixels:
PIXEL_COUNT = 189
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

def blink(pixels, rgb):
    
    pixels.set_pixel(73, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
    pixels.set_pixel(115, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
    pixels.show()
    time.sleep(1.5)
    
    pixels.set_pixel(73, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
    pixels.set_pixel(115, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
    pixels.show()
    time.sleep(1.5)
    
if __name__ == "__main__":
    
    pixels.clear()
    pixels.show()  
    rgb = [255, 0, 0]
    
    for i in range (0, 100):
        blink(rgb)