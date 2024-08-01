#!/bin/bash
# This is the namenode backup script.  The script assumes it is running on a gateway with the default configuration of the cluster namenode to backup.
# Most recent Author: Julie Gay
# Run Example:  /usr/local/bin/scripts/backupNameNode.sh -s DSC1 -t MSC1 -d /opt/oclc/backups/namenode -m 4

# cron gets its path from /etc/crontab.  If this is not in cron, the PATH specification is not needed.
PATH=/usr/lib64/qt-3.3/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/opt/dell/srvadmin/bin:/bin:/home/cloudera-scm/bin:/usr/java/jdk1.8/bin
echo $PATH
EMAIL_LIST='DBA-Hadoop-Support@oclc.org'
#EMAIL_LIST='gay@oclc.org'
#set -x
usage()
{
   echo "

     backupNameNode.sh Backup name node for Hadoop cluster
     examples:

     Usage:

     -s Required: {SYSTEM NAME to backup}  The name of the cluster that you are backing up
                       ex: DEV1, PROD1, PROD2

     -t Optional: {Remote cluster to backup to } name of cluster you are backing up to
                       ex: DEV1, PROD1, PROD2
     
     -h {Help}

     -d Required {local directory to put backup} - 
                like  /home/cloudera-scm/backups or /opt/oclc/backups/namenode 
 
     -e Optional {HDFSBASEDIR} - HDFS directory to use on remote cluster}
                 Default is /backups/namenode 

     -m Required {MAX_DAYS] - max days to keep backups in hdfs

     -n Optional {LOCAL_MAX_DAYS} Number of days to keep local backups Default is 1 day

   "
}
GOODPARMS="FALSE"

while getopts s:t:m:n:d:e:h  name
 do
    case $name in
    s)      SYSTEM="$OPTARG";;
    t)      CLUSTER="$OPTARG";;
    m)      MAX_DAYS="$OPTARG";;
    n)      LOCAL_MAX_DAYS="$OPTARG";;
    e)      HDFSBASEDIR="$OPTARG";; 
    d)      DIRECTORY="$OPTARG"
            GOODPARMS="TRUE";;
    h)      GOODPARMS="FALSE";;
    ?)      echo "Invalid Option Specified: $name"
            GOODPARMS="FALSE";;
    esac
 done

echo SYSTEM is $SYSTEM
echo Remote CLUSTER is $CLUSTER
echo HDFS Directory is $HDFSBASEDIR
echo MAX_DAYS is $MAX_DAYS
echo LOCAL MAX DAYS is $LOCAL_MAX_DAYS
echo DIRECTORY is $DIRECTORY
echo GOODPARMS is $GOODPARMS

if [ "X$SYSTEM" = "X" ]
then
   echo System is required
   GOODPARMS="FALSE"
fi

#[ ! -z "$CLUSTER" ] && echo "Not empty" || echo "Empty"

if [  -z "$CLUSTER" ]
then
   echo "No secondary CLUSTER specified so NOT backing up to another cluster"
fi

if [ "X$DIRECTORY" = "X" ]
then
   echo DIRECTORY is required
   GOODPARMS="FALSE"
fi

if [ "X$MAX_DAYS" = "X" ]
then
  echo MAX_DAYS is required
  GOODPARMS="FALSE"
fi

if [ "X$LOCAL_MAX_DAYS" = "X" ]
then
  LOCAL_MAX_DAYS=1
  echo "LOCAL_MAX_DAYS is set to default of $LOCAL_MAX_DAYS"
fi

if [ "$GOODPARMS" = "FALSE" ]
then
   usage
   exit 1   
fi

# get namenode for remote cluster if specified
if [ ! -z "$CLUSTER" ];then
#   REMOTEURL=$(/home/gay/get_namenode.sh ${CLUSTER})
   REMOTEURL=$(get_namenode.sh ${CLUSTER})
   ERROR=$?
   echo "Error returned " $ERROR
   echo "Remote URL "$REMOTEURL

   if [ -z "$REMOTEURL" ]
      then
      echo $CLUSTER" Is returning empty not backing up remotely"
      CLUSTER=""
      REMOTEURL=""     
   elif [ "$REMOTEURL" = "Invalid Cluster!" ]
      then
      echo $CLUSTER" is invalid not backing up remotely"
      CLUSTER=""
      REMOTEURL=""
   fi
fi

echo "Remote cluster namenode is "$REMOTEURL

DATE=`date +'%Y%m%d' -d "${MAX_DAYS} days ago"`
TIMESTAMP=`date +%Y%m%d_%H%M%S`
LOCALBACKUPDIR=$DIRECTORY/$SYSTEM/$TIMESTAMP

if [ -z "$HDFSBASEDIR" ]
  then
    echo "HDFSBASEDIR is blank so setting to /backups/namenode"
    HDFSBASEDIR="/backups/namenode/"    
  fi

