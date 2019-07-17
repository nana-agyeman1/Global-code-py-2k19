import requests

#url = "https://maker.ifttt.com/use/oLXaSVTrxOexMIOzthhsPukbi6F0jhWapcN3gOyCw1X"
r = requests.get("https://maker.ifttt.com/trigger/HTU/with/key/oLXaSVTrxOexMIOzthhsPukbi6F0jhWapcN3gOyCw1X", {"Value1": "Hello team!"})
#r = requests.post("https://maker.ifttt.com/trigger/HTU/with/key/oLXaSVTrxOexMIOzthhsPukbi6F0jhWapcN3gOyCw1X")
c = r.status_code
print(c)


#https://maker.ifttt.com/trigger/GLBLCD/with/key/oLXaSVTrxOexMIOzthhsPukbi6F0jhWapcN3gOyCw1X
'''Sending a message to another phone'''
name = "Alex"
messenger = "What's up with you"

requests.get("https://maker.ifttt.com/trigger/HTU/with/key/oLXaSVTrxOexMIOzthhsPukbi6F0jhWapcN3gOyCw1X",{"Value1": "Hello team!"})










'''import os, sys
import RPi.GPIO as GPIO
import time
import requests 
from datetime import datetime
 
def post(value):
	payload={"value1":str(value),"value2":str(datetime.now())}
	req = requests.post("http://maker.ifttt.com/trigger/<eventname>/with/key/<maker-key>", data=payload)
	print (req.url)
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
start=1
past=0
while True:
	now=GPIO.input(25)
	if(now!=past and start==0):
		post(now)
	start=0
	time.sleep(5)
	past=now
GPIO.cleanup()'''
