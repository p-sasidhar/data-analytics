#!/bin/bash
#source /home/hduser/smp/conf/env.sh
pid_file_smp='/home/hduser/smp/pid-dir/hbase-hduser-regionserver.pid'
curpid=`ps -ww -eo pid,lstart,user,euid,cmd | grep "org.apache.hadoop.hbase.regionserver" | grep -v "grep" | awk '{print $1,$2,$3,$4,$5,$6}'`
if [ -n "$curpid" ]; then
echo On this Date: `date` "-> RegionServer running with PID:" "$curpid".
elif [ -z "$curpid" ]; then
echo Removing pid file: `rm $pid_file_smp`
/home/hduser/smp/hbase-1.3.1/bin/hbase-daemon.sh start regionserver 2>&1
sleep 8
curpid=`ps -ww -eo pid,lstart,user,euid,cmd | grep "org.apache.hadoop.hbase.regionserver" | grep -v "grep" | awk '{print $2,$3,$4,$5,$6}'`
        if [ -f "$pid_file_smp" ]; then
                echo On this Date: `date` "-> RegionServer started with PID:" `cat $pid_file_smp` && echo $curpid
        fi
echo "----------------------------------------------------------"
exit 1
fi
