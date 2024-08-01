#!/bin/sh
source /home/hduser/smp/conf/env.sh
TODAY=$(date +"%Y-%m-%d-%H%M")
NOW=$(date +"%Y-%m-%d")

DIR="/home/hduser/hdfs-storage"
if [[ ! -e $DIR/$NOW ]]; then
	mkdir -p "$DIR/$NOW"
fi
echo 'Total Disk Space in HDFS' > $DIR/$NOW/$TODAY-hdfs_usage.txt
echo '###############################################################' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
/home/hduser/smp/hadoop-2.5.1/bin/hdfs dfs -df -h / 2>/dev/null >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo '' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo 'Disk Usage of HDFS Root File System' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo '###############################################################' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
/home/hduser/smp/hadoop-2.5.1/bin/hdfs dfs -du -h / >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo '' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo 'Disk Usage of HBase, /hbase, /hbase/data, /hbase/data/data/default' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo '###############################################################' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo '' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
/home/hduser/smp/hadoop-2.5.1/bin/hdfs dfs -du -h /hbase 2>/dev/null >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo '' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
/home/hduser/smp/hadoop-2.5.1/bin/hdfs dfs -du -h /hbase/data 2>/dev/null >>$DIR/$NOW/$TODAY-hdfs_usage.txt
echo '' >>$DIR/$NOW/$TODAY-hdfs_usage.txt
/home/hduser/smp/hadoop-2.5.1/bin/hdfs dfs -du -h /hbase/data/data/default 2>/dev/null >>$DIR/$NOW/$TODAY-hdfs_usage.txt
#echo 'getting dump of HBase UI'
hadoop dfsadmin -report 2>/dev/null | sed -n '/Configured/,/Name/p; /Live/q' >>$DIR/$NOW/hadoop_50070_ui.txt
curl -Lo $DIR/$NOW/hbase_ui.html http://10.90.120.11:16010/master-status
