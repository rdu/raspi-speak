gcc usbreset.c -o usbreset
mv usbreset /usr/local/sbin/
chown root:root /usr/local/sbin/usbreset
chmod 0755 /usr/local/sbin/usbreset
