#!/bin/bash
file=$(hadoop fs -ls /tmp/hadoop-yarn/staging/hduser/.staging/job_1530007175344_0005/libjars | grep  '.*2018-[0-8].*' | awk '{print $8}' 2>/dev/null)
file1=$(hadoop fs -ls /tmp/hadoop-yarn/staging/hduser/.staging/job_1530007175344_0005/libjars | grep  '.*2017-[0-8].*' | awk '{print $8}' 2>/dev/null)
hadoop fs -mkdir /tmp/2018 2>/dev/null
hadoop fs -mkdir /tmp/2017 2>/dev/null
counter=0
counter1=0
for i in $file
do
hadoop fs -cp $i /tmp/2018/ 2>/dev/null
counter=$(($counter + 1))
done
for f in $file1
do
hadoop fs -cp $f /tmp/2017/ 2>/dev/null
counter1=$(($counter1 + 1))
done

echo "Total processed files in 2018: $counter"
echo "Total processed files in 2017: $counter1"
