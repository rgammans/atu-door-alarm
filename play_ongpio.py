#!/usr/bin/env python
 
import os
from time import sleep
import txlog
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)


txlog.initialise_subsystem("DoorAlarm")
 
while True:
    #Wait for a change in the PIR sensor
    GPIO.wait_for_edge((23, GPIO.RISING)
    txlog.send_msg("Door alarm triggered")
    os.system('mpg123 -q binary-language-moisture-evaporators.mp3')

    #Clear the flip-flop latch; after playback has finished
    GPIO.output(24, GPIO.HIGH)
    sleep(0.001);
    GPIO.output(24, GPIO.LOW)

