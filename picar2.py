
#this is the script that runs the motors
#from pythonprogramming.net

import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

def forward(x):
        GPIO.output(13, GPIO.HIGH)
        sleep(x)
        GPIO.output(13, GPIO.LOW)

def reverse(x):
        GPIO.output(15, GPIO.HIGH)
        sleep(x)
        GPIO.output(15, GPIO.LOW)

def left(x):
        GPIO.output(11, GPIO.HIGH)
        sleep(x)
        GPIO.output(11, GPIO.LOW)

def right(x):
        GPIO.output(7, GPIO.HIGH)
        sleep(x)
        GPIO.output(7, GPIO.LOW)


GPIO.cleanup()

