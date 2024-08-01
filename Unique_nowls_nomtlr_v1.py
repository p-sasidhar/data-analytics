#!/usr/bin/python
"""
Created on Fri Jul 27 17:00:27 2018

@author: sasidhar.p
"""
import csv
import sys
import os
import time
from datetime import datetime
import subprocess

Example = ("Usage:python Unique_nowls_nomtlr.py <Mass query output folder>"
"\n"
"E.G:"
"\n"
"\n"
"python Unique_nowls_nomtlr.py mass_ouput")


if len(sys.argv) != 2:
    print("Number of arguments should be 1")
    print
    print Example
    sys.exit()
mass_output = sys.argv[1]

testname = raw_input('Please enter the directory name where output files needs to be copied:')
if not os.path.isfile(testname) and not os.path.isdir(testname):
     os.mkdir(testname)
testPath=os.getcwd()+'/'+testname
no_wls_imsi_om = {}
no_wls_imsi_or = {}
no_wls_imsi_fr = {}
no_mtlr_imsi_om = {}
no_mtlr_imsi_or = {}
no_mtlr_imsi_fr = {}
mtlr_imsi_om = {}
mtlr_imsi_or = {}
mtlr_imsi_fr = {}
wls_imsi_om = {}
wls_imsi_or = {}
wls_imsi_fr = {}
set_imsi_om = {}
set_imsi_or = {}
set_foreign_imsi = {}
start_time = time.time()

def parse_file():
    global total_records
    total_records = 0
    for f_name in os.listdir(mass_output):
        if f_name.endswith(".csv"):
            with open(mass_output+'/'+f_name) as f:
                csvReader = csv.reader(f, delimiter=',')
                for line in csvReader:
                    ln = csvReader.line_num
                    if ln == 1:
                        continue

                    total_records += 1
                    imsi = line[0]
                    loc = line[4]
                    event = line[9]
                    htime = line[8][:-5]
                    htime_sec = datetime.strptime(htime,"%Y%m%d%H%M%S")
        #        print htime_sec
                    h1 = int(time.mktime(htime_sec.timetuple()))
        #        print h1
        #        h1 = int(h1)
        #        print h1
        #        h_hour = h1 // 3600 % 24
        #        print h_hour
                    carrier = line[12]


                    unique_set_imsi_om(imsi,carrier)
                    unique_set_imsi_or(imsi,carrier)
                    unique_no_wls_imsi(imsi,carrier,loc)
                    unique_no_mtlr_imsi(imsi,carrier,event)
                    create_file(imsi,h1,event)
    read_files()

def create_file(imsi,h1,event):

    if event == 'MT LR':
        with open(testPath+'/'+imsi+".txt" ,'a+') as f:
            f.write(str(h1) + "\n")

def read_files():

    for file in os.listdir(testPath):

        if file.endswith(".txt"):
            s_imsi = []
            file_handle = open(testPath+"/"+file, "r")
            for line in file_handle:
                s_imsi.append(line)
            _sorted = sorted(s_imsi)
            fincounter(file, _sorted)

def fincounter(filename, sorted):
    #print(filename + ":" + str(len(sorted)))
    count_mtlr = 0
    count_nonmtlr = 0
    for i in range(1, len(sorted)):
#        print i
#        print(filename + ":" + sorted[i] + ":" + sorted[i-1] + "::::"+ str(int(sorted[i]) - int(sorted[i-1])))
#        if(int(sorted[i][8:12]) - int(sorted[i-1][8:12])> 14400):
        if(int(sorted[i]) - int(sorted[i-1]) >= 10800) and (int(sorted[i]) - int(sorted[i-1]) < 16200):
            count_mtlr+=1
        else:
            count_nonmtlr += 1
    imsi = filename[:-4]
    _str = imsi +","+str(count_mtlr) + ","+str( count_nonmtlr)
#    print(_str)
    with open(testPath+"/MTLR_Output", "a+") as fo:
        fo.write(_str+"\n")

def unique_set_imsi_om(imsi,carrier):
    if carrier == "OM":
        if imsi.startswith("42202"):
#	    set_imsi_om.add(imsi)
            set_imsi_om[imsi] = imsi
#	    print set_imsi_om


def unique_set_imsi_or(imsi,carrier):
    if carrier == "NW":
        if imsi.startswith("42203"):
            set_imsi_or[imsi] = imsi

    if not imsi.startswith("42202") and not imsi.startswith("42203"):
        set_foreign_imsi[imsi] = imsi


