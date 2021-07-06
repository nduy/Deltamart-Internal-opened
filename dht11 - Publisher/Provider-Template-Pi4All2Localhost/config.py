# This is configuration scripts contains constant regulating the data stream Publishing.

# Provider MQTT hostname or IP
DEST_IP="localhost";

#Name of the MQTT topic under which the stream will be published
TOPIC_NAME="lighthouseDmorning";

#Expected stream rate sample per second
STREAM_RATE=3;

TEST = False;
# SProvider-side data enoding. None by default
#See page 8 of Collectability Cheatsheet
#Value: Natural number (including Zero-0)
ENCODING=7;

"""
    if (scheme_code==0): # No Encoding
        return string;
    elif (scheme_code==1):    #ASCII
        return string.encode('ascii')
    elif (scheme_code==2):    #UTF8
        return string.encode("utf-8")
    elif (scheme_code==3):    #UTF16
        return string.encode("utf-16")
    elif (scheme_code==4):    #UTF16
        return binascii.hexlify(bytes(string, 'utf-8'))
    elif (scheme_code==5):    #Base 16
         return base64.b16encode(bytes(string, 'utf-8'))
    elif (scheme_code==6):    #Base 32
        return base64.b32encode(bytes(string, 'utf-8'))
    elif (scheme_code==7):    #Base 64
        return base64.b64encode(bytes(string))
    else:
        return string
"""

# ID of the Provider (you)
PROVIDER_ID="TPF"
#Verbal level 1,2,3.
VERBOSE = 3

# LIMITS

