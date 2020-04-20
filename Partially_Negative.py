#	Angkan Biswas
#	20.04.2020
#	To take a picture using the web camera & perform negation part by part.

import cv2
import numpy

camera = cv2.VideoCapture(0)					# Get access of the web camera.
cameraStatus, picture = camera.read()				# ake a picture using the camera.
camera.release()						# Release the captured camera

picture = cv2.resize(picture, (384, 256))			# Resize picture 

x = 0; y = 0; w = 192; h = 128
picture[y:y+h, x:x+w] = 255 - picture[y:y+h, x:x+w]		# Perform negation on the top-left part
x = 192; y =128; w = 192; h = 128
picture[y:y+h, x:x+w] = 255 - picture[y:y+h, x:x+w]		# Perform negation on the bottom-right part

cv2.imshow('My Picture', picture)	
cv2.waitKey(0)
