import Adafruit_BBIO.GPIO as GPIO
import time
import os
import datetime
#install the soundcloud python wrapper from github at https://github.com/soundcloud/soundcloud-python ​ 
import soundcloud

#Button and LED connections
recordLED = "P9_11"
uploadLED = "P9_12"
recordButton = "P9_13"
uploadButton = "P9_15"
#Create a soundcloud auth token using the user credential auth flow, paste your token below
soundcloudToken = "X-XXXXX-XXXXXXXX-XXXXXXXXXXXXXX"
# create a client object with access token
client = soundcloud.Client(access_token=soundcloudToken)

command =""
soundFileName=""
print "Test program to record and upload to soundcloud"
#dateTimeNow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
#print dateTimeNow

#use lsusb and aplay -l to check if your external USB sound card is detected. 
#record command using ALSA, increase the Mic volume using alsamixer
# arecord -D plughw:0 --duration=10 -f cd -vv testsound.wav

#to store the recorded .wav files, create the recordtests folder
os.chdir('/root/recordtests')

GPIO.setup(recordLED, GPIO.OUT)
GPIO.setup(uploadLED, GPIO.OUT)
GPIO.setup(recordButton, GPIO.IN)
GPIO.setup(uploadButton, GPIO.IN)

while True:
    if GPIO.input(recordButton):
        GPIO.output(recordLED, GPIO.HIGH)
        #getting current date and time
        dateTimeNow = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        print "Recording ....."
        soundFileName = "TestSound"+dateTimeNow+".wav"
        command = "arecord -D plughw:0 --duration=20 -f cd -vv "+ soundFileName
        print command
        os.system(command)
        GPIO.output(recordLED, GPIO.LOW)

    if GPIO.input(uploadButton):
        GPIO.output(uploadLED, GPIO.HIGH)
        print "uploading to soundcloud ....."
        # upload audio file to soundcloud
        track = client.post('/tracks', track={
        'title': soundFileName,
        'sharing': 'private',
                'asset_data': open(soundFileName, 'rb')
        })
        # print track link
        print track.permalink_url
        GPIO.output(uploadLED, GPIO.LOW)

    time.sleep(0.5)

