# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:55:22 2021

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

def setMin0R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin1R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin2R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin3R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin4R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin5R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin6R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin7R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin8R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin9R(pixels, rgb):
        pixels.set_pixel(58, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(59, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(60, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(65, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(67, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
        pixels.set_pixel(100, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(101, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(102, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(107, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(109, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(142, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(143, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(144, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin0L(pixels, rgb):
        pixels.set_pixel(54, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(55, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(56, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(69, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(71, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(96, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(97, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(98, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(111, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(113, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(138, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(139, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(140, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin1L(pixels, rgb):
        pixels.set_pixel(54, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(55, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(56, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(69, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(71, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(96, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(97, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(98, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(111, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(113, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(138, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(139, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(140, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin2L(pixels, rgb):
        pixels.set_pixel(54, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(55, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(56, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(69, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(71, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(96, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(97, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(98, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(111, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(113, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(138, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(139, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(140, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin3L(pixels, rgb):
        pixels.set_pixel(54, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(55, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(56, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(69, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(71, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(96, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(97, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(98, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(111, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(113, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(138, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(139, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(140, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin4L(pixels, rgb):
        pixels.set_pixel(54, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(55, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(56, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(69, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(71, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(96, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(97, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(98, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(111, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(113, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(138, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(139, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(140, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def setMin5L(pixels, rgb):
        pixels.set_pixel(54, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(55, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(56, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(69, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(71, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(96, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(97, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(98, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(111, Adafruit_WS2801.RGB_to_color( 0, 0, 0))
        pixels.set_pixel(113, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(138, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(139, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        pixels.set_pixel(140, Adafruit_WS2801.RGB_to_color( rgb[0], rgb[1], rgb[2]))
        
def min0(pixels, rgb):
        
        setMin0R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()

def min1(pixels, rgb):
        
        setMin1R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min2(pixels, rgb):
        
        setMin2R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min3(pixels, rgb):
        
        setMin3R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min4(pixels, rgb):
        
        setMin4R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min5(pixels, rgb):
        
        setMin5R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min6(pixels, rgb):
        
        setMin6R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min7(pixels, rgb):
        
        setMin7R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min8(pixels, rgb):
        
        setMin8R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min9(pixels, rgb):
        
        setMin9R(pixels, rgb)
        setMin0L(pixels, rgb)
        pixels.show()
        
def min10(pixels, rgb):
        
        setMin0R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min11(pixels, rgb):
        
        setMin1R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min12(pixels, rgb):
        
        setMin2R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
        
def min13(pixels, rgb):
        
        setMin3R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min14(pixels, rgb):
        
        setMin4R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min15(pixels, rgb):
        
        setMin5R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min16(pixels, rgb):
        
        setMin6R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min17(pixels, rgb):
        
        setMin7R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min18(pixels, rgb):
        
        setMin8R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min19(pixels, rgb):
        
        setMin9R(pixels, rgb)
        setMin1L(pixels, rgb)
        pixels.show()
        
def min20(pixels, rgb):       
        
        setMin0R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min21(pixels, rgb):
        
        setMin1R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min22(pixels, rgb):
        
        setMin2R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min23(pixels, rgb):
        
        setMin3R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min24(pixels, rgb):
        
        setMin4R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min25(pixels, rgb):        
        
        setMin5R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min26(pixels, rgb):        
        
        setMin6R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min27(pixels, rgb):        
        
        setMin7R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min28(pixels, rgb):        
        
        setMin8R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()
        
def min29(pixels, rgb):        
        
        setMin9R(pixels, rgb)
        setMin2L(pixels, rgb)
        pixels.show()

def min30(pixels, rgb):        
        
        setMin0R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min31(pixels, rgb):        
        
        setMin1R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min32(pixels, rgb):        
        
        setMin2R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min33(pixels, rgb):        
        
        setMin3R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min34(pixels, rgb):        
        
        setMin4R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min35(pixels, rgb):        
        
        setMin5R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min36(pixels, rgb):        
        
        setMin6R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min37(pixels, rgb):        
        
        setMin7R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min38(pixels, rgb):        
        
        setMin8R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min39(pixels, rgb):        
        
        setMin9R(pixels, rgb)
        setMin3L(pixels, rgb)
        pixels.show()
        
def min40(pixels, rgb):        
        
        setMin0R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min41(pixels, rgb):        
        
        setMin1R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min42(pixels, rgb):        
        
        setMin2R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min43(pixels, rgb):        
        
        setMin3R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min44(pixels, rgb):        
        
        setMin4R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min45(pixels, rgb):        
        
        setMin5R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min46(pixels, rgb):        
        
        setMin6R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min47(pixels, rgb):        
        
        setMin7R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min48(pixels, rgb):        
        
        setMin8R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()
        
def min49(pixels, rgb):        
        
        setMin9R(pixels, rgb)
        setMin4L(pixels, rgb)
        pixels.show()        

def min50(pixels, rgb):        
        
        setMin0R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min51(pixels, rgb):        
        
        setMin1R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min52(pixels, rgb):        
        
        setMin2R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min53(pixels, rgb):        
        
        setMin3R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min54(pixels, rgb):        
        
        setMin4R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min55(pixels, rgb):        
        
        setMin5R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min56(pixels, rgb):        
        
        setMin6R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min57(pixels, rgb):        
        
        setMin7R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min58(pixels, rgb):        
        
        setMin8R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()
        
def min59(pixels, rgb):        
        
        setMin9R(pixels, rgb)
        setMin5L(pixels, rgb)
        pixels.show()   

def setMin(minute, pixels, rgb):
    if	minute == 0: 
        min0(pixels, rgb)
    if	minute == 1: 
    	min1(pixels, rgb)
    if	minute == 2: 
    	min2(pixels, rgb)
    if	minute == 3: 
    	min3(pixels, rgb)
    if	minute == 4: 
    	min4(pixels, rgb)
    if	minute == 5: 
    	min5(pixels, rgb)
    if	minute == 6: 
    	min6(pixels, rgb)
    if	minute == 7: 
    	min7(pixels, rgb)
    if	minute == 8: 
    	min8(pixels, rgb)
    if	minute == 9: 	
    	min9(pixels, rgb)
    if	minute == 10: 
    	min10(pixels, rgb)
    if	minute == 11: 
    	min11(pixels, rgb)
    if	minute == 12: 
    	min12(pixels, rgb)
    if	minute == 13: 
    	min13(pixels, rgb)
    if	minute == 14: 
    	min14(pixels, rgb)
    if	minute == 15: 
    	min15(pixels, rgb)
    if	minute == 16: 
    	min16(pixels, rgb)
    if	minute == 17: 
    	min17(pixels, rgb)
    if	minute == 18: 
    	min18(pixels, rgb)
    if	minute == 19: 
    	min19(pixels, rgb)
    if	minute == 20: 
    	min20(pixels, rgb)
    if	minute == 21: 
    	min21(pixels, rgb)
    if	minute == 22: 
    	min22(pixels, rgb)
    if	minute == 23: 
    	min23(pixels, rgb)
    if	minute == 24: 
    	min24(pixels, rgb)
    if	minute == 25: 
    	min25(pixels, rgb)
    if	minute == 26: 
    	min26(pixels, rgb)
    if	minute == 27: 
    	min27(pixels, rgb)
    if	minute == 28: 
    	min28(pixels, rgb)
    if	minute == 29: 
    	min29(pixels, rgb)
    if	minute == 30: 
    	min30(pixels, rgb)
    if	minute == 31: 
    	min31(pixels, rgb)
    if	minute == 32: 
    	min32(pixels, rgb)
    if	minute == 33: 
    	min33(pixels, rgb)
    if	minute == 34: 
    	min34(pixels, rgb)
    if	minute == 35: 
    	min35(pixels, rgb)
    if	minute == 36: 
    	min36(pixels, rgb)
    if	minute == 37: 
    	min37(pixels, rgb)
    if	minute == 38: 
    	min38(pixels, rgb)
    if	minute == 39: 
    	min39(pixels, rgb)
    if	minute == 40: 
    	min40(pixels, rgb)
    if	minute == 41: 
    	min41(pixels, rgb)
    if	minute == 42: 
    	min42(pixels, rgb)
    if	minute == 43: 
    	min43(pixels, rgb)
    if	minute == 44: 
    	min44(pixels, rgb)
    if	minute == 45: 
    	min45(pixels, rgb)
    if	minute == 46: 
    	min46(pixels, rgb)
    if	minute == 47: 
    	min47(pixels, rgb)
    if	minute == 48: 
    	min48(pixels, rgb)
    if	minute == 49: 
    	min49(pixels, rgb)
    if	minute == 50: 
    	min50(pixels, rgb)
    if	minute == 51: 
    	min51(pixels, rgb)
    if	minute == 52: 
    	min52(pixels, rgb)
    if	minute == 53: 
    	min53(pixels, rgb)
    if	minute == 54: 
    	min54(pixels, rgb)
    if	minute == 55: 
    	min55(pixels, rgb)
    if	minute == 56: 
    	min56(pixels, rgb)
    if	minute == 57: 
    	min57(pixels, rgb)
    if	minute == 58: 
    	min58(pixels, rgb)
    if	minute == 59: 
    	min59(pixels, rgb)
    
if __name__ == "__main__": 
        # Clear all the pixels to turn them off.
        pixels.clear()
        # Make sure to call show() after changing any pixels!
        pixels.show()  
        rgb = [255, 0, 0]

        for i in range (0, 60):
            setMin(i, rgb)
            time.sleep(0.5)
       
        
        
        
"""
        for i in range (20):
            pixels.set_pixel(116, Adafruit_WS2801.RGB_to_color( 255, 0, 0 ))
            pixels.set_pixel(74, Adafruit_WS2801.RGB_to_color( 255, 0, 0 ))
            pixels.show()
            time.sleep(1.75)
            print(i)
            pixels.set_pixel(116, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
            pixels.set_pixel(74, Adafruit_WS2801.RGB_to_color( 0, 0, 0 ))
            pixels.show()
            time.sleep(1.75)"""
            