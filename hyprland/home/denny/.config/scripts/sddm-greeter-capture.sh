TMPXAUTHORITY=$(ls /var/run/sddm/)
sleep 30
DISPLAY=:0 XAUTHORITY=/var/run/sddm/$TMPXAUTHORITY xwd -root > /tmp/greeter.xwd
convert /tmp/greeter.xwd /home/denny/greeter.png
