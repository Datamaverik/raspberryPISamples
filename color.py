import RPi.GPIO as GPIO
import time 

GPIO.setmode(GPIO.BCM)

S2, S3 = 22, 23
OUT = 24

GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
GPIO.setup(OUT, GPIO.IN)

def measure():
    count = 0
    start = time.time()
    while time.time() - start < 0.5:
        if GPIO.input(OUT):
            count += 1
    return count

try:
    while True:
        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.LOW)
        red = measure()
        
        GPIO.output(S2, GPIO.LOW)
        GPIO.output(S3, GPIO.HIGH)
        blue = measure()
        
        GPIO.output(S2, GPIO.HIGH)
        GPIO.output(S3, GPIO.HIGH)
        green = measure()
        
        print(f"R: {red} G: {green} B: {blue}")
        
        if red > green and red > blue:
            print("Red detected")
        elif green > red and green > blue:
            print("Green detected")
        else:
            print("Blue detected")
            
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    
# VCC -> 3.3V
# GND -> GND
# OUT -> GPIO24
# S0 -> GPIO17
# S1 -> GPIO27
# S2 -> GPIO22
# S3 -> GPIO23