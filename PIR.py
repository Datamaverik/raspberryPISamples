import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIR = 21
LED = 17
BUZZER = 18

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

try:
    while True:
        if GPIO.input(PIR):
            print("Motion detected")
            GPIO.output(LED, True)
            GPIO.output(BUZZER, True)
        else:
            print("No motion")
            GPIO.output(LED, False)
            GPIO.output(BUZZER, False)
            
        time.sleep(1)
        
except KeyboardInterrupt:
    print("exiting..")
    
finally:
    GPIO.cleanup()

# VCC -> 5V
# GND -> GND
# OUT -> GPIO21