# Created by Carmelito Andrade for the DIY Drum kit project
#Based on Adafruit's python libary for 12-Key Capacitive Touch Sensor Breakout - MPR121
#clone the forked github repo from - https://github.com/adafruit/Adafruit_Python_MPR121
#git clone https://github.com/CJAndrade/DIY-Drum-Kit
#sudo python setup.py install


import sys
import time
import os
import subprocess
import Adafruit_MPR121.MPR121 as MPR121
import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()
folderDial = "P9_33"
tuneDial = "P9_35"
tuneFileAt = '/root/soundFiles/tunes'
song1Poll = 0
song2Poll = 0
wavFileAt = '/root/soundFiles/basicDrum'
os.chdir(wavFileAt)

print 'Adafruit MPR121 Capacitive Touch Sensor Test'

# Create MPR121 instance.
cap = MPR121.MPR121()

# Initialize communication with MPR121 using default I2C bus of device, and 
# default I2C address (0x5A).  On BeagleBone Black will default to I2C bus 0.
if not cap.begin(bus=1):
    print 'Error initializing MPR121.  Check your wiring!'
    sys.exit(1)

# Main loop to print a message every time a pin is touched.
print 'Press Ctrl-C to quit.'
#subprocess.call("aplay loneyDay.wav &",shell=True)
print 'ready to use MPR121'
last_touched = cap.touched()

while True:
        potValue = ADC.read(folderDial)
        #print "Folder Pot Value: ",potValue
	potValueTune = ADC.read(tuneDial)	
	#print "Song Dial Value:",potValueTune

	while True:
    		current_touched = cap.touched()
    # Check each pin's last and current state to see if it was pressed or released.
                potValue = ADC.read(folderDial)
                print "Tune Pot Value : ",potValueTune
		if potValueTune <0.5:
			print "Tune Pot Value less than 0.5"
			#if song1Poll == 0:
                #song1 = subprocess.Popen("aplay /root/soundFiles/tunes/Birdsong.wav",shell = True)
				#time.sleep(1)
				#song1Poll = song1.poll()
				#print "song1Poll" + str(song1Poll)
		
		else: 
			print "Tune Pot Value GREATER than 0.5"
			#subprocess.call("",shell = True)
                #subprocess.call(command,shell = True)
		#song1Poll = song1.poll()

		#Changing the Folder based on the Pot values - Blue Dial aka the Folder Dial
                if  potValue <0.3:
                        print "Sound pot 0.3 Basic Drums"
                        wavFileAt = '/root/soundFiles/basicDrum'
                        os.chdir(wavFileAt)
                elif potValue > 0.3 and potValue <0.6:
                        print "Sound pot 0.3 to 0.6 qucik Drums"
                        wavFileAt = '/root/soundFiles/quicksDrum'
                        os.chdir(wavFileAt)
		elif potValue > 0.6 and potValue <0.85:
                	print "Sound pot value 0.6 to 0.85 Bass Guitar "
			wavFileAt = '/root/soundFiles/bassGuitar'
			os.chdir(wavFileAt)
                else:
                        print "Sound pot value 0.85 Funk files"
			wavFileAt = '/root/soundFiles/funk'
			os.chdir(wavFileAt)

   		for i in range(12):
        # Each pin is represented by a bit in the touched value.  A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        		pin_bit = 1 << i
			#potValue = ADC.read(folderDial)
        		#print "Pot Value : ",potValue
                        #if potValue > 0.5 and potValue <0.7:
		        #        print "value betweem 0.5 and 0.7"
			#if potValue > 0.7:
                	#	print "value greater than 0.7"
			#if potValue <0.5:
			#	print "value is less than 0.5"
				

        # First check if transitioned from not touched to touched.
        		if current_touched & pin_bit and not last_touched & pin_bit:
            			print '{0} touched!'.format(i)
	    			command ="aplay "+str(i) +".wav"
	    			print command
	    			subprocess.call(command,shell = True)	    
        # Next check if transitioned from touched to not touched.
        		if not current_touched & pin_bit and last_touched & pin_bit:
            			print '{0} released!'.format(i)

    # Update last state and wait a short period before repeating.
    		last_touched = current_touched
    		time.sleep(0.1)#using 0.05 is more re-active
		if potValue < 0.5:
			print "value less than 0.5"
			break