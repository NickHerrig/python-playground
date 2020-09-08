import os

import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    topic = os.environ['MQTT_TOPIC']
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

mqtt_broker_host = os.environ['MQTT_BROKER_HOST']
mqtt_broker_port = int(os.environ['MQTT_BROKER_PORT'])
client.connect(mqtt_broker_host, mqtt_broker_port, 60)
client.loop_forever()
