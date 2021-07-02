"""
Supporting functions for  the Subscriber
"""
import paho.mqtt.client as mqtt
import time
import json

rs=[]
dst_topic="#"
def on_connect(client, userdata, flags, rc,qos=0):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#", qos=0)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))
    rs.append(str(msg.payload))
    n_sample=len(rs)
    print("^^^Received {0} samples".format(str(n_sample)))
    if (n_sample % 100 ==0):
        print("^^^Received {0} samples".format(str(n_sample)))
        print("latest sample: {0}".format(msg.payload))

#    print(rs)

def subscribenExport(dst_host="test.mosquitto.org",dst_topic="#",listen_time=3):
    """
    Subscribe to thde dest_host under dest_topic with qos
    Params:
    1. dst_host: destination hostname or IP of the destination MQTT Broker
    2. dst_topic: MQTT topic to subscribe
    3. qos: Quality of service
    4.listen_time: The yime to listen to the Provider: IN MINUTE

    Returns:
    1. Nothing, message is appened to global variable rs

    """
    dst_topic=dst_topic
    print(">>Subscribing to [{0}] under topic of \"{1}\" in {2} minutes".format(dst_host,dst_topic,listen_time));
# The callback for when the client receives a CONNACK response from the server.
    startTime = time.time()
    endTime= startTime;
    runTime = listen_time * 60 # Runtime of 3 seconds

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(dst_host, 1883, 10)
    while True:
        client.loop()
        currentTime = time.time()
        if (currentTime - startTime) > runTime:
            endTime= time.time()
            break
    return (rs,startTime,endTime)
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#    client.loop_forever(timeout=0.01,max_packets=100)
#    client.loop(timeout=0.5)

if __name__ == '__main__':
    samples,start_time,end_time=subscribenExport("test.mosquitto.org","#",listen_time=0.1)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    print("SUMMARY===================================================")
    print("{0} samples received".format(len(samples)))
    json_string = json.dumps(samples)
    print("=======================JSON STR"+(time.strftime('%Y-%m-%d %H:%M:%S.', time.localtime(start_time)))+"->"+time.strftime('%Y-%m-%d %H:%M:%S.', time.localtime(end_time)))
    #print(json_string)

    f = open("Outputfile.json", "w")
    f.write("{\"data\"\\:"+json_string+"}")
    f.close()
