#!/bin/bash

# get the temp from TMP101 A
temp=$(i2cget -y 2 0x4a 0)
# convert the temp from celsius to fahrenheit
temp2=$(($temp *9/5 +32))
# get the temp from TMP101 B
tmp=$(i2cget -y 2 0x48 0)
# convert the temp from celsius to fahrenheit
tmp2=$(($tmp *9/5 +32))
# print out the converted temp of TMP101 A to the terminal window
echo TMP101 A: $temp2 F
# print out the converted temp of TMP101 B to the terminal window
echo TMP101 B: $tmp2 F
