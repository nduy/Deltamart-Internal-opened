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

#    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

#######################################
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
if __name__ == '__main__':

    client=mqtt.Client()
    subclient = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)
    while True:

        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        print( humidity, temperature);
   #     now = datetime.now()
   #     current_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3];
   #     print ('Timestamp:{0} {}Data:{Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(current_time,temperature, humidity)
    
        
        now = datetime.now()

        current_time = now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3];
        print(" Time =", current_time)
    #    load='{'+ '"'+'+Time":'+ current_time +',"Temperature"'+': {0:0.1f} ,"Humidity": {1:0.1f} %'.format(temperature,humidity)+'}';
        header='{\"ProviderID\":\"TPT\"'
#	header='{ \"ProviderID\":\"TPT\"'
        dt=",\"data\":{"+ '\"Temprature":{0:0.1f},"Humidity":{1:0.1f}'.format(temperature, humidity)+'}}'
        print(dt);
        load=dt; 

#        load= ',"utc_time":"' + current_time+'"'+",\data\:"+"{"+ "\"Temprature":{0:0.1f},"Humidity":{1:0.1f}'.format(,temperature, humidity)+'}}';
        load=header+load;
        print(load);
        client.publish(topic="soundtrackDdepth", payload=load);
        print("=>Published:\n"+load);
 