def unique_no_mtlr_imsi(imsi,carrier,event):
    if carrier == "OM":
        if imsi.startswith("42202"):
            if event != 'MT LR':
                if imsi not in mtlr_imsi_om:
                    no_mtlr_imsi_om[imsi] = imsi

            else:
                mtlr_imsi_om[imsi] = imsi
                if imsi in no_mtlr_imsi_om:
                    no_mtlr_imsi_om.pop(imsi)
    if carrier == "NW":
        if imsi.startswith("42203"):
            if event != 'MT LR':
                if imsi not in mtlr_imsi_or:
                    no_mtlr_imsi_or[imsi] = imsi

            else:
                mtlr_imsi_or[imsi] = imsi
                if imsi in no_mtlr_imsi_or:
                    no_mtlr_imsi_or.pop(imsi)

    if not imsi.startswith("42202") and not imsi.startswith("42203"):
        if event != 'MT LR':
                if imsi not in mtlr_imsi_fr:
                    no_mtlr_imsi_fr[imsi] = imsi

        else:
            mtlr_imsi_fr[imsi] = imsi
            if imsi in no_mtlr_imsi_fr:
                no_mtlr_imsi_fr.pop(imsi)


def unique_no_wls_imsi(imsi,carrier,loc):
    if carrier == "OM":
        if imsi.startswith("42202"):
            if loc != 'WLS':
                if imsi not in wls_imsi_om:
                    no_wls_imsi_om[imsi] = imsi

            else:
                wls_imsi_om[imsi] = imsi
                if imsi in no_wls_imsi_om:
                    no_wls_imsi_om.pop(imsi)
    if carrier == "NW":
        if imsi.startswith("42203"):
            if loc != 'WLS':
                if imsi not in wls_imsi_or:
                    no_wls_imsi_or[imsi] = imsi

            else:
                wls_imsi_or[imsi] = imsi
                if imsi in no_wls_imsi_or:
                    no_wls_imsi_or.pop(imsi)
    if not imsi.startswith("42202") and not imsi.startswith("42203"):
        if loc != 'WLS':
                if imsi not in wls_imsi_fr:
                    no_wls_imsi_fr[imsi] = imsi

        else:

            wls_imsi_fr[imsi] = imsi
            if imsi in no_wls_imsi_fr:
                no_wls_imsi_fr.pop(imsi)


parse_file()
with open(testPath+'/Unique_Output' , 'w') as f1:
    f1.write('--------------------------------------'+'\n')
    f1.write("Total records : " +str(total_records) +'\n')
    f1.write('--------------------------------------'+'\n')
    f1.write('    Domestic Omantel Subscribers          '+'\n')
    f1.write('--------------------------------------'+'\n')
    f1.write('UNIQUE IMSIs for Omantel Carrier : '+str(len(set_imsi_om.keys()))+'\n')
    f1.write("Unique IMSI's with no MTLR : " +str(len(no_mtlr_imsi_om.keys()))+'\n')
    f1.write("Unique IMSI's with no WLS : " +str(len(no_wls_imsi_om.keys()))+'\n')
    f1.write('--------------------------------------'+'\n')
    f1.write('    Domestic Ooredoo Subscribers          '+'\n')
    f1.write('--------------------------------------'+'\n')
    f1.write('UNIQUE IMSIs for Ooredoo Carrier : ' +str(len(set_imsi_or.keys()))+'\n')
    f1.write("Unique IMSI's with no MTLR : " +str(len(no_mtlr_imsi_or.keys()))+'\n')
    f1.write("Unique IMSI's with no WLS : " +str(len(no_wls_imsi_or.keys()))+'\n')
    f1.write('--------------------------------------'+'\n')
    f1.write('    Foreign Subscribers          '+'\n')
    f1.write('--------------------------------------'+'\n')
    f1.write('UNIQUE Foreign IMSIs : ' +str(len(set_foreign_imsi.keys()))+'\n')
    f1.write("Unique IMSI's with no MTLR : " +str(len(no_mtlr_imsi_fr.keys()))+'\n')
    f1.write("Unique IMSI's with no WLS : " +str(len(no_wls_imsi_fr.keys()))+'\n')
'''
print "Total records : " , str(total_records)
print 'UNIQUE IMSIs for Omantel Carrier : ' , len(set_imsi_om.keys())
print 'UNIQUE IMSIs for Ooredoo Carrier : ' , len(set_imsi_or.keys())
print 'UNIQUE Foreign IMSIs : ' , len(set_foreign_imsi.keys())
print "Unique IMSI's with no MTLR : " , len(no_mtlr_imsi.keys())
print "Unique IMSI's with no WLS : " , len(no_wls_imsi.keys())
# print hour_mtlr_imsi.keys(), hour_mtlr_imsi.values()
#print sorted(hour_mtlr_imsi.keys()), sorted(hour_mtlr_imsi.values())
# for key,value in hour_mtlr_imsi.iteritems(), key=lambda (k,v): (v,k)):
#     print (key,value)
#print set_imsi_om.keys()
'''
elapsed_time_secs = time.time() - start_time
print "Execution completed in",elapsed_time_secs,"seconds"

