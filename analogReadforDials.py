#Testing readings from the potentiometer dials connected to the 3D printed part
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()
analogPinBlue = "P9_35"
analogPinYel = "P9_33"
while(1):
        potValueBlue = ADC.read(analogPinBlue)
        potValYel = ADC.read(analogPinYel)
        print "Pot Value Blue : ",potValueBlue
        print "Pot Value Green :",potValYel
        time.sleep(5)
