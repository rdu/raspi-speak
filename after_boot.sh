sleep 60

FILE1=/dev/bus/usb/001/003
FILE2=/dev/bus/usb/001/002
if [ -r "$FILE1" ]; then
	usbreset $FILE1
fi
if [ -r "$FILE2" ]; then
	usbreset $FILE2
fi
sleep 10
docker restart listener
