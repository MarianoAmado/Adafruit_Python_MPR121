# Burn SD with standard Raspbian

# Basic config:
- 	raspi-config:
	> - i2c
	> - SSH
	> - boot to CLI
-	wifi:
	>/etc/wpa_supplicant/wpa_supplicant.conf, or from the desktop
- 	change pass, clean fs, etc.

# Install library (FORK!) (and copy files):
	sudo apt-get update
    sudo apt-get install build-essential python-dev python-smbus python-pip git
    git clone https://github.com/MarianoAmado/Adafruit_Python_MPR121.git
    sudo python setup.py develop

>modificar sensibilidad: MPR121.py (line 106)

# Add to /boot/config.txt :
	dtoverlay=i2c-bcm2708  #i2c driver Fix.
	dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4  #PWM Audio output (gpio 18 & 13).
	dtoverlay=gpio-shutdown,gpio_pin=5  #Shutdown button pin.

# Execute on start:
	sudo nano /etc/systemd/system/TOCA.service
	-
	[Unit]
	Description=Servicio TOCA murales
	After=multi-user.target

	[Service]
	Type=idle
	ExecStart=/usr/bin/python /home/pi/myscript.py

	[Install]
	WantedBy=multi-user.target
	-

	sudo systemctl enable TOCA.service
	sudo systemctl start TOCA.service
	systemctl status TOCA.service

# MPR121 and Audio PCB ..

>changes to original:
self._i2c_retry(self._device.write8, MPR121_CONFIG1, 0x20) 
self._i2c_retry(self._device.write8, MPR121_CONFIG2, 0x3A)				   
