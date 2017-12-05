import urllib
from subprocess import call
import paho.mqtt.client as mqtt
import os
from importlib import reload
import urllib.parse

MQTT_PORT=int(os.environ['MQTT_PORT'])
MQTT_HOST=os.environ['MQTT_HOST']
MQTT_TOPIC=os.environ['MQTT_TOPIC']
TTS_HOST=os.environ['TTS_HOST']
TTS_PORT=os.environ['TTS_PORT']
AUDIO_DEVICE=os.environ['AUDIO_DEVICE']

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    text = msg.payload.decode('iso-8859-1').encode('utf8');
    print(msg.topic+" "+str(msg.payload))
    url = "http://" + TTS_HOST  + ":" + TTS_PORT  + "/read?voiceId=Vicki&text=" + urllib.parse.quote(text) + "&outputFormat=ogg_vorbis"
    call(["ogg123", "-d", "alsa", "-o", AUDIO_DEVICE, url])

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_forever()

