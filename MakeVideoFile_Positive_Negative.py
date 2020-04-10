#	Angkan Biswas
#	10.04.2020
#	Capture a video file.

import cv2
import numpy as np

camera = cv2.VideoCapture(0)							#	Open a cemera.

for i in range(100): 
	_, frame = camera.read()						#	Take a frame.
	
	resizeFrame = cv2.resize(frame,(300,200))				# 	Resize the freame.
	negativeFrame = 255 - resizeFrame					#	Negative frame
	concateFrame = np.concatenate((resizeFrame, negativeFrame), axis = 1) 	#	Add two frames side by side
	
	cv2.imshow('My Face',concateFrame)					#	Display the frame.
	cv2.waitKey(10)								#	Hold the display window for 50 millisecond

camera.release()								#	Release the captured camera










