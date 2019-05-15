#	Angkan Biswas
#	08.05.2019
#	Play a video file.

import cv2

camera = cv2.VideoCapture('/home/dell/Downloads/RoseBlooming.mp4')		#	Upload a video file from source.

for i in range(800): 
	_, frame = camera.read()						#	Take a frame.
	frame_1 = cv2.resize(frame,(300,200)) 					# 	Resize the freame.
	cv2.imshow('RoseBlooming',frame_1)					#	Display the frame.
	cv2.waitKey(50)								#	Hold the display window for 50 millisecond

camera.release()								#	Release the captured camera
