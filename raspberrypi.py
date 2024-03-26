#!/usr/bin/python
# Read a Pir-sensor and send a Mqtt message when motion detected
# Uses edge detection to limit the rate of Mqtt-messages
import paho.mqtt.client as paho
import time
import urlparse
import RPi.GPIO as GPIO
import datetime

# Mqtt
mqttc = paho.Client()
url_str = 'mqtt://192.168.1.79:1883'
url = urlparse.urlparse(url_str)
mqttc.username_pw_set("emonpi", "emonpimqtt2016")

# Setup Gpio
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)         # Output from PIR motion sensor connected to pin 13

def printtime(): # Used for debug
	# Current time
	global hour, minute, wholetime
	now = datetime.datetime.now()
	hour = str(now.hour)
	minute = int(now.minute)
	minute = '%02d' % minute
	wholetime = hour + ":" + minute

def sendmqtt(mess):
    try:
	mqttc.connect(url.hostname, url.port)
	mqttc.publish("pir/hallway", mess)
	sleep(5)
    except:
	    pass

sendmqtt("Pirmqtt started")

while True:
	try:
		GPIO.wait_for_edge(13, GPIO.RISING)
	 	#printtime()
   		#print "Time now: " + wholetime
		#print("Motion detected")
  		sendmqtt("on")
		time.sleep(5)
		sendmqtt("off")
		time.sleep(5)
	except KeyboardInterrupt:
    		# quit
    		sys.exit()	 