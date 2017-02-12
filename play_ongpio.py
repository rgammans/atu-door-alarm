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
#os.system('~/setup_jack.sh')

##Annouce we are running and clear the input latch.
nwok,error = txlog.initialise_subsystem("DoorAlarm")
if not nwok: print "No Network found continuing without net ({0})".format(error)

GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
sleep(0.001);
GPIO.output(24, GPIO.HIGH)

 
while True:
    #Wait for a change in the PIR sensor
    GPIO.wait_for_edge(23, GPIO.RISING)

    #Report alarm fired to game log server, if we found a network.
    if nwok: txlog.send_msg("Door alarm triggered")
    if DEBUG:
       print "Edge detected waiting playing audio";

    ##Play the audio
    os.system('mpg123 -q /home/pi/audio/play-this.mp3')

    if DEBUG:
       print "waiting one before clearing";

    sleep(1)

    if DEBUG:
       #Print this first as there slight race condition	
       #between setting pin24 high and waiting for a rising edge on pin23
       #which we eneed to keep a s mall as possible
       print "clearing latch"

    #Clear the flip-flop latch; after playback has finished
    GPIO.output(24, GPIO.LOW)
    sleep(0.001);
    GPIO.output(24, GPIO.HIGH)

