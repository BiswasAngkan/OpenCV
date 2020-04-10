#	Angkan Biswas
#	10.04.2020
#	Capture a video file.

import cv2
import numpy as np

camera = cv2.VideoCapture(0)							#	Open a cemera.

lowThreshold = 40							
highThreshold = 250								#	Generaly, highThreshold = 3*lowTheshold

for i in range(1000): 
	_, frame = camera.read()						#	Take a frame.
	
	resizeFrame = cv2.resize(frame,(300,200))				# 	Resize the freame.
	negativeFrame = 255 - resizeFrame					#	Negative frame
	concateFrame1 = np.concatenate((resizeFrame, negativeFrame), axis = 1) 	#	Add two frames side by side
	print(concateFrame1.shape)

	edge = cv2.Canny(resizeFrame, lowThreshold, highThreshold)		#	Detect edge using Canny algorithm
	print(edge.shape)	
	edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)				#	Convert 2D edge into 3D edge	
	print(edge.shape)	
	concateFrame2 = np.concatenate((concateFrame1, edge), axis = 1) 	#	Add two frames side by side
	
	cv2.imshow('My Face',concateFrame2)					#	Display the frame.
	cv2.waitKey(10)								#	Hold the display window for 50 millisecond

camera.release()								#	Release the captured camera










