import os
import paho.mqtt.client as mqtt

MQTT_PORT=int(os.environ['MQTT_PORT'])
MQTT_HOST=os.environ['MQTT_HOST']
MQTT_TOPIC=os.environ['MQTT_TOPIC']
SPEECH_HOST=os.environ['SPEECH_HOST']
SPEECH_PORT=int(os.environ['SPEECH_PORT'])

from os import listdir
from os.path import isfile, join
mypath = "./models"
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_start()

def detect(user, name):
    print("detect:" + user + ", " + name)
    client.publish(MQTT_TOPIC, user + ", " + name)
    return

models = []
callbacks = []
for file in files:
    parts = file.split("_")
    models.append("./models/" + file)
    callback = {"callback": detect, "user": parts[0], "name": parts[1]}
    callbacks.append(callback)

import snowboydecoder
import sys
import signal

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(models, sensitivity=0.4, audio_gain=4)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.06)

detector.terminate()
