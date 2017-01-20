import sys
import time
import random
from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
from time import sleep
import telepot
from twilio.rest import TwilioRestClient


camera = PiCamera()
client = TwilioRestClient(account='ACd7bae9272d87caddf22fb8f0a3cecb7c', token='7b45f7580aea80b43fd5e420df93148b')
pir = MotionSensor(4)
while True:
    pir.wait_for_motion()
    filename = datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")    
    camera.start_recording(filename)
    client.messages.create(to='+918897771300',from_='+15084434500',body="Hey There! It seems someone is at your home. Were you expecting someone?")
    sleep(10)
    pir.wait_for_no_motion()
    camera.stop_recording()
