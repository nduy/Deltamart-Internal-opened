#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is the code for Buyer client to
1. Retrieves status of an establised DCA
2. Subscribes to the DCA
3. Randomly print some received samples
4. Export to JSON File
"""

import re
import os
import sys
import ast
import requests
from termcolor import colored
import pprint

import lib
from lib import *

# Global variables
BuyerID="DDN";  # A dummy user ID of the Buyer
providID_pattern = re.compile('[A-Z0-9]{3}')

dcaID="";  # A dummy Data Collection Activity
dcaID_pattern = re.compile('[a-z0-9]{10}')

def print_logo():
    # Use a breakpoint in the code line below to debug your script.
    with open('delta-logo-ascii-art.txt', 'r') as f:
        for line in f:
           print(colored(line.rstrip(),'blue'))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_logo();
    print(colored( "      === DELTAMART DATA STREAM SUBSCRIBER ===",'red'))
    BuyerID = input("Enter YOUR User ID: ");
    # Validate User name until it is good enough
    '''
    while (providID_pattern.match(BuyerID)== None):
        BuyerID = input("Incorrect Buyer ID, Reenter your UserID: ");

    dcaID = input("Enter ID of the Data Collection Activity (10 characters: ");
    '''
    # Print out inputed data
    print("===========================")
    print("==You entered the following ìnormation")
# print("UserID:{0}ta Collection ID{1}" ".format(BuyerID));
    print("Now looking for establised Data Collection Activity for user {}".format(BuyerID));

x = requests.get('http://dmart.hopto.org/dcaquery.php?BuyerID='+BuyerID);
print("Now parse the results");
print(x.text)
dcaresult = ast.literal_eval(x.text);
print('There are '+str(dcaresult['Count'])+ " DCA established for you (as a Buyer):");
results = dcaresult['Results'];
for i in range(0,dcaresult['Count']):
    print(colored("((-- Index={0}--))".format(i),'blue'))
#    print("* {0}".format(results[i]));###########################OK
    results[i]['Provider.Email']= results[i]['Email']
    results[i].pop('Email')
    results[i]['Provider.Fullname'] = results[i]['Fullname']
    results[i].pop('Fullname')
    results[i]['Provider.IPAddress'] = results[i]['IPAddress']
    results[i].pop('IPAddress')
    results[i]['Provider.ZTNetworkID'] = results[i]['ZTNetworkID']
    results[i].pop('ZTNetworkID')
    results[i]['Provider.UserID'] = results[i]['UserID']
    results[i].pop('UserID')
    results[i]['Provider.Online'] = results[i]['Online']
    results[i].pop('Online')
    pprint.pprint(results[i])
#    print(results[i])


Sellecteddca_index=0
Sellecteddca_index = int(input("Enter index of the Data Collection you want to recieve data (number from 0 to {0}:".format(dcaresult['Count']-1)));
#print(type(Sellecteddca_index))
#print(type(dcaresult['Count']))
while (Sellecteddca_index<0 or Sellecteddca_index>int(dcaresult['Count'])-1):
    Sellecteddca_index = input("[!]Incorrect input. Reenter index of the Data Collection you want to recieve data (number from 0 to {0}:".format(dcaresult['Count']-1));
############################################
listenTime = float(input("Enter the period of time you want to listen to Provider from now (in minutes): "));
# Validate User name until it is good enough
while (listenTime<=0 or listenTime>=60):
    BuyerID = input("Incorrect Buyer ID, Reenter listening time range[0.0,59.99]:");
print(colored("The stream will be saved by the end of the selected time period in \"Output\" Folder  ","magenta"))
fileName = input("Enter  filename to save (Under \"Output\" folder:");

# Now do subscribe LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
print(results[Sellecteddca_index])
Pro_IP= results[Sellecteddca_index]['Provider.IPAddress']
Pro_topic= results[Sellecteddca_index]['MQTTopic']
Pro_id= results[Sellecteddca_index]['Provider.UserID']

samples,start_time,end_time = lib.subscribenExport(Pro_IP,Pro_topic,listen_time=listenTime)

### Write to JSON file
print("SUMMARY===================================================")
print("==Tototal samples received: {0}".format(len(samples)))
json_string = json.dumps(samples)
print("=======================LISTENNED  TO PROVIDER. FROM Local_Time"+(time.strftime('%Y-%m-%d %H:%M:%S.', time.localtime(start_time)))+" TO Local_Time"+time.strftime('%Y-%m-%d %H:%M:%S.', time.localtime(end_time)))
#print(json_string)
#print(colored("The stream will be saved by the end of the selected time period in \"Output\" Folder  ","magenta"))
#fileName= input("Enter  filename to save (Under \"Output\" folder:");

if sys.platform == 'win32':
    fullFileName = "Output\\"+fileName+".json"
else: # Linux and everything else
    fullFileName = "Output/"+fileName+".json"
print("Writing stream to "+fullFileName)

f = open(fullFileName, "w+")
f.write("{")
f.write('\"From_User\":\"'+Pro_id+'\"')
f.write(',\"Local_StartTime\":\"'+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))+'\",'
        +'\"Local_EndTime\":\"'+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))+'\",'
         +" \"Data_Samples\":"+json_string+"}");
f.close()
# print(colored("Program completed.\nYou can now safely turn the program off and see output at {0}".format(fullFileName)),"red")
print(colored("Program completed.\nYou can now safely turn the program off and see output at: ","green"))

if sys.platform == 'win32':
    print(colored(os.getcwd() +'\\'+ fullFileName,"red"))
else: # Linux and everything else
    print(colored(os.getcwd() +'/'+ fullFileName,"red"))

