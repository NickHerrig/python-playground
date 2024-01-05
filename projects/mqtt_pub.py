import os
import time
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

mqtt_broker_host = '192.168.0.100'
mqtt_broker_port = 1883
topic = 'test/status'

client.connect(mqtt_broker_host, mqtt_broker_port, 60)

while True:
    payload = "ON"
    request = client.publish(topic=topic, payload=payload)
    print(request.rc)
    time.sleep(2)
    payload = "OFF"
    request = client.publish(topic=topic, payload=payload)
    time.sleep(2)
