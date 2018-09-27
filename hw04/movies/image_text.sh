# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

convert tux.png -background white label:'Trey Lewis' \
	-gravity Center -append \
	$TMP_FILE

sudo fbi -noverbose -T 1 -a $TMP_FILE
