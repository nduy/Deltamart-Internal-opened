!pip install paho-mqtt
# coding=utf-8
# This is a sample client  for publishing message to Deltamart Lightsail Broker .

# Press Shift+F10 to execute it or replace it with your code.

import paho.mqtt.client as mqtt;
from datetime import datetime;
import random
import string

from time import sleep

N_SAMPLES=3650;
LOAD_CHAR_SIZE=10;

def id_generator(size=50, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
...
# get_random_string(8)
# get_random_string(8)
#get_random_string(6)
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("panda/test0")

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

    client.connect("52.19.248.189", 1883, 60)

    now = datetime.now()

########### Main code for sending data is here:
    for i in range(0,N_SAMPLES):
        print(i);
        tmp=id_generator(LOAD_CHAR_SIZE, "6793YUIO");
        print(tmp);
        print(tmp);
        dt_string = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3];
        client.publish(topic="delta/test", payload="\n \n=>   Package"+"["+str(i+1)+" of "+str(N_SAMPLES) +"]"+"\n| Time:"+dt_string+ " ,| Load:"+ tmp);
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