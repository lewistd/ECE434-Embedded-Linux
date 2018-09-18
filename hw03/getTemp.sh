#!/bin/bash

temp=$(i2cget -y 2 0x4a 0)
temp2=$(($temp *9/5 +32))
#tmp=$(i2cget -y 2 0x49 0)
#tmp2=$(($tmp *9/5 +32))
echo TMP101 A: $temp2 F
#echo TMP101 B: $tmp2 F
