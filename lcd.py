# sudo raspi-config
# enable i2c in the interfacing option
# sudo reboot
# i2cdetect -l
# i2cdetect -y 1
# sudo pi3 install rpi_lcd
# sudo find /usr/local -name rpi_lcd 2> /dev/null -> gives the location of the library
# go to that location and edit the address if needed

from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

def safe_exit(signum, frame):
    exit(1)
    
signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
    lcd.text("Hello,", 1)
    lcd.text("Raspberry Pi", 2)
    pause()

except KeyboardInterrupt:
    pass

finally:
    lcd.clear()
    
# GND -> GND (PIN6)
# VCC -> 5V (PIN2)
# SDA -> PIN3
# SCL -> PIN5