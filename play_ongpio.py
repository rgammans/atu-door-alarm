#!/usr/bin/env python
 
DEBUG=1

import os
from time import sleep
import txlog
import RPi.GPIO as GPIO

#Setup Input GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

##Enable audio routing.
os.system('~/setup_jack.sh')

##Annouce we are running and clear the input latch.
txlog.initialise_subsystem("DoorAlarm")
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
sleep(0.001);
GPIO.output(24, GPIO.HIGH)

 
while True:
    #Wait for a change in the PIR sensor
    GPIO.wait_for_edge(23, GPIO.RISING)

    #Report alarm fired to game log server.
    txlog.send_msg("Door alarm triggered")
    if DEBUG:
       print "Edge detected waiting playing audio";

    ##Play the audio
    os.system('mpg123 -q ~/audio/binary-language.mp3')

    if DEBUG:
       print "waiting one before clearing";
       sleep(1)
       print "cleared latch"

    #Clear the flip-flop latch; after playback has finished
    GPIO.output(24, GPIO.LOW)
    sleep(0.001);
    GPIO.output(24, GPIO.HIGH)

