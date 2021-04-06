#!/usr/bin/python
import sys
import Adafruit_DHT
import paho.mqtt.client as mqtt;
from datetime import datetime;
import random;
import string;
from datetime import datetime


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

#while True:

#    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

#    print 'Temp: {0:0.1f}   Humidity: {1:0.1f} %'.format(temperature, humidity)

#######################################
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
if __name__ == '__main__':

    client=mqtt.Client()
    subclient = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("52.19.248.189", 1883, 60)
    while True:

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        print( humidity, temperature);

    #    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    
        
        now = datetime.now()

        current_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3];
    #  
    #    load='%s %s %s"%(current_time,str(temperature),str(humidity))
        load ="{'sensor':"+ "'DHT11',"+"'time':"+current_time+",'temperature':"+ str(temperature)+", 'humidity':"+str(humidity)+"}"
    #    load= '{' + current_time+',{0:0.1f},{1:0.1f} '.format(temperature, humidity);
        load="{'time': '%s','sensor':'DHT11','temperature': %s, 'humidity': %s }"%(current_time,str(temperature),str(humidity))
    #    load= "{'a':0,'b':1,'c':2}"
        print(load);
        client.publish(topic="delta/dht11", payload=load);
        print("=>Published:\n"+load);
 

