# Script Name: Foreigner_Classification_A.py 
# Script Details: This script uses the input Foreigner_Classification.ini file and generates the ULI data based on the inputs. 
# Script Release Date: 2019-11-21
# Script Version : Foreigner_Classification_A_V1.3
# Changes : Added Uniq IMSI File generation Logic -V1.1
# Changes : changed Foreign_Configuration.ini file with buffer duration and naming convention - V1.2
# Changes : Changed Buffer time from hours to minutes
import csv
from ConfigParser import SafeConfigParser
import socket
import json
import time
import glob
from multiprocessing import Process
from datetime import datetime, timedelta
from dateutil import parser
import os
import sys
import shutil

Example1 = (
    "Usage:python Foreign_Classification.py <config.ini>"
    "\n"
    "E.G:"
    "\n"
    "\n"
    "python Foreign_Classification_A_V1.2.py Foreign_classification.ini")

if len(sys.argv) < 1:
    print("Incorrect arguments Passed.Please refer the example below and retry")
    print
    print Example1
    sys.exit()



parser = SafeConfigParser()
parser.read(sys.argv[1])

countries = parser.get('Values','List_of_Foreign_Country_Codes').split(',')
#print countries
bdsp_ip = parser.get('Values','Bdsp_CIF_ip').strip()
#print bdsp_ip
bdsp_port = int(parser.get('Values','BDSP_CIF_port').strip())
#print bdsp_port
uniqueImsiCount = parser.get('Values','uniqueImsiCount').strip()
number_of_hours = parser.get('Values','Query_duration').strip()
dest_dir = parser.get('Values','Output_Directory').strip()
buffer = parser.get('Values','Buffer_Duration').strip()
a = datetime.now() - timedelta(minutes=int(buffer))
end_time = a.strftime('%Y%m%d%H%M%S')
end_time_file = a.strftime('%Y%m%d%H')
b = a - timedelta(hours=int(number_of_hours))
start_time = b.strftime('%Y%m%d%H%M%S')

message = {"authToken": "polaris1", "outputMessageFormat": "csv", "notificationPort": 1179, "massFilter": {"cgi": [], "imeis": [], "countries": countries, "days": [], "rat": [], "subscriberTypes": [], "eventGroup": "", "subEventTriggers": [], "switchAddresses": [], "imsis": [], "eventTypes": [], "networkNames": [], "msisdns": []}, "messageType": "sqr", "serviceName": "massSearch", "startTime": start_time, "uniqueImsiCount": uniqueImsiCount, "endTime": end_time}
statmsg = {"authToken": "polaris1", "messageType": "sqstr"}

def intToBytes(n):

    b = bytearray([0, 0, 0, 0])  # init
    b[3] = n & 0xFF
    n >>= 8
    b[2] = n & 0xFF
    n >>= 8
    b[1] = n & 0xFF
    n >>= 8
    b[0] = n & 0xFF
    return b

def bytes_to_int(b, offset):
    n = (b[offset + 0] << 24) + (b[offset + 1] << 16) + (b[offset + 2] << 8) + b[offset + 3]
    return n

def TCP_Connection(message,bdsp_ip,bdsp_port):

    s = socket.socket()
    s.connect((bdsp_ip,int(bdsp_port)))
    message["notificationIpAddress"]=s.getsockname()[0]
    print message
    s.send(intToBytes(len(json.dumps(message))))
    s.send(json.dumps(message))
    dataack = s.recv(4)
    b = bytearray()
    b.extend(dataack)
    dataack = s.recv(1024)
    resp2 = json.loads(dataack)
    return resp2

def End_notification():
    client_socket = socket.socket()
    client_socket.bind(('', 1179))
    client_socket.listen(30)
    while True:
        c, addr = client_socket.accept()
        notification_resp = c.recv(1024)
        b = bytearray()
        b.extend(notification_resp)
        datalen = bytes_to_int(b, 0)
        data = c.recv(datalen)
        print data
        notify_data = json.loads(data)
        stat = notify_data["status"]
	ftp_status = notify_data["ftpStatus"]

        if stat == 'CompletedWithSuccess':
		if ftp_status == 'Completed':
		
            		filename_rename(data)

def submit_request(message):
    Request_resp = TCP_Connection(message,bdsp_ip,bdsp_port)
    print Request_resp
    server_session_id = Request_resp['serverSessionId']
    status = Request_resp['status']
    if status == 'Ongoing':
        threadname = Process(target=End_notification)
        threadname.start()
    statmsg["serverSessionId"] = server_session_id
    time.sleep(2)
    while status == 'Ongoing':
	time.sleep(2)
        status_resp = TCP_Connection(statmsg,bdsp_ip,bdsp_port)
        status = status_resp['status']
        time.sleep(2)
    threadname.terminate()

def filename_rename(data):
    global dest_dir
    count = 1
    with open(dest_dir+'/'+'endtime.txt','w') as et:
        et.write(end_time_file)
    # final_folder = 'Foreign_output_'+end_time
    notification_data = json.loads(data)
    out_folder = notification_data["resultPath"]["ftpPushFolder"]
    uniq_out_folder = out_folder+'/uniqueimsis'
    for filename in os.listdir(out_folder):
    	if filename.endswith('.csv'):
            # os.system(mkdir -p out_folder+'/'+final_folder)
            os.system('cp '+out_folder+'/'+filename+' '+dest_dir)
            os.rename(dest_dir+'/'+filename, dest_dir+'/'+'ULI-'+end_time_file+'-'+str(count)+'.csv')
	    count+=1
    for f1 in os.listdir(uniq_out_folder):
        if f1.startswith('uniquelist'):
            os.system('cp '+uniq_out_folder+'/'+f1+' '+dest_dir)
            os.rename(dest_dir+'/'+f1, dest_dir+'/'+'SUB-'+end_time_file+'-'+str(count)+'.csv')
#    os.rename(dest_dir+'/'+filename, dest_dir+'/'+'UniqueIMSI_'+end_time+'.csv')


submit_request(message)
