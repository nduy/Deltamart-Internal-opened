# -*- coding: utf-8 -*-
"""
Supporting functions for  the Subscriber
"""
import paho.mqtt.client as mqtt
import time
import json
import base64
rs=[]
dst_topic="#"
selected_decoding_method=0
def on_connect(client, userdata, flags, rc,qos=0):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#", qos=0)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    # Decode message:
    decoded_payload = decode_message(msg.payload,selected_decoding_method)
    print("Decoded--->"+str(decoded_payload));
    rs.append(str(decoded_payload))
    n_sample=len(rs)
#    print("^^^Received {0} samples".format(str(n_sample)))
    if (n_sample % 100 ==0):
        print("^^^Received {0} samples".format(str(n_sample)))
        print("latest sample: {0}".format(decoded_payload))

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

def decode_message(encrypted_message="",decode_method=0):
    '''
    :param encrypted_message:(squece of byte-like string: b'something') The message encrypted by some methods
    :param decode_method: an Integer code of the decoding method:

    byte_string = b"\x61\x62\x63\xc3\xa1"
    (((0))): Do nothing, just return the original message
    (((1))): ASCII: e.g result:ERR 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
    UTF-8: UTF-8 E.g.'abcá'
      (((2))): utf-8: e.g result:ERR 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
    UTF-8: UTF-8 E.g. E.g: b"\x61\x62\x63\xc3\xa1" to 'abcá'.
    (((3))): UTF16. E.g result : UnicodeDecodeError: 'utf-16-le' codec can't decode byte 0xa1 in position 4: truncated data
             b'\xff\xfea\x00b\x00c\x00' to 'abc'
    (((4))) UTF32: UTF32. E.g: b'\xff\xfe\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00' to 'abc'
    (((5))) Base16: Base16.E.g: b'616263' to 'abc'
    (((6))) Base32: E.g. b"MFRGG===" to 'abc'
    (((7))) Base64. E.g: b"YWJj" to 'abc'
    (((8))) Base85. E.g.b"@:E^" to 'abc'

    :return:
    plain text <class 'str')at arbitrary length.
    '''

    if (decode_method==0): # Do nothing
        return encrypted_message;
    elif decode_method==1: # ASCII
        return encrypted_message.decode('ascii');
    elif (decode_method==2): #UTF8
        return encrypted_message.decode('utf8');
    elif (decode_method==3): #UTF16
        return encrypted_message.decode('utf16');
    elif(decode_method == 4): #UTF32
        return encrypted_message.decode('utf32');
    elif(decode_method == 4): # Base16
        return base64.b16decode(encrypted_message);
    elif(decode_method == 5): # Base32
        return base64.b32decode(encrypted_message);
    elif(decode_method == 6): # Base64
        return base64.b64decode(encrypted_message);
    elif(decode_method == 7):
        return base64.b85decode(encrypted_message);
    else:
        return encrypted_message
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
