Run manually with 
```nohup /usr/bin/python3 garage-door.py &```

the following libraries need to be installed

sudo apt install python3-pip python3-gpiozero
sudo pip3 install paho-mqtt

Also, to have the script run at boot, I created a System Service. See garagedoor.service

Add file to /etc/systemd/system/ directory

Then run ```sudo systemctl enable garagedoor.service```


----


Example output when checking systemd for my service's status:
```
pi@garagepi:~ $ sudo systemctl status garagedoor.service
● garagedoor.service - Garage Door Opener Command Script
   Loaded: loaded (/etc/systemd/system/garagedoor.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2018-12-08 17:02:24 UTC; 1min 37s ago
 Main PID: 420 (python3)
   CGroup: /system.slice/garagedoor.service
           └─420 /usr/bin/python3 /home/pi/garage-door.py

Dec 08 17:02:24 garagepi.ryan systemd[1]: Started Garage Door Opener Command Script.
```
---

For systemd help, see these findings that helped me:
https://raspberrypi.stackexchange.com/questions/84892/run-python-script-at-startup-with-systemd-service
https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/sect-managing_services_with_systemd-unit_files
https://unix.stackexchange.com/questions/126009/cause-a-script-to-execute-after-networking-has-started

It restart service on failure, looking into:
https://singlebrook.com/2017/10/23/auto-restart-crashed-service-systemd/