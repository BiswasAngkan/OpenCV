#	Angkan Biswas
#	11.04.2020
#	Capture pictures using web camera & concatenate with existing video file.

import cv2
import numpy as np

camera1 = cv2.VideoCapture('/home/dell/Downloads/RoseBlooming.mp4')		# Open an existing video file		
camera2 = cv2.VideoCapture(0)							# Open a cemera.

for i in range(100): 
	_, frame1 = camera1.read()						# Take a frame from existing video file.
	_, frame2 = camera2.read()						# Take a picture from the web camera.

	resizeFrame1 = cv2.resize(frame1,(300,200))
	resizeFrame2 = cv2.resize(frame2,(300,200))				# Resize the freame.

	concateFrame = np.concatenate((resizeFrame1, resizeFrame2),axis =1) 	# Add two frames side by side
	
	cv2.imshow('RoseBlooming + Myface',concateFrame)			# Display the frame.
	cv2.waitKey(10)								# Hold the display window for 10 millisecond

camera1.release()							
camera2.release()								# Release the open camera










