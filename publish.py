
import random

from paho.mqtt import client as mqtt_client


broker = 'wss://vernemq-testops.pwc.dev.cos.pwtestops.com/mqtt'
# generate client ID with pub prefix randomly
topic = "python/mqtt"
client_id = 'mqttx_cc70525f'
username = 'tsmmqttuser'
password = 'ZFjN39bfg4YgCL9d'
# username = 'tsmmqttuser'
# password = 'ZFjN39bfg4YgCL9d'
msg = 'test'
port = 8080



def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print("Send {msg} to topic {topic}")
        else:
            print("Failed to send message to topic {topic}")
            
        client.loop_stop()

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)

if __name__ == '__main__':
    run()
