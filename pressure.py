import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PRES = 25
LED = 17

GPIO.setup(PRES, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.input(PRES):
            print("Pressure detected")
            GPIO.output(LED, True)
        else:
            print("No Pressure")
            GPIO.output(LED, False)
            
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    
# VCC -> 3.3V
# GND -> GND
# DO -> GPIO25