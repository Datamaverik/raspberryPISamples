import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

MQ3 = 23
LED = 17

GPIO.setup(MQ3, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.input(MQ3):
            print("Alcohol detected")
            GPIO.output(LED, True)
        else:
            print("No alcohol")
            GPIO.output(LED, False)
        
        time.sleep(1)

except KeyboardInterrupt:
    print("stopping...")
    
finally:
    GPIO.cleanup()

# VCC -> 5V
# GND -> GND
# DO (Digital Output) -> GPIO23