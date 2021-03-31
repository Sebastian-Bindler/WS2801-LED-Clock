# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:10:21 2021

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

def setHr0L(pixels, rgb):
        pixels.set_pixel(44, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(45, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(46, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(79, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(81, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(86, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(87, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(88, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(121, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(123, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(128, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(129, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(130, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr1L(pixels, rgb):
        pixels.set_pixel(44, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(45, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(46, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(79, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(81, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(86, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(87, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(88, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(121, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(123, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(128, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(129, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(130, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr2L(pixels, rgb):
        pixels.set_pixel(44, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(45, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(46, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(79, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(81, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(86, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(87, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(88, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(121, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(123, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(128, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(129, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(130, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr0R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr1R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr2R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))

def setHr3R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr4R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr5R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr6R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr7R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr8R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setHr9R(pixels, rgb):
        pixels.set_pixel(48, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(49, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(50, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(75, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(77, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(90, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(91, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(92, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(117, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(119, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(132, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(133, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(134, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
        
def hr0(pixels, rgb):
        
        setHr0R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()

def hr1(pixels, rgb):
        
        setHr1R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr2(pixels, rgb):
        
        setHr2R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr3(pixels, rgb):
        
        setHr3R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr4(pixels, rgb):
        
        setHr4R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr5(pixels, rgb):
        
        setHr5R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr6(pixels, rgb):
        
        setHr6R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr7(pixels, rgb):
        
        setHr7R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr8(pixels, rgb):
        
        setHr8R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr9(pixels, rgb):
        
        setHr9R(pixels, rgb)
        setHr0L(pixels, rgb)
        pixels.show()
        
def hr10(pixels, rgb):
        
        setHr0R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr11(pixels, rgb):
        
        setHr1R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr12(pixels, rgb):
        
        setHr2R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
        
def hr13(pixels, rgb):
        
        setHr3R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr14(pixels, rgb):
        
        setHr4R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr15(pixels, rgb):
        
        setHr5R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr16(pixels, rgb):
        
        setHr6R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr17(pixels, rgb):
        
        setHr7R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr18(pixels, rgb):
        
        setHr8R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr19(pixels, rgb):
        
        setHr9R(pixels, rgb)
        setHr1L(pixels, rgb)
        pixels.show()
        
def hr20(pixels, rgb):       
        
        setHr0R(pixels, rgb)
        setHr2L(pixels, rgb)
        pixels.show()
        
def hr21(pixels, rgb):
        
        setHr1R(pixels, rgb)
        setHr2L(pixels, rgb)
        pixels.show()
        
def hr22(pixels, rgb):
        
        setHr2R(pixels, rgb)
        setHr2L(pixels, rgb)
        pixels.show()
        
def hr23(pixels, rgb):
        
        setHr3R(pixels, rgb)
        setHr2L(pixels, rgb)
        pixels.show()
        
def hr24(pixels, rgb):
        
        setHr4R(pixels, rgb)
        setHr2L(pixels, rgb)
        pixels.show()

def setHr(hour, pixels, rgb):
    if	hour == 0: 
        hr0(pixels, rgb)
    if	hour == 1: 
    	hr1(pixels, rgb)
    if	hour == 2: 
    	hr2(pixels, rgb)
    if	hour == 3: 
    	hr3(pixels, rgb)
    if	hour == 4: 
    	hr4(pixels, rgb)
    if	hour == 5: 
    	hr5(pixels, rgb)
    if	hour == 6: 
    	hr6(pixels, rgb)
    if	hour == 7: 
    	hr7(pixels, rgb)
    if	hour == 8: 
    	hr8(pixels, rgb)
    if	hour == 9: 	
    	hr9(pixels, rgb)
    if	hour == 10: 
    	hr10(pixels, rgb)
    if	hour == 11: 
    	hr11(pixels, rgb)
    if	hour == 12: 
    	hr12(pixels, rgb)
    if	hour == 13: 
    	hr13(pixels, rgb)
    if	hour == 14: 
    	hr14(pixels, rgb)
    if	hour == 15: 
    	hr15(pixels, rgb)
    if	hour == 16: 
    	hr16(pixels, rgb)
    if	hour == 17: 
    	hr17(pixels, rgb)
    if	hour == 18: 
    	hr18(pixels, rgb)
    if	hour == 19: 
    	hr19(pixels, rgb)
    if	hour == 20: 
    	hr20(pixels, rgb)
    if	hour == 21: 
    	hr21(pixels, rgb)
    if	hour == 22: 
    	hr22(pixels, rgb)
    if	hour == 23: 
    	hr23(pixels, rgb)

                
if __name__ == "__main__":   
    
            # Clear all the pixels to turn them off.
    pixels.clear()
        # Make sure to call show() after changing any pixels!
    pixels.show()  
    rgb = [255, 0, 0]
        
    for i in range (0 , 24):
        setHr(i, rgb)
        time.sleep(0.5)
        
        
