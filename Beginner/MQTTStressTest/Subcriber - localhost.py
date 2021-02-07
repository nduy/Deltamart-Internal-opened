import paho.mqtt.client as mqtt
import datetime;
topic= "panda/test0";
latest_time= 1;
current_avg_interval=0.0
#####################################
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("New message");
    print("["+msg.topic+"]"+" "+str(msg.payload))
    now= datetime.now()
    dt_string=now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3];
    print(dt_string);
    print("\n_______ "+latest_time);
    if latest_time is not None:
        delta_time=timeStamp-latest_time
        print(delta_time);
        current_avg_interval= (current_avg_interval+ delta_time.total_seconds())/2
    else:
        print("Entered");
        latest_time=timeStamp;        
    print("["+msg.topic+"]"+" "+str(msg.payload))
    print("\n===>Average interval:"+current_avg_interval) 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("127.0.0.1", 1883, 10)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
print("-")
client.loop_forever()
print("===")