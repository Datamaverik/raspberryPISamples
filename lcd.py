# sudo raspi-config
# Interface Options → I2C → Enable
# sudo reboot
# i2cdetect -y 1
# sudo pi3 install rpi_lcd
# sudo find /usr/local -name rpi_lcd 2> /dev/null -> gives the location of the library
# go to that location and edit the address if needed

# sudo apt update
# sudo apt install python3-rpi.gpio python3-smbus i2c-tools
# sudo apt install python3-rplcd
# sudo apt install python3-gpiozero

from RPLCD.gpio import CharLCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

lcd = CharLCD(
    pin_rs=25,
    pin_e=24,
    pins_data=[23, 17, 27, 22],
    numbering_mode=GPIO.BCM
)

try:
    lcd.clear()
    lcd.write_string("Hello Shreyash!")

    time.sleep(2)

    lcd.clear()
    lcd.write_string("Parallel LCD")

except KeyboardInterrupt:
    lcd.clear()
    
# VSS	GND
# VDD	5V
# V0	Potentiometer (contrast)
# RS	GPIO25
# RW	GND
# E	GPIO24
# D4	GPIO23
# D5	GPIO17
# D6	GPIO27
# D7	GPIO22
# A (LED+)	5V
# K (LED-)	GND