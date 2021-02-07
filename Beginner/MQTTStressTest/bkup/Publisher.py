# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.

import paho.mqtt.client as mqtt;
from datetime import datetime;
import random
from time import sleep

topic="panda/test0";
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Press the green button in the gutter to run the script.


#######################################
if __name__ == '__main__':

    client=mqtt.Client()
    subclient = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("127.0.0.1", 1883, 60)

    now = datetime.now()


    for i in range(0,1024):
        print(i);
        dt_string = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3];
        client.publish(topic=topic, payload="["+str(i)+"]"+"\n"+dt_string);
        #sleep(random.uniform(0,0.5));

    #subclient.subscribe()


    print ("Exiting the  script");
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
