#!/bin/bash
# Set up gpio 7 to read and gpio 3 to write
cd /sys/class/gpio
echo 3 > export
echo 7 > export
echo 30 > export
echo 31 > export
echo 48 > export
echo 50 > export

echo in  > gpio7/direction
echo out > gpio3/direction
echo in  >  gpio31/direction
echo out > gpio30/direction
echo in  > gpio48/direction
echo out > gpio50/direction
