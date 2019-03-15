# Burn SD with standard Raspbian

# Basic config (disable gui, wifi, pass, clean fs, I2C enable, etc):
	Wifi: /etc/wpa_supplicant/wpa_supplicant.conf

# Install library (FORK!) (and copy files):
	sudo apt-get update
    sudo apt-get install build-essential python-dev python-smbus python-pip git
  *----> git clone https://github.com/adafruit/Adafruit_Python_MPR121.git
    sudo python setup.py install

# Fix for I2C driver:
	 Add to /boot/config.txt: dtoverlay=i2c-bcm2708

# Set up PWM audio (GPIO 18 & 13):
	Add to /boot/config.txt: dtoverlay=pwm-2chan,pin=18,func=2,pin2=13,func2=4

# Setup Shutdown button:
	Add to /boot/config.txt: dtoverlay=gpio-shutdown,gpio_pin=12

# Execute on start:
	sudo nano /etc/systemd/system/TOCA.service (...) ##python folder!
	
	sudo systemctl enable TOCA.service
	sudo systemctl start TOCA.service
	systemctl status TOCA.service

# MPR121 and Audio PCB C:

*------>

	self._i2c_retry(self._device.write8, MPR121_CONFIG1, 0x20) 
	self._i2c_retry(self._device.write8, MPR121_CONFIG2, 0x3A)				   