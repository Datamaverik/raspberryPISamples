import adafruit_dht
import board
import time

dht = adafruit_dht.DHT11(board.D4)

try:
    while True:
        temp = dht.temperature
        humidity = dht.humidity
        
        print(f"Temp: {temp} Humidity: {humidity}")
        
        time.sleep(2)
        
except KeyboardInterrupt:
    print("ending..")
    
# VCC -> 3.3V
# DATA -> GPIO4
# GND -> GND