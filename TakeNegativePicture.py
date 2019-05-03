#	Angkan Biswas
#	03.05.2019
#	To take a picture using the web camera of the computer.

import cv2
import numpy

camera = cv2.VideoCapture(0)					#	Get access of the web camera.
cameraStatus, picture = camera.read()				#	Take a picture using the camera.

positivePic = cv2.resize(picture, (384, 256))			#	Resize picture 
negativePic = 255 - positivePic					#	Convert into negative picture
concatePic = numpy.concatenate((positivePic,negativePic))	#	Concate pictures
cv2.imshow('My Picture', concatePic)	
camera.release()						#	Release the captured camera

cv2.waitKey(0)
