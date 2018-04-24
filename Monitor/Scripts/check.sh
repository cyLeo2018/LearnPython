#!/usr/bin/env bash

check_cpu(){
C_number=`grep -c 'model name' /proc/cpuinfo`
User=`uptime|awk -F ',' '{print $3}'`
Load=`uptime|awk -F ',' '{print $6}'`
NAME=`hostname`
TYPE=`cat /proc/cpuinfo |grep 'model name'|head -1|awk -F ':' '{print $2}'|awk -F '(' '{print $1}'`
echo "主机名:${NAME}"
echo "CPU数量:${C_number}"
echo "CPU型号:${TYPE}"
echo "当前登录用户:${User}"
echo "15分钟内CPU负载:${Load}"
}

check_memory(){
MemTotal=`cat /proc/meminfo|grep MemTotal|awk '{print $2}'`
MemFree=`cat /proc/meminfo|grep MemFree|awk '{print $2}'`
Buffers=`cat /proc/meminfo|grep Buffers|awk '{print $2}'`
SwapTotal=`cat /proc/meminfo|grep SwapTotal|awk '{print $2}'`
SwapCached=`cat /proc/meminfo|grep SwapCached|awk '{print $2}'`
echo "总内存:$[ $MemTotal/1024 ]MB"
echo "剩余内存:$[ $MemFree/1024 ]MB"
echo "Buffers:$[ $Buffers/1024 ]MB"
echo "SwapTotal:$[ $SwapTotal/1024 ]MB"
echo "SwapCached:$[ $SwapCached/1024 ]MB"
}

check_disk(){
df -hT|grep -v tmp|grep -v Filesystem|awk '{print $7"分区:已用"$6}'
}

check_inode(){
df -i|awk '{print $5}'|egrep -v 'IUse'|sort |head -1
}

echo '################### check CPU ####################'
check_cpu
echo '################### check Memory #################'
check_memory
echo '################### check Disk ###################'
check_disk
echo '################### echo File Inode ##############'
check_inode
echo '检查完成!'