import os

from queue import Queue

import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    topic = 'test/#'
    client.subscribe(topic)

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload
    print(topic, payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

mqtt_broker_host = '192.168.0.100'
mqtt_broker_port = 1883
client.connect(mqtt_broker_host, mqtt_broker_port, 60)
client.loop_forever()
