#!/usr/bin/python
# This script will pull FBI files from APP1 Node and copy it to "previous day" directory under /Disk and then Compress the dir, Once Compression is done it will delete that directory 
# The Count of Number of files which it has pulled using ftp to the previous day Directory will be appeneded to a log file "FBI_Archival_COunt.log" under /home/hduser/
#10-01-2019 - changed code instead of ftp, we changed to copy command to copy in the same node QNAP mount point /archive
#@Sasidhar
from datetime import datetime, timedelta
import glob
import os
import time
#from ftplib import FTP
import shutil
import tarfile
import logging as log
s_dir = '/archive1/'
fbi_dir = '/mnt2/FBIFilesBackupDir/'
log.basicConfig(filename='FBI_Archival_Count.log', level=log.DEBUG)
a = datetime.now() - timedelta(days=1)
b = a.strftime('%Y%m%d')
c = a.strftime('%Y-%m-%d')

filelist = glob.glob('/mnt2/FBIFilesBackupDir/*-*-*-*-*-'+b+'*.xml')
with open('/home/hduser/smp/FBI_filenames.txt', 'w') as fileobj:
	log.info('Number of FBI files count '+str(len(filelist)) + ' for the day : '+str(c))
	for filename in filelist:
		filename = filename.split('/')[-1]
		fileobj.write(filename+'\n')
time.sleep(3)
os.system('mkdir -p'+' '+s_dir+b)
with open('/home/hduser/smp/FBI_filenames.txt') as f:
	for filename in f:
		filename = filename.strip()
		shutil.copy(fbi_dir+str(filename), s_dir+b)
filelist1 = glob.glob('/archive1/'+b+'/*-*-*-*-*-'+b+'*.xml')
log.info('Count of FBI files Pulled from App1 node for the day : '+str(c)+' is '+str(len(filelist1)))
os.chdir('/archive1/')
os.system('tar -czf'+' '+b+'.tar.gz'+' '+b)
time.sleep(10)
os.system('rm -rf'+' '+b)
