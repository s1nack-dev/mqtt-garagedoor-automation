import time
from gpiozero import *
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt

garage_open = OutputDevice(4)
garage_open.on()
garage_open.off()
garage_open.close

def on_connect( client, userdata, flags, rc):
    print ("connected with code:" +str(rc))
    client.subscribe("garage/switches/door")

def on_message( client, userdata, msg):
    print("triggering garage")
    garage_open.on()
    time.sleep(2)
    garage_open.off()
    time.sleep(1)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt_broker_ip_goes_here", 1883, 60)
client.username_pw_set("mqtt_username", "mqtt_password")

# This allows the connection to stay connected.
# Continues loop to run forever
client.loop_forever()