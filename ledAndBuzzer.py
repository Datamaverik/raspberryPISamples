import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED = 17
BUZZER = 18

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

try:
    while True:
        GPIO.output(LED, True)
        GPIO.output(BUZZER, True)
        print("Led on, buzzer on")
        time.sleep(1)
        
        GPIO.output(LED, False)
        GPIO.output(BUZZER, False)
        print("Led and buzzer off")
        time.sleep(1)
        
except KeyboardInterrupt:
    print("exiting...")

finally:
    GPIO.cleanup()
    
# led (+ve side) bigger side -> GPIO17
# led shorter side -> GND
# Buzzer (+ve side) -> GPIO18
# Buzzer (-ve side) -> GND