if [ ! -d "$LOCALBACKUPDIR" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
  mkdir -p $LOCALBACKUPDIR
  if [ $? -ne 0 ]; then
      echo "Failed to create $LOCALBACKUPDIR"
      exit 1
  fi
fi
echo $LOCALBACKUPDIR

#Delete local backups
echo "deleting these files from $DIRECTORY/$SYSTEM older than $LOCAL_MAX_DAYS"

find $DIRECTORY/$SYSTEM -type d -ctime $LOCAL_MAX_DAYS   -print
#find $DIRECTORY/$SYSTEM -type d -ctime +$LOCAL_MAX_DAYS  -exec rm -rf {} \; -print
find $DIRECTORY/$SYSTEM -type d -ctime $LOCAL_MAX_DAYS  -exec rm -rf {} \;

#get the image
hdfs dfsadmin -fetchImage $LOCALBACKUPDIR 
if [ $? != 0 ]
  then
    echo "namenode image fetch failed"
    exit 1
  fi 

LATESTBACKUP=`ls -1 $LOCALBACKUPDIR`
echo "LATEST BACKUP: $LATESTBACKUP"

#Put a timestamp on it and zip it
mv $LOCALBACKUPDIR/$LATESTBACKUP $LOCALBACKUPDIR/${LATESTBACKUP}_${TIMESTAMP}
gzip $LOCALBACKUPDIR/*

BACKUPFILE="${LATESTBACKUP}_${TIMESTAMP}.gz"
echo "Latest backup "$BACKUPFILE 

#Put this file into hdfs local for move
echo $LOCALBACKUPDIR/$BACKUPFILE

#Ports are different for CDH 5 and CDH 6 so checking version
VERSION=$(hdfs version | grep cdh5)
echo $VERSION
if [ -z "$VERSION" ]
then
   echo "not version 5, so assume version 6 or greater"
   VERSION=6
   PORT=9870
else
   echo "version is 5 - use version 5 ports"
   VERSION=5
   PORT=50070
fi
echo $VERSION
echo $PORT

# if there is a remote cluster specified
# check for the backup directory and then backup directory/system
# if they do not exist create them 

if [ ! -z "$CLUSTER" ]; 
then

   echo "backing up to remote cluster"
   # First change the namenode to the webhdfs url
   WEBHDFSHOST=$(echo $REMOTEURL | sed 's/hdfs:\/\///g')
   echo $REMOTEURL
   echo $WEBHDFSHOST
   # replace the port based on the version of CDH   
   WEBHDFSHOST=$(echo $WEBHDFSHOST | sed  "s/8020/$PORT/g")
   
   echo $WEBHDFSHOST
   # Testing the failure
   hdfs dfs -ls -d webhdfs://$WEBHDFSHOST/$HDFSBASEDIR 
   if [ $? -ne 0 ]; then
      echo "Making Remote HDFS Directory webhdfs://$REMOTEURL/$HDFSBASEDIR"
      hdfs dfs -mkdir webhdfs://$WEBHDFSHOST/$HDFSBASEDIR
      if [ $? -ne 0 ]; then
         echo "Local backup successful - Access to "$CLUSTER $WEBHDFSHOST " failed - not failing job " |  mail -s "$SYSTEM remote Namenode backup to $CLUSTER failed " ${EMAIL_LIST}
         exit 0 
      fi
   fi

#   hdfs dfs -ls -d webhdfs://$WEBHDFSHOST/$HDFSBASEDIR/$SYSTEM  >/dev/null 2>&1
   hdfs dfs -ls -d webhdfs://$WEBHDFSHOST/$HDFSBASEDIR/$SYSTEM  
   if [ $? -ne 0 ]; then
      echo "Making Remote HDFS Directory webhdfs://$WEBHDFSHOST/$HDFSBASEDIR/$SYSTEM"
      echo webhdfs://$WEBHDFSHOST/$HDFSBASEDIR/$SYSTEM
      hdfs dfs -mkdir webhdfs://$WEBHDFSHOST/$HDFSBASEDIR/$SYSTEM
      if [ $? -ne 0 ]; then
         echo "Local backup successful - Failed to create webhdfs://$HDFSBASEDIR/$SYSTEM. Not failing job" | mail -s "$SYSTEM Remote Namenode backup to $CLUSTER failed " ${EMAIL_LIST}
         exit 0
      fi
   fi
   echo "remote directory created"

   # move the backup to a remote cluster specified

   hdfs dfs -copyFromLocal $LOCALBACKUPDIR/$BACKUPFILE  webhdfs://$WEBHDFSHOST/$HDFSBASEDIR/$SYSTEM
   if [ $? -ne 0 ]; then
     echo "Local backup successful but copy to remote cluster failed webhdfs://$WEBHDFSHOST/$HDFSBASEDIR/$SYSTEM Not failing job" | mail -s "$SYSTEM remote Namenode backup to $CLUSTER failed " ${EMAIL_LIST}
     exit 0
     fi

   # remove remote backups older than maxdays from remote cluster

   echo "Clearing remote hdfs directory older than $MAX_DAYS days"
   days_diff=$MAX_DAYS
   now=$(date +%s)
   hdfs dfs  -ls webhdfs://$WEBHDFSHOST/$HDFSBASEDIR/$SYSTEM | while read f; do
     dir_date=`echo $f | awk '{print $6}'`
     filename=`echo $f | awk '{print $8}'`
     difference=$(( ( $now - $(date -d "$dir_date" +%s) ) / (24 * 60 * 60 ) ))
     if [ $difference -gt $days_diff ]; then
       echo "Deleting file:" $filename ;
       hdfs dfs  -ls  $filename;
       hdfs dfs  -rm $filename;
     fi
   done
   echo "all done with remote cluster"
fi
echo "all done"
exit

