#	Angkan Biswas
#	19.04.2020
#	Capture a video file & rotate translate continuosly

import cv2
import imutils

camera = cv2.VideoCapture(0)							# Open a cemera.

degree = 0
x = 2
y = 2

for i in range(200): 
	_, frame = camera.read()						# Take a frame.
	resizeFrame = cv2.resize(frame,(300,200))				# Resize the frame.
	
	rotateImg = imutils.rotate(resizeFrame, degree)				# To rotate the frame		
	translateImg = imutils.translate(rotateImg, x , y)			# to translate the rotated frame

	cv2.imshow('My Face',translateImg)					# Display the frame.
	cv2.waitKey(10)								# Hold the display window for 10 millisecond
	
	degree = degree + 2
	x = x + 1
	y = y + 1

camera.release()								# Release the captured camera










