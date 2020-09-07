import json
import logging
import os

import paho.mqtt.client as mqtt


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                     datefmt='%d-%b-%y %H:%M:%S'
    )


def main(payload):
    """Connect to mqtt broker, send payload, and log response"""
    mqtt_broker_host = os.environ['MQTT_BROKER_HOST']
    mqtt_broker_port = int(os.environ['MQTT_BROKER_PORT'])
    topic = os.environ['MQTT_TOPIC']

    client = mqtt.Client()
    client.connect(mqtt_broker_host, mqtt_broker_port, 60)

    payload = json.dumps(payload)

    message = client.publish(topic=topic, payload=payload, qos=2)

    logging.info('Message successful: {sucess}'.format(sucess=message.is_published))
    logging.info('Return code: {rc}'.format(rc=message.rc))


if __name__=='__main__':
    """Control flow mock of microswitch triggering ever 20 seconds"""
    import time
    while True:
        logging.info('Microswitch has been triggered')
        is_triggered_payload = {
            'mydata': {
                'battery_level': 3.28762,
                'input_3': 1,
                'rssi': 100,
                'transmission_count': 219,
                'type': 37
            }
        }
        main(is_triggered_payload)
        time.sleep(20)

        logging.info('Microswitch no longer triggered')
        not_triggered_payload = {
            'mydata': {
                'battery_level': 3.28762,
                'input_3': 0,
                'transmission_count': 219,
                'type': 37
            }
        }
        main(not_triggered_payload)
        time.sleep(20)
