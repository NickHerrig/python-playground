import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect(ip, port, 60)

payload = 'hello'
request = client.publish("/name/message", payload=payload)

print(request.is_published)
print(request.mid)
print(request.rc)


