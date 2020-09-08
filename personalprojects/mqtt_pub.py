import os
import json
import time
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

mqtt_broker_host = os.environ['MQTT_BROKER_HOST']
mqtt_broker_port = int(os.environ['MQTT_BROKER_PORT'])
topic = os.environ['MQTT_TOPIC']

client.connect(mqtt_broker_host, mqtt_broker_port, 60)

while True:
    payload = {"temperature":23.20,"humidity":51.60}
    payload = json.dumps(payload)
    request = client.publish(topic=topic, payload=payload)
    print(request.rc)
    time.sleep(10)
    payload = {"temperature":40.0,"humidity":5.60}
    payload = json.dumps(payload)
    request = client.publish(topic=topic, payload=payload)
    time.sleep(10)
