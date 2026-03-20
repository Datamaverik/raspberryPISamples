from pyfingerprint.pyfingerprint import PyFingerprint

try:
    f = PyFingerprint('/dev/serial10', 57600)
    
    if not f.verifyPassword():
        raise ValueError('Wrong password')
    
    print("Sensor initialized")
    
    while True:
        print("Waiting for finger...")
        
        while not f.readImage():
            pass
        
        f.convertImage(0x01)
        
        result = f.searchTemplate()
        
        postion = result[0]
        
        if postion >= 0:
            print("Match found at postion ", postion)
        else:
            print("No match found")
        
except Exception as e:
    print("Error: ", e)

# VCC -> 5v
# GND -> GND
# TX -> GPIO15
# RX -> GPIO14