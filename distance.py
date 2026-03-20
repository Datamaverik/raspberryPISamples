import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 5
ECHO = 6

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        GPIO.output(TRIG, False)
        time.sleep(0.1)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == 0:
            start = time.time()
            
        while GPIO.input(ECHO) == 1:
            end = time.time()
            
        duration = end - start
        distance = (duration * 34300) / 2
        
        print(f"Distance: {distance:.2f} cm")
        
        time.sleep(1)
        
except KeyboardInterrupt:
    print("exiting...")
    
finally:
    GPIO.cleanup()

# VCC -> 5V
# GND -> GND
# TRIG -> GPOI5
# ECHO -> GPIO6