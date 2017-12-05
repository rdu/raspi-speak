sleep 10

echo 0 > /sys/bus/usb/devices/1-1/authorized
sleep 2
echo 1 > /sys/bus/usb/devices/1-1/authorized
sleep 3
docker restart listener
