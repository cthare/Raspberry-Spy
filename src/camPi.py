import RPi.GPIO as GPIO
import time
import picamera
import datetime
from mailPi import sendMessage

# Set filename for photo
# using date/time structure
def getFileName():
	return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.png")

# GPIO sensor settings
def initiateSensor(pinNumber):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pinNumber, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Set sensor settings and run camera
def runCam():
	sensorPin = 7
	prevState = False
	currState = False
	cam = picamera.PiCamera()

	initiateSensor(sensorPin)

	# Currently set to a infinite loop
	# to continously run. Exit program
	# with keyboard interrupt
	while True:
		time.sleep(5)
		prevState = currState
		currState = GPIO.input(sensorPin)
		if currState != prevState:
			if currState:
				fileName = getFileName()
				cam.capture(fileName)
				sendMessage(fileName